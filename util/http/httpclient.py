# -*-coding:utf-8-*-
import requests
import json
import time
from util.http.sslAdapter import Ssl3Adapter
from util.log.log import Log


def try_requests(func):
    # 请求重试函数  失败后重试3次
    def new_request(*args, **kwargs):
        state = True
        number = 0
        while state and number < 3:
            try:
                return func(*args, **kwargs)
                state = False
            except requests.exceptions.ConnectionError as e:
                Log().info("Connection refused by the server..{0}".format(e))
                Log().info("Waiting for 3 seconds and try again...")
                time.sleep(3)
                number += 1
                continue
    return new_request


class HttpClient:
    """发送http请求"""

    def __init__(self, timeout=60):
        self.logger = Log()
        self.requests = requests
        self.timeout = timeout
        self.requests.session().mount('https://', Ssl3Adapter())

    @try_requests
    def get(self, url, header_dict=None, param_dict=None):
        response = requests.get(url, headers=header_dict, params=param_dict, timeout=self.timeout)
        return response

    @try_requests
    def post_form(self, url, body_dict=None, header_dict=None, param_dict=None):
        response = requests.post(url, data=body_dict, headers=header_dict, params=param_dict, timeout=self.timeout)
        return response

    @try_requests
    def post_json(self, url, body_dict=None, header_dict=None, param_dict=None):
        header_dict['content-type'] = 'application/json'
        if isinstance(body_dict, dict):
            response = requests.post(url, data=json.dumps(body_dict), headers=header_dict, params=param_dict,
                                     timeout=self.timeout)
        else:
            response = requests.post(url, data=body_dict, headers=header_dict, params=param_dict, timeout=self.timeout)
        return response

    @try_requests
    def post_multipart(self, url, files=None, header_dict=None):
        response = requests.post(url, files=files, headers=header_dict)
        return response

    @try_requests
    def post_multipart_file(self, url, file_path, header_dict=None):
        files = {'file': (open(file_path, 'rb'))}
        response = requests.post(url, files=files, headers=header_dict)
        return response

    @try_requests
    def put(self, url, body_dict=None, header_dict=None, param_dict=None):
        header_dict['content-type'] = 'application/json'
        response = requests.put(url, data=json.dumps(body_dict), headers=header_dict, params=param_dict,
                                timeout=self.timeout)
        return response


if __name__ == '__main__':
    response = HttpClient().post_form('', {'test': '123'})
    print(response.text)
