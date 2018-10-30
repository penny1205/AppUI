#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin

import os
import random
import datetime
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.db.dbutil import DBUtil
from BVT.common.company_project import CompanyProject
from BVT.common.company_cars import CompanyCars
from interface.wuliuyun.wayBill.saveWayBill import SaveWayBill
from interface.wuliuyun.wayBill.postTmsConfirmWayBill import PostTmsConfirmWayBill
from interface.wuliuyun.wayBill.postArriveConfirm import BillArriveConfirm
from interface.wuliuyun.wayBill.postShipperUploadReceipt import PostShipperUploadReceipt


class CreateWayBill(object):
    """ 创建运单公共方法 """

    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        # 订单号
        self.upWayBillId = ''
        # 用车日期
        self.date = datetime.date.today()
        # 项目信息
        projects_list = CompanyProject().get_project()
        project = random.choice(projects_list)
        self.projects_id = project['projectId']
        self.projects_name = project['projectName']
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
        self.mobile = self.config['chezhu_mobile']  # 联系电话
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
        self.totalAmt = '10000'  # 总金额
        self.preAmt = '1000'  # 预付款
        self.oilAmt = '1000'  # 油卡金额
        self.destAmt = '1000'  # 到付金额
        self.lastAmt = '1000'  # 尾款
        # 自定义费用
        self.oilCardDeposit = random.randint(0, 9999)  # 油卡押金
        self.handlingFee = random.randint(0, 9999)  # 装卸费
        self.deliveryFee = random.randint(0, 9999)  # 送货费
        self.otherFee = random.randint(0, 9999)  # 其他费用
        # 其他
        self.photoAirWay = FileUtil.getProjectObsPath() + os.sep + 'config' + os.sep + 'image' + os.sep + 'photoTransProt.png'  # 运输协议照片
        self.content = '自动化脚本录单'  # 运单备注
        self.partnerNo = self.config['partnerNo']  # 货主编号
        self.maker = self.config['partnerNo']  # 制单人

        # 公司车信息
        self.mobile_company = random.choice(CompanyCars().get_company_drivers_mobile())


    def select_waybill(self, mobile):
        db = DBUtil(host=self.config['db_host'], port=self.config['db_port'],
                    user=self.config['db_user'], passwd=self.config['db_passwd'],
                    dbname=self.config['db_dbname'], charset=self.config['db_charset'])
        sql = 'SELECT * from YD_APP_TRANSPORTCASH where mobile = \'{0}\' AND partnerNo = \'{1}\' AND billStatus = \'W\' AND delStatus = \'0\''.format(
            mobile, self.partnerNo)
        waybill = db.execute_select_one_record(sql)[0]
        return waybill

    def create_waybill(self):
        """ 录单 """
        # 录单字段更新至2017-12-22版本
        carType = '2'  # 用车类型 carType 1 公司车  2 外请车

            self.logger.info('###  创建外请车运单  ###')
            response = SaveWayBill().save_waybill(projectId=self.projects_id, projects=self.projects_name,
                                                  upWayBillId=self.upWayBillId, carType=carType,
                                                  applyDate=self.date, sendProvince=self.sendProvince,
                                                  sendCity=self.sendCity, sendDistrict=self.sendDistrict,
                                                  arriveProvince=self.arriveProvince,
                                                  arriveCity=self.arriveCity, arriveDistrict=self.arriveDistrict,
                                                  station=self.station, demandId='', receiptReceive=self.receiptReceive,
                                                  cargoName=self.cargoName, cargoWeight=self.cargoWeight,
                                                  cargoVolume=self.cargoVolume,
                                                  cargoNumberOfCases=self.cargoNumberOfCases,
                                                  cargoWorth=self.cargoWorth,
                                                  insuranceCosts=self.insuranceCosts, mobile=self.mobile,
                                                  accountName=self.accountName, driverCardBank=self.driverCardBank,
                                                  driverCardNo=self.driverCardNo,
                                                  vehicleIdNo=self.vehicleIdNo, supplierId=self.supplierId,
                                                  supplierName=self.supplierName, oilCardNo=self.oilCardNo,
                                                  hasReceipt=self.hasReceipt, realName=self.realName, idNo=self.idNo,
                                                  carNo=self.carNo, carModel=self.carModel, carLength=self.carLength,
                                                  income=self.income, totalAmt=self.totalAmt, preAmt=self.preAmt,
                                                  oilAmt=self.oilAmt, destAmt=self.destAmt, lastAmt=self.lastAmt,
                                                  oilCardDeposit=self.oilCardDeposit,
                                                  handlingFee=self.handlingFee, deliveryFee=self.deliveryFee,
                                                  otherFee=self.otherFee,
                                                  source='APP', photoAirWay=self.photoAirWay, content=self.content)
            return response
        else:
            self.logger.error('###  创建运单失败：carType error!  ###')
            return None

    def saveWayBill(self, carType):
        # 创建运单 处理手机号有未发车运单的情况
        if carType == '1':
            mobile = self.mobile_company
        elif carType == '2':
            mobile = self.mobile

        response = self.create_waybill(carType)
        if response.json()['code'] == 0:
            # billId = response.json()['content']['billId']
            return response
        else:
            self.logger.info('创建运单失败{0}'.format(response.json()))
            waybillId = self.select_waybill(mobile)
            self.logger.info('查找该司机未确认发车的运单，并进行确认发车操作')
            PostTmsConfirmWayBill().post_tmsconfirmwaybill(waybillId)
            response = self.create_waybill(carType)
            self.logger.info('确认发车返回结果：{0}'.format(response.json()))
            # billId = response.json()['content']['billId']
            return response

    def confirmWayBill(self):
        # 创建运单并确认发车
        waybillId = self.saveWayBill().json()['content']['billId']
        response = PostTmsConfirmWayBill().post_tmsconfirmwaybill(waybillId)
        self.logger.info('确认发车返回结果：{0}'.format(response.json()))
        return waybillId

    def arrive_confirm(self):
        # 对运单进行到达确认操作
        waybillId = self.confirmWayBill()
        response = BillArriveConfirm().bill_arriveconfirm(waybillId)
        self.logger.info('到达确认返回结果：{0}'.format(response.json()))
        return waybillId

    def upload_receipt(self):
        # 对运单进行回单上传操作
        waybillId = self.arrive_confirm()
        receipt0 = FileUtil.getProjectObsPath() + os.sep + 'config' + os.sep + 'image' + os.sep + 'receipt0.png'
        abnormal = 'Y'  # 是否有异常 Y：是、N：是
        damaged = 'Y'  # 是否有破损 Y：是、N：是
        losted = 'Y'  # 是否丢失 Y：是、N：是
        memo = '自动化测试--回单上传'  # 备注
        response = PostShipperUploadReceipt().post_shipper_upload_receipt(waybillId=waybillId, abnormal=abnormal,
                                                                          damaged=damaged, losted=losted, memo=memo,
                                                                          receipt0=receipt0)
        self.logger.info('回单上传返回结果： {0}'.format(response.json()))
        return waybillId


if __name__ == '__main__':
    test = CreateWayBill().saveWayBill(carType='1')
    print(test)
