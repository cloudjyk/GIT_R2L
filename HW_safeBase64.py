#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
def safe_base64_decode(s):
    # if not len(s)%4:
    #     return base64.b64decode(s)
    # else:
    #     while len(s)%4:
    #         s=s+b'='
    #     return base64.b64decode(s)
    return base64.b64decode(s+b'='*(4-len(s)%4))
if __name__=='__main__':
    print(safe_base64_decode(b'YWJjZA=='))
    assert b'abcd' == safe_base64_decode(b'YWJjZA==')
    print(safe_base64_decode(b'YWJjZA'))
    assert b'abcd' == safe_base64_decode(b'YWJjZA')