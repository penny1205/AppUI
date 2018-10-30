#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin

from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class HeaderDict(object):
    # 配置接口请求head_dict内容
    def __init__(self):
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()

    def wuliuyun_header(self):
        # 凯京物流云APP请求head_dict内容
        head_dict = {
            'YD_VERSION': str(self.config['wuliuyun_version']),
            'YD_CLIENT': str(self.config['wuliuyun_client']),
            'YD_OAUTH': str(self.config['app_api_YD_OAUTH']),
            'User-Agent': str(self.config['User-Agent'])
        }
        return head_dict

    def special_line_header(self):
        # 企业专线贷用户请求head_dict内容
        head_dict = {
            'YD_VERSION': str(self.config['wuliuyun_version']),
            'YD_CLIENT': str(self.config['wuliuyun_client']),
            'YD_OAUTH': str(self.config['app_api_YD_OAUTH']),
            'User-Agent': str(self.config['User-Agent'])
        }
        return head_dict

    def chezhu_header(self):
        # 凯京车主APP请求head_dict内容
        head_dict = {
            'YD_VERSION': str(self.config['chezhu_version']),
            'YD_CLIENT': str(self.config['chezhu_client']),
            'YD_OAUTH': str(self.config['chezhu_token']),
            'User-Agent': str(self.config['User-Agent'])
        }
        return head_dict

    def register_header(self):
        # 凯京车主APP已认证用户head_dict
        head_dict = {
            'YD_VERSION': str(self.config['chezhu_version']),
            'YD_CLIENT': str(self.config['chezhu_client']),
            'YD_OAUTH': str(self.config['driver_register_token']),
            'User-Agent': str(self.config['User-Agent'])
        }
        return head_dict

if __name__ == '__main__':
    test = HeaderDict()
    print(test.wuliuyun_header())
    print(test.chezhu_header())
