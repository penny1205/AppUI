#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.log.log import Log
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from BVT.common.db_operation import DbOperation
from BVT.common.createWayBill import CreateWayBill


class PayForDriver(object):
    def __init__(self, mobile):
        self.mobile = mobile
        self.waybill = CreateWayBill(self.mobile, totalAmt='1', preAmt='1', oilAmt='0', destAmt='0', lastAmt='0')
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        # URL ##
        self.url_pay_waybill = 'https://hfuapi.keking.cn:8887/api/tms/pay/single'
        self.head_dict = {
            'YD_VERSION': str(self.config['wuliuyun_version']),
            'YD_CLIENT': str(self.config['wuliuyun_client']),
            'YD_OAUTH': str(self.config['wuliuyun_token']),
            'token': str(self.config['wuliuyun_token']),
            'User-Agent': str(self.config['User-Agent'])
        }
        self.shipper_wallet_pwd = self.config['wuliuyun_wallet_pwd']

    def pay_for_driver(self):
        self.logger.info('### 获取用户钱包余额信息 ###')
        balance = self.get_wallet_info()['availBalance']
        balance = float(balance)
        if balance != 0:
            self.logger.info('### 钱包余额为{}###'.format(str(balance)))
            return
        else:
            self.logger.info('### 用户余额为零，创建运单并进行余额支付 ###')
            waybillId = self.waybill.confirmWayBill()
            body_dict = {"wayBillId":  waybillId,  # 运单ID，String，必填
                         "paymentMethod": "2",  # 支付方式，int【贷款付商户=1】、【余额付司机=2】、【白条付司机=3】、【线下支付=4】
                         "amountType": "1",  # 预付款1，油卡2，到付款3，尾款4,9总运费
                         "amount": "1.00",  # 实际支付金额，double
                         "password": self.shipper_wallet_pwd,  # 使用线下支付时必填，其他不填；
                         "verifiCode": "",  # 可能会有，非必填
                         "actualPayee": ""  # 实际收款人loginId
                         }
            response = HttpClient().post_json(url=self.url_pay_waybill, header_dict=self.head_dict, body_dict=body_dict)
            DbOperation().delete_waybill_driver(self.mobile)
            return response

    def get_wallet_info(self):
        # 获取司机钱包信息  'cardBindFlag' 是否绑卡  'availBalance' 余额信息
        url_get_wallet = 'https://hfuapi.keking.cn:8015/app/mybank/myWallet'
        head_dict = {
            'YD_VERSION': str(self.config['chezhu_version']),
            'YD_CLIENT': str(self.config['chezhu_client']),
            'YD_OAUTH': str(self.config['driver_token_regiseter']),
            'User-Agent': str(self.config['User-Agent'])
        }
        response = HttpClient().get(url=url_get_wallet, header_dict=head_dict).json()['content']
        return response


if __name__ == '__main__':
    balance = PayForDriver('18655148783').get_wallet_info()['availBalance']
    balance = float(balance)
    if balance != 0:
        print(balance)
    else:
        print('wallet balance is 0')
