#!/usr/bin/env python3
"""
宝塔面板 (BT Panel / aaPanel) 加密 .py 文件解密工具
===================================================

用法:
    python3 bt_decrypt.py <加密文件路径> [输出文件路径]

示例:
    python3 bt_decrypt.py comMod.py                    # 输出 comMod_decrypted.py
    python3 bt_decrypt.py comMod.py decrypted.py       # 输出 decrypted.py

支持的加密格式:
    - 每行独立 base64 + AES-128-CBC 加密
    - 所有块统一解密后通过 PKCS7 padding 自动识别空行
    - 密钥: Z2B87NEAS2BkxTrh
    -  IV : WwadH66EGWpeeTT6
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
        print("请先安装 pycryptodome: pip3 install pycryptodome")
        sys.exit(1)

# === 解密参数 ===
KEY = b"Z2B87NEAS2BkxTrh"   # 16 字节 AES-128 密钥
IV  = b"WwadH66EGWpeeTT6"   # 16 字节 CBC 初始向量
MODE = AES.MODE_CBC


def decrypt_line(line: str) -> str:
    """解密单行 base64 密文，返回明文字符串"""
    ciphertext = base64.b64decode(line)

    # AES-CBC 解密 — 所有块统一处理（不跳过 16 字节块）
    cipher = AES.new(KEY, MODE, IV)
    plaintext = cipher.decrypt(ciphertext)

    # PKCS7 去填充：pad_len 范围 1~16（含全填充 16）
    pad_len = plaintext[-1]
    if 0 < pad_len <= 16 and all(b == pad_len for b in plaintext[-pad_len:]):
        plaintext = plaintext[:-pad_len]

    return plaintext.decode("utf-8") if plaintext else ""


def decrypt_file(input_path: str, output_path: str = None) -> str:
    """解密整个加密文件"""
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        dir_name = os.path.dirname(input_path) or "."
        output_path = os.path.join(dir_name, f"{base_name}_decrypted.py")

    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    results = []
    errors = 0
    for line in lines:
        try:
            results.append(decrypt_line(line))
        except Exception as e:
            results.append(f"# [解密失败] {e}")
            errors += 1

    output = "\n".join(results)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

    return output_path, len(lines), errors


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(input_path):
        print(f"错误: 文件不存在 - {input_path}")
        sys.exit(1)

    output_path, total_lines, errors = decrypt_file(input_path, output_path)

    size = os.path.getsize(output_path)
    print(f"解密完成!")
    print(f"  输入: {input_path} ({total_lines} 行密文)")
    print(f"  输出: {output_path} ({size:,} 字节)")
    if errors:
        print(f"  警告: {errors} 行解密失败")


if __name__ == "__main__":
    main()
