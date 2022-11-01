

"""百度通用翻译接口"""
API_NAME = 'fanyi'
# 地址信息
uri_scheme = 'http'
endpoint = 'api.fanyi.baidu.com'
resource_path = '/api/trans/vip/translate'
url = uri_scheme + u'://' + endpoint + resource_path

# 保持不变的参数
_from = 'en'
_to = 'zh'

# 请求消息参数
req_param = {
    "q": "",  # 请求翻译 query, UTF-8
    "from": _from,  # 翻译源语言
    "to": _to,  # 翻译目标语言
    "appid": "",  # APP ID
    "salt": "",  # 随机数
    "sign": "",  # 签名，appid+q+salt+密钥 的MD5值
}

# 响应消息参数
res_param = {
    "from": _from,
    "to": _to,
    "trans_result": [
        {
            "src": "Hello World! This is 1st paragraph.",
            "dst": "你好，世界！这是第一段。"
        },
        {
            "src": "This is 2nd paragraph.",
            "dst": "这是第二段。"
        }
    ]
}

