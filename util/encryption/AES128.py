#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin

import re
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES


class AES128(object):
    def __init__(self):
        self.BS = 16
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt_aes(self, AES_key, value):
        text = json.dumps(value)
        cryptor = AES.new(AES_key, AES.MODE_ECB)
        text = self.pad(text)
        ciphertext = cryptor.encrypt(text)
        return b64encode(ciphertext)

    def decrypt_aes(self, AES_key, value):
        missing_padding = 4 - len(value) % 4
        if missing_padding:
            value += b'=' * missing_padding
        text = b64decode(value)
        cryptor = AES.new(AES_key, AES.MODE_ECB)
        ciphertext = cryptor.decrypt(text)
        ciphertext = str(ciphertext, encoding="utf-8")
        ciphertext = re.findall('.*}', ciphertext)[0]
        ciphertext = json.loads(ciphertext)
        return ciphertext


if __name__ == '__main__':
    AES_key = '4B30DF18DD64913DCD6F60224B63A90F'
    value = {
	"contacts":
        [
            {
                "p":
                    [
                        "12345678901",
                        "12345678902"
                    ],
                "n": "张三"
            },
            {
                "p":
                    [
                        "12345678903",
                        "12345678904"
                    ],
                "n": "李四"
            }
        ],

	"messages":
        [
            {
                "c": "验证码：1234【中国银行】",
                "p": "12345678905",
                "t": "1516082700"
            },
            {
                "c": "验证码：123456【支付宝】",
                "p": "12345678906",
                "t": "1516082701"
            }
        ],

	"apps":
        [
            {
                "a": "wechat",
                "p": "com.tencent.cn"
            },
            {
                "a": "qq",
                "p": "com.tencent.cn"
            },
            {
                "a": "taobao",
                "p": "com.alibaba"
            }
        ],

	"calls":
        [
            {
                "p": "12345678907",
                "d": "60",
                "t": "1516082702"
            },
            {
                "p": "12345678908",
                "d": "60",
                "t": "1516082703"
            }
        ]
}
    pwd = AES128().encrypt_aes(AES_key, value)
    print(pwd)
    # pwd = b'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'
    # pwd = AES128().decrypt_aes(AES_key, pwd)
    # print(pwd)
