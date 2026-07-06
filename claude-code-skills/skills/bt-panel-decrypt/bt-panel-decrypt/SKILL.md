---
name: bt-panel-decrypt
description: 宝塔面板 (BT Panel / aaPanel) 商业版加密 Python 源码模块解密工具。当用户需要解密宝塔面板的 comMod.py 或其他 .py 加密文件时应使用此 skill。加密特征：文件内容全为 Base64 字符串 (A-Za-z0-9+/=)，每行独立 AES-128-CBC 加密，全部块统一解密后通过 PKCS7 padding 自动恢复。密钥 Z2B87NEAS2BkxTrh，IV WwadH66EGWpeeTT6。
agent_created: true
---

# 宝塔面板加密文件解密

## 快速解密

```bash
pip3 install pycryptodome
python3 scripts/bt_decrypt.py <加密文件.py> [输出文件.py]
```

## 加密原理

宝塔面板商业版对 Python 模块进行行级 AES-128-CBC 加密：

| 参数 | 值 |
|------|-----|
| 算法 | AES-128-CBC |
| 密钥 | `Z2B87NEAS2BkxTrh` (16B) |
| IV | `WwadH66EGWpeeTT6` (16B) |
| 编码 | Base64 |
| 填充 | PKCS7 |

密钥硬编码在 `PluginLoader.xxx.so` 的 `.text` 段中，`Ploader::_get_sgin_key()` 函数通过：
```python
v4 = [90,87,50,119,66,97,56,100,55,72,78,54,69,54,65,69,
      83,71,50,87,66,112,107,101,120,101,84,84,114,84,104,54]
key = v4[::2]   # 偶数位 = Z2B87NEAS2BkxTrh
iv  = v4[1::2]  # 奇数位 = WwadH66EGWpeeTT6
```

此密钥同时用于数据库密码加密和模块源码加密。

## 密钥更新

如宝塔更新密钥，使用 `scripts/extract_key.py` 从新版 `PluginLoader.so` 中提取：

```bash
python3 scripts/extract_key.py PluginLoader.xxx.so 加密文件样本.py
```

脚本会搜索 `.text` 段中 32 字节 ASCII 数组，拆分奇偶位为 key/IV 候选，然后用加密样本验证。

## 解密逻辑

`scripts/bt_decrypt.py` 的核心逻辑：

```python
KEY = b"Z2B87NEAS2BkxTrh"
IV  = b"WwadH66EGWpeeTT6"

for line in encrypted_lines:
    data = base64.b64decode(line)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    plaintext = cipher.decrypt(data)

    # PKCS7 去填充：pad_len 范围 1~16（含全填充 16）
    pad_len = plaintext[-1]
    if 0 < pad_len <= 16 and all(b == pad_len for b in plaintext[-pad_len:]):
        plaintext = plaintext[:-pad_len]

    output(plaintext.decode("utf-8") if plaintext else "")
```
