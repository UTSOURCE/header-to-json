# -*- coding: utf-8 -*-
import json

# 自己把header复制这
headers = """
appVersion: 7.9.0
language: zh-Hans-CN
Content-Type: application/json;charset=utf-8
"""

headers = headers.strip().split('\n')
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
print(json.dumps(headers, indent=1))