#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin

import random
import datetime
import os
from util.log.log import Log
from util.http.httpclient import HttpClient
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.file.photofileFormat import PhotoFileFormat
from util.db.dbutil import DBUtil
from BVT.common.company_project import CompanyProject


class CreateWayBill(object):
    """ 创建运单公共方法 """

    def __init__(self, mobile, totalAmt='10000', preAmt='1000', oilAmt='1000', destAmt='1000', lastAmt='1000'):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        # URL ##
        self.url_create_waybill = 'https://hfuapi.keking.cn:8015/app/payment/saveWayBill'
        self.url_confirm_waybill = 'https://hfuapi.keking.cn:8015/app/payment/tmsConfirmWayBill'
        self.url_arrive_waybill = 'https://hfuapi.keking.cn:8015/app/payment/confirmWayComplete'
        self.url_upload_receipt = 'https://hfuapi.keking.cn:8015/app/shipper/uploadReceipt'
        self.head_dict = {
            'YD_VERSION': str(self.config['wuliuyun_version']),
            'YD_CLIENT': str(self.config['wuliuyun_client']),
            'YD_OAUTH': str(self.config['wuliuyun_token']),
            'User-Agent': str(self.config['User-Agent'])
        }
        # 录单信息 ##
        self.mobile = mobile
        # 订单号
        self.upWayBillId = ''
        # 用车日期
        self.date = datetime.date.today()
        # 项目信息
        projects_list = CompanyProject().get_project()
        self.projects_id = projects_list[0]
        self.projects_name = projects_list[1]
        # 出发地
        self.sendProvince = '北京'
        self.sendCity = '北京'
        self.sendDistrict = '海淀区'
        # 到达地
        self.arriveProvince = '安徽'
        self.arriveCity = '合肥'
        self.arriveDistrict = '蜀山区'
        # 途径地
        self.station = '[{\"province\":\"天津\",\"city\":\"天津\",\"district\":\"河西区\"},{\"province\":\"安徽\",\"city\":\"阜阳\",\"district\":\"阜南县\"}]'
        # 回单信息
        self.receiptReceive = ''
        # 货物信息
        self.cargoName = '快递'  # 货物名称
        self.cargoWeight = random.randint(1, 10)  # 货物重量
        self.cargoVolume = random.randint(1, 10)  # 货物体积
        self.cargoNumberOfCases = random.randint(1, 100)  # 货物件数
        self.cargoWorth = random.randint(1, 1000)  # 货物价值
        self.insuranceCosts = random.randint(1, 1000)  # 货物投保费用
        # 承运信息
        self.realName = '自动化测试'  # 司机姓名
        self.carNo = '皖A00000'
        self.idNo = '340100199001010101'  # 司机身份证号
        self.accountName = '自动化测试'  # 账户名
        self.driverCardBank = '自动化测试'  # 司机账户开户行
        self.driverCardNo = '0123456789012345'  # 司机银行卡号
        self.vehicleIdNo = '987654321012345'  # 车架号
        self.supplierId = ''  # 供应商ID
        self.supplierName = ''  # 供应商名称
        self.oilCardNo = 'abc123456'  # 油卡卡号
        self.hasReceipt = '1'  # 是否有回单 1有 0没有
        self.carLength = '7.6'  # 车长
        self.carModel = 'TE_ZHONG_CHE'  # 车型
        # 运费信息
        self.income = random.randint(0, 10000)  # 发车收入
        self.totalAmt = totalAmt  # 总金额
        self.preAmt = preAmt  # 预付款
        self.oilAmt = oilAmt  # 油卡金额
        self.destAmt = destAmt  # 到付金额
        self.lastAmt = lastAmt  # 尾款
        # 自定义费用
        self.oilCardDeposit = random.randint(0, 9999)  # 油卡押金
        self.handlingFee = random.randint(0, 9999)  # 装卸费
        self.deliveryFee = random.randint(0, 9999)  # 送货费
        self.otherFee = random.randint(0, 9999)  # 其他费用
        # 其他
        # self.photoAirWay = FileUtil.getProjectObsPath() + os.sep + 'config' + os.sep + 'image' + os.sep + 'photoTransProt.png'  # 运输协议照片
        self.content = 'UI自动化录单'  # 运单备注
        self.partnerNo = self.config['partnerNo']  # 货主编号
        self.maker = self.config['partnerNo']  # 制单人

        # 公司车信息
        # self.mobile_company = random.choice(CompanyCars().get_company_drivers_mobile())

    def select_waybill(self):
        # 查找待发车运单
        db = DBUtil(host=self.config['Mysql_host'], port=self.config['Mysql_port'],
                    user=self.config['Mysql_user'], passwd=self.config['Mysql_passwd'],
                    dbname=self.config['Mysql_dbname'], charset=self.config['Mysql_charset'])
        sql = 'SELECT * from YD_APP_TRANSPORTCASH where mobile = \'{0}\' AND partnerNo = \'{1}\' AND billStatus = \'W\' AND delStatus = 0'.format(
            self.mobile, self.partnerNo)
        waybill = db.execute_select_one_record(sql)
        if waybill:
            return waybill[0]

    def delete_waybill(self):
        # 删除待发车运单
        db = DBUtil(host=self.config['Mysql_host'], port=self.config['Mysql_port'],
                         user=self.config['Mysql_user'], passwd=self.config['Mysql_passwd'],
                         dbname=self.config['Mysql_dbname'], charset=self.config['Mysql_charset'])
        sql = 'UPDATE YD_APP_TRANSPORTCASH SET delStatus = 1 where mobile = \'{0}\' AND partnerNo = \'{1}\' AND billStatus = \'W\' AND delStatus = 0'.format(
            self.mobile, self.partnerNo)
        db.execute_sql(sql)

    def create_waybill(self):
        """ 录单 """
        # 录单字段更新至2017-12-22版本
        carType = '2'  # 用车类型 carType 1 公司车  2 外请车
        self.logger.info('###  创建外请车运单  ###')
        try:
            files = {
                # 基本信息
                "projectId": (None, str(self.projects_id)),  # 项目ID
                "projects": (None, str(self.projects_name)),  # 项目名称
                "upWayBillId": (None, str(self.upWayBillId)),  # 订单号
                "carType": (None, str(carType)),  # 用车性质 1公司车 2外请车
                "applyDate": (None, str(self.date)),  # 用车日期
                "sendProvince": (None, str(self.sendProvince)),  # 发货省份
                "sendCity": (None, str(self.sendCity)),  # 发货城市
                "sendDistrict": (None, str(self.sendDistrict)),  # 发货区县
                "arriveProvince": (None, str(self.arriveProvince)),  # 到达省份
                "arriveCity": (None, str(self.arriveCity)),  # 到达城市
                "arriveDistrict": (None, str(self.arriveDistrict)),  # 到达区县
                "station": (None, str(self.station)),
                # 途径地 [{ "province":"",# 省份"city":"",# 城市"district":""# 区县},......]
                "demandId": (None, ""),  # 运单需求ID
                "receiptReceive": (None, str(self.receiptReceive)),
                # 回单信息[{ "receiver":"",# 回单接收人"mobile":""# 联系电话,"province":""# 省份,"city":"",# 城市,"district":"",# 区县,"addressDetail":""# 详细地址}]

                # 货物信息
                "cargoName": (None, str(self.cargoName)),  # 货物名称
                "cargoWeight": (None, str(self.cargoWeight)),  # 货物重量
                "cargoVolume": (None, str(self.cargoVolume)),  # 货物体积
                "cargoNumberOfCases": (None, str(self.cargoNumberOfCases)),  # 货物件数
                "cargoWorth": (None, str(self.cargoWorth)),  # 货物价值
                "insuranceCosts": (None, str(self.insuranceCosts)),  # 货物投保费用

                # 承运信息
                "mobile": (None, str(self.mobile)),  # 联系电话
                "accountName": (None, str(self.accountName)),  # 账户名
                "driverCardBank": (None, str(self.driverCardBank)),  # 司机账户开户行
                "driverCardNo": (None, str(self.driverCardNo)),  # 司机银行卡号
                "vehicleIdNo": (None, str(self.vehicleIdNo)),  # 车架号
                "supplierId": (None, str(self.supplierId)),  # 供应商ID
                "supplierName": (None, str(self.supplierName)),  # 供应商名称
                "oilCardNo": (None, str(self.oilCardNo)),  # 油卡卡号
                "hasReceipt": (None, str(self.hasReceipt)),  # 是否有回单 1有 0没有
                "realName": (None, str(self.realName)),  # 司机姓名
                "idNo": (None, str(self.idNo)),  # 司机身份证号
                "carNo": (None, str(self.carNo)),  # 车牌号
                "carLength": (None, str(self.carLength)),  # 车长
                "carModel": (None, str(self.carModel)),  # 车型

                # 运费信息
                "income": (None, str(self.income)),  # 发车收入
                "totalAmt": (None, str(self.totalAmt)),  # 总金额
                "preAmt": (None, str(self.preAmt)),  # 预付款
                "oilAmt": (None, str(self.oilAmt)),  # 油卡金额
                "destAmt": (None, str(self.destAmt)),  # 到付金额
                "lastAmt": (None, str(self.lastAmt)),  # 尾款

                # 自定义费用
                "oilCardDeposit": (None, str(self.oilCardDeposit)),  # 油卡押金
                "handlingFee": (None, str(self.handlingFee)),  # 装卸费
                "deliveryFee": (None, str(self.deliveryFee)),  # 送货费
                "otherFee": (None, str(self.otherFee)),  # 其他费用

                # 其他
                "source": (None, "APP"),  # 来源 (TMS/APP)
                # "photoAirWay": "",  # 运输协议照片
                "content": (None, str(self.content)),  # 运单备注
                "partnerNo": (None, str(self.partnerNo)),  # 货主编号
                "maker": (None, str(self.maker))  # 制单人
            }

            # 发送请求
            response = HttpClient().post_multipart(self.url_create_waybill, files=files, header_dict=self.head_dict)
            return response
        except Exception:
            self.logger.error('###  创建运单失败：carType error!  ###')
            return None

    def saveWayBill(self):
        # 创建运单 处理手机号有未发车运单的情况
        response = self.create_waybill()
        if response.json()['code'] == 0:
            return response
        else:
            self.logger.info('创建运单失败{0}'.format(response.json()))
            self.logger.info('查找该司机未确认发车的运单，并进行删除操作')
            self.delete_waybill()
            response = self.create_waybill()
            self.logger.info('确认发车返回结果：{0}'.format(response.json()))
            return response

    def confirmWayBill(self):
        # 创建运单并确认发车
        waybillId = self.saveWayBill().json()['content']['billId']
        body_dict = {
            'billId': waybillId  # 运单ID
        }
        response = HttpClient().post_json(url=self.url_confirm_waybill, body_dict=body_dict, header_dict=self.head_dict)
        self.logger.info('确认发车返回结果：{0}'.format(response.json()))
        return waybillId

    def arrive_confirm(self):
        # 对运单进行到达确认操作
        waybillId = self.confirmWayBill()
        body_dict = {
            'billId': waybillId  # 运单ID
        }
        response = HttpClient().post_json(url=self.url_arrive_waybill, body_dict=body_dict, header_dict=self.head_dict)
        self.logger.info('到达确认返回结果：{0}'.format(response.json()))
        return waybillId

    def upload_receipt(self):
        # 对运单进行回单上传操作
        waybillId = self.arrive_confirm()
        waybillId = str(waybillId)
        abnormal = 'Y'  # 是否有异常 Y：是、N：是
        damaged = 'Y'  # 是否有破损 Y：是、N：是
        losted = 'Y'  # 是否丢失 Y：是、N：是
        memo = '自动化测试--回单上传'  # 备注
        receipt_img = FileUtil.getProjectObsPath() + os.sep+'config'+os.sep+'image'+os.sep+'receipt0.png'
        # receipt0 = PhotoFileFormat().format_photo(receipt_img)
        files = {
            "id": (None, waybillId),  # 运单id
            "abnormal": (None, abnormal),  # 是否有异常 Y：是、N：是
            "damaged": (None, damaged),  # 是否有破损 Y：是、N：是
            "losted": (None, losted),  # 是否丢失 Y：是、N：是
            "memo": (None, memo),  # 备注
            "type": (None, "S"),  # S：货主、C：司机
            "receipt_0": ("receipt.png", open(receipt_img, 'rb'), 'image/png')  # 回单图片文件
        }
        self.head_dict.pop('content-type')
        response = HttpClient().post_multipart(url=self.url_upload_receipt, header_dict=self.head_dict, files=files)
        self.logger.info('回单上传请求： {0}'.format(response.request.headers))
        self.logger.info('回单上传返回结果： {0}'.format(response.json()))
        # return waybillId


if __name__ == '__main__':
    test = CreateWayBill('18056070690').saveWayBill()
    print(test.json())
