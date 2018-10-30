#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin

import os
from util.log.log import Log


class PhotoFileFormat(object):
    # 格式化图片文件
    def __init__(self):
        self.logger = Log()

    def format_photo(self, photopath):
        # 根据图片路径返回post请求需要的表单格式
        if photopath != '':  # 需传递图片绝对路径
            if os.path.isfile(photopath):
                receipt_name = os.path.basename(photopath)
                with open(photopath, 'rb') as f:
                    receipt = (receipt_name, f.read())
            else:
                self.logger.info('### 图片路径不正确：{0} ###'.format(photopath))
                receipt = (None, '')
        else:
            receipt = (None, '')
        return receipt