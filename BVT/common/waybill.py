#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import re
from util.db.dbutil import DBUtil
from util.http.httpclient import HttpClient
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class WaybillOperation(object):
    def __init__(self):
        self.log = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()

    def del_waybill(self, waybill_no='', waybill_state=''):
        db_host = self.config['Mysql_host']
        db_port = self.config['Mysql_port']
        db_name = self.config['Mysql_dbname']
        db_user = self.config['Mysql_user']
        db_pwd = self.config['Mysql_pwd']
        partner_no = self.config['partnerNo']
        db = DBUtil(host=db_host, port=db_port, user=db_user, passwd=db_pwd, dbname=db_name, charset='utf8')
        if waybill_no:
            sql = 'UPDATE YD_APP_TRANSPORTCASH SET delStatus = \'1\' WHERE id = {0} '.format(waybill_no)
            db.execute_sql(sql)
        else:
            sql = 'SELECT id from YD_APP_TRANSPORTCASH where partnerNo = \'{0}\' AND transStatus = \'{1}\' ' \
                  'AND delStatus = \'0\''.format(partner_no, waybill_state)  # D 待发车  E 运输中  A 已到达  C已完成
            waybill_data = db.execute_select_many_record(sql)
            self.log.info('Waybill select result:' + str(waybill_data))
            waybill_list = re.findall("\d+", str(waybill_data))
            for waybillNo in waybill_list:
                sql = 'UPDATE YD_APP_TRANSPORTCASH SET delStatus = \'1\' WHERE id = {0} '.format(waybillNo)
                db.execute_sql(sql)

    def create_waybill(self, projectId='', projects='', upWayBillId='', carType='', applyDate='', sendProvince='',
                       sendCity='', sendDistrict='', arriveProvince='', arriveCity='', arriveDistrict='', station='',
                       receiptReceive='', cargoName='', cargoWeight='', cargoVolume='', cargoNumberOfCases='',
                       cargoWorth='', insuranceCosts='', mobile='', accountName='', driverCardBank='', driverCardNo='',
                       vehicleIdNo='', supplierId='', supplierName='', oilCardNo='', hasReceipt='', realName='',
                       idNo='', carNo='', carLength='', carModel='', income='', totalAmt='', preAmt='', oilAmt='',
                       destAmt='', lastAmt='', oilCardDeposit='', handlingFee='', deliveryFee='', otherFee='',
                       source='APP', content='UI自动化录单', partnerNo='jUTViKluU', maker='18056070690'):
        self.log.info('#####  {0}  #####'.format(__name__))
        _apiUrl = '{0}{1}/payment/saveWayBill'.format(
            self.config['app_api_host'], self.config['app_api_path'])
        _head_dict = {
            'YD_OAUTH': self.config['app_api_YD_OAUTH']
        }
        photoAirWay = (None, '')
        try:
            files = {
                # 基本信息
                "projectId": (None, str(projectId)),  # 项目ID
                "projects": (None, str(projects)),  # 项目名称
                "upWayBillId": (None, str(upWayBillId)),  # 订单号
                "carType": (None, str(carType)),  # 用车性质 1公司车 2外请车
                "applyDate": (None, str(applyDate)),  # 用车日期
                "sendProvince": (None, str(sendProvince)),  # 发货省份
                "sendCity": (None, str(sendCity)),  # 发货城市
                "sendDistrict": (None, str(sendDistrict)),  # 发货区县
                "arriveProvince": (None, str(arriveProvince)),  # 到达省份
                "arriveCity": (None, str(arriveCity)),  # 到达城市
                "arriveDistrict": (None, str(arriveDistrict)),  # 到达区县
                "station": (None, str(station)),  # 途径地 [{ "province":"",# 省份"city":"",# 城市"district":""# 区县},......]
                "receiptReceive": (None, str(receiptReceive)),
                # 回单信息[{ "receiver":"",# 回单接收人"mobile":""# 联系电话,"province":""# 省份,"city":"",# 城市,"district":"",# 区县,"addressDetail":""# 详细地址}]

                # 货物信息
                "cargoName": (None, str(cargoName)),  # 货物名称
                "cargoWeight": (None, str(cargoWeight)),  # 货物重量
                "cargoVolume": (None, str(cargoVolume)),  # 货物体积
                "cargoNumberOfCases": (None, str(cargoNumberOfCases)),  # 货物件数
                "cargoWorth": (None, str(cargoWorth)),  # 货物价值
                "insuranceCosts": (None, str(insuranceCosts)),  # 货物投保费用

                # 承运信息
                "mobile": (None, str(mobile)),  # 联系电话
                "accountName": (None, str(accountName)),  # 账户名
                "driverCardBank": (None, str(driverCardBank)),  # 司机账户开户行
                "driverCardNo": (None, str(driverCardNo)),  # 司机银行卡号
                "vehicleIdNo": (None, str(vehicleIdNo)),  # 车架号
                "supplierId": (None, str(supplierId)),  # 供应商ID
                "supplierName": (None, str(supplierName)),  # 供应商名称
                "oilCardNo": (None, str(oilCardNo)),  # 油卡卡号
                "hasReceipt": (None, str(hasReceipt)),  # 是否有回单 1有 0没有
                "realName": (None, str(realName)),  # 司机姓名
                "idNo": (None, str(idNo)),  # 司机身份证号
                "carNo": (None, str(carNo)),  # 车牌号
                "carLength": (None, str(carLength)),  # 车长
                "carModel": (None, str(carModel)),  # 车型

                # 运费信息
                "income": (None, str(income)),  # 发车收入
                "totalAmt": (None, str(totalAmt)),  # 总金额
                "preAmt": (None, str(preAmt)),  # 预付款
                "oilAmt": (None, str(oilAmt)),  # 油卡金额
                "destAmt": (None, str(destAmt)),  # 到付金额
                "lastAmt": (None, str(lastAmt)),  # 尾款

                # 自定义费用
                "oilCardDeposit": (None, str(oilCardDeposit)),  # 油卡押金
                "handlingFee": (None, str(handlingFee)),  # 装卸费
                "deliveryFee": (None, str(deliveryFee)),  # 送货费
                "otherFee": (None, str(otherFee)),  # 其他费用

                # 其他
                "source": (None, str(source)),  # 来源 (TMS/APP)
                "photoAirWay": photoAirWay,  # 运输协议照片
                "content": (None, str(content)),  # 运单备注
                "partnerNo": (None, str(partnerNo)),  # 货主编号
                "maker": (None, str(maker))  # 制单人
            }  # 发送请求
            response = HttpClient().post_multipart(_apiUrl, files=files, header_dict=_head_dict)
            self.log.info('#####  请求消息头：{0}  #####'.format(response.request.headers))
            self.log.info('#####  请求消息体：{0}  #####'.format(response.request.body))
            return response
        except Exception as error:
            self.log.error('####  发生错误：{0}  ####\t\t####  返回None  ####'.format(error))
            return None

    def confirmWayBill(self, billId):
        # 创建运单并确认发车
        self.log.info('#####  {0}  #####'.format(__name__))
        _apiUrl = '{0}{1}/payment/tmsConfirmWayBill'.format(
            self.config['app_api_host'], self.config['app_api_path'])
        _head_dict = {
            'YD_OAUTH': self.config['app_api_YD_OAUTH']
        }
        body_dict = {
            'billId': billId  # 运单ID
        }
        try:
            response = HttpClient().post_json(_apiUrl, header_dict=_head_dict, body_dict=body_dict)
            self.logger.info('确认发车返回结果：{0}'.format(response.json()))
            return billId
        except Exception as error:
            self.log.error('####  发生错误：{0}  ####\t\t####  返回None  ####'.format(error))
            return None

    def arrive_confirm(self):
        # 对运单进行到达确认操作
        billId = self.create_waybill().json()['content']['billId']
        self.log.info('#####  {0}  #####'.format(__name__))
        _apiUrl = '{0}{1}/payment/confirmWayComplete'.format(
            self.config['app_api_host'], self.config['app_api_path'])
        _head_dict = {
            'YD_OAUTH': self.config['app_api_YD_OAUTH']
        }
        body_dict = {
            'billId': billId  # 运单ID
        }
        response = BillArriveConfirm().bill_arriveconfirm(waybillId)
        self.logger.info('到达确认返回结果：{0}'.format(response.json()))
        return waybillId

    def upload_receipt(self, carType):
        # 对运单进行回单上传操作
        waybillId = self.arrive_confirm(carType)
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
    WaybillOperation().del_waybill(waybill_state='A')
