#!/usr/bin/env python3
"""
从 PluginLoader.so 中提取 AES 密钥

用法:
    python3 extract_key.py PluginLoader.xxx.so

原理:
    搜索 .text 段中 32 字节的 ASCII 数组（如 _get_sgin_key 的 v4 数组），
    按奇偶位拆分为 key 和 IV，然后用 comMod 密文验证。
"""

import sys
import os
import base64

try:
    from Cryptodome.Cipher import AES
except ImportError:
    try:
        from Crypto.Cipher import AES
    except ImportError:
        print("pip3 install pycryptodome")
        sys.exit(1)


def extract_keys_from_so(so_path: str):
    """从 .so 文件中搜索潜在密钥"""
    with open(so_path, "rb") as f:
        data = f.read()

    # ELF .text 段偏移 (适用于 x86_64 PluginLoader)
    # 实际范围通过 ELF header 解析
    try:
        text_start, text_end = parse_elf_text_section(data)
    except Exception:
        # 回退: 搜索整个文件 (会慢一些)
        text_start, text_end = 0, len(data)

    candidates = set()
    for i in range(text_start, min(text_end, len(data)) - 32):
        chunk = data[i : i + 32]
        if all(48 <= b <= 122 for b in chunk):
            s = chunk.decode()
            if len(set(s)) >= 15:
                candidates.add((s[::2], s[1::2]))

    return candidates


def parse_elf_text_section(data: bytes):
    """解析 ELF 找到 .text 段偏移"""
    import struct

    if data[:4] != b"\x7fELF":
        raise ValueError("不是 ELF 文件")

    is_64bit = data[4] == 2
    if is_64bit:
        e_shoff = struct.unpack("<Q", data[0x28:0x30])[0]
        e_shentsize = struct.unpack("<H", data[0x3A:0x3C])[0]
        e_shnum = struct.unpack("<H", data[0x3C:0x3E])[0]
        e_shstrndx = struct.unpack("<H", data[0x3E:0x40])[0]
    else:
        e_shoff = struct.unpack("<I", data[0x20:0x24])[0]
        e_shentsize = struct.unpack("<H", data[0x2E:0x30])[0]
        e_shnum = struct.unpack("<H", data[0x30:0x32])[0]
        e_shstrndx = struct.unpack("<H", data[0x32:0x34])[0]

    # 解析 section headers
    shstrtab_off = e_shoff + e_shstrndx * e_shentsize
    if is_64bit:
        shstrtab_addr = struct.unpack("<Q", data[shstrtab_off + 24 : shstrtab_off + 32])[0]
    else:
        shstrtab_addr = struct.unpack("<I", data[shstrtab_off + 16 : shstrtab_off + 20])[0]

    for i in range(e_shnum):
        sh_off = e_shoff + i * e_shentsize
        name_idx = struct.unpack("<I", data[sh_off : sh_off + 4])[0]
        name_end = data[shstrtab_addr + name_idx :].find(b"\x00")
        name = data[shstrtab_addr + name_idx : shstrtab_addr + name_idx + name_end].decode()

        if name == ".text":
            if is_64bit:
                sh_offset = struct.unpack("<Q", data[sh_off + 24 : sh_off + 32])[0]
                sh_size = struct.unpack("<Q", data[sh_off + 32 : sh_off + 40])[0]
            else:
                sh_offset = struct.unpack("<I", data[sh_off + 16 : sh_off + 20])[0]
                sh_size = struct.unpack("<I", data[sh_off + 20 : sh_off + 24])[0]
            return sh_offset, sh_offset + sh_size

    raise ValueError("找不到 .text 段")


def test_key_with_sample(even: str, odd: str, test_file: str) -> bool:
    """用测试文件验证密钥对"""
    if not os.path.exists(test_file):
        return False

    key = even.encode()[:16].ljust(16, b"\x00")
    iv = odd.encode()[:16].ljust(16, b"\x00")

    with open(test_file) as f:
        lines = [l.strip() for l in f if l.strip()]

    good = 0
    for line in lines[:200]:
        try:
            dl = base64.b64decode(line)
            if len(dl) == 16:
                continue
            cipher = AES.new(key, AES.MODE_CBC, iv)
            dec = cipher.decrypt(dl)
            printable = sum(1 for b in dec if 32 <= b < 127)
            if printable >= len(dec) * 0.8:
                good += 1
        except:
            pass

    return good >= 10


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    so_path = sys.argv[1]
    test_file = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(so_path):
        print(f"错误: {so_path} 不存在")
        sys.exit(1)

    print(f"解析 {so_path} ...")
    candidates = extract_keys_from_so(so_path)
    print(f"找到 {len(candidates)} 个候选密钥对")

    if test_file and os.path.exists(test_file):
        print(f"用 {test_file} 验证...")
        for even, odd in candidates:
            if test_key_with_sample(even, odd, test_file):
                print(f"\n✅ 有效密钥: key='{even}', iv='{odd}'")
                print(f"\n在 bt_decrypt.py 中更新:")
                print(f'  KEY = b"{even}"')
                print(f'  IV  = b"{odd}"')
                return
        print("未找到有效密钥（可能需要用不同模式测试）")
    else:
        print("\n候选密钥对 (需要用加密文件验证):")
        for even, odd in list(candidates)[:20]:
            print(f"  key='{even}'  iv='{odd}'")


if __name__ == "__main__":
    main()
