#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from util.db.dbutil import DBUtil
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil


class DbOperation(object):
    def __init__(self):
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.db = DBUtil(host=self.config['Mysql_host'], port=self.config['Mysql_port'],
                         user=self.config['Mysql_user'], passwd=self.config['Mysql_passwd'],
                         dbname=self.config['Mysql_dbname'], charset=self.config['Mysql_charset'])

    def update(self, sql):
        self.db.execute_sql(sql)

    def select_driver_info(self, mobile):
        data_dict = {}
        sql = 'SELECT idNo,name,isCertifacate,pyAuthFlag,carNo,isCarCertificate from YD_APP_USER where mobile = \'{0}\' and source = \'register\''.format(
            mobile)
        data = self.db.execute_select_one_record(sql)
        data_dict['idNo'] = data[0]
        data_dict['name'] = data[1]
        data_dict['isCertifacate'] = data[2]
        data_dict['AuthFlag'] = data[3]
        data_dict['carNo'] = data[4]
        data_dict['isCarCertificate'] = data[5]
        return data_dict

    def initialize_driver_info(self, mobile):
        sql = 'UPDATE `YD_APP_USER` SET `carNo`=NULL, `idNo`=NULL, `name`=NULL, `portraitId`=NULL, `coreLoginId`=NULL,' \
              ' `custId`=\'0\', `isCarCertificate`=NULL, `isCardBindFlag`=NULL, `isCertifacate`=NULL, `portrait`=NULL,' \
              ' `pyAuthFlag`=NULL, `pyAuthResult`=NULL, `clientId`=NULL, `introducerPhone`=NULL WHERE (`mobile`=\'{0}\'' \
              ' and `source`=\'register\')'.format(mobile)
        self.db.execute_sql(sql)

    def update_driver_info(self):
        custId = self.config['custId_unregister']
        mobile = self.config['mobile_unregister']
        name = self.config['name_unregister']
        idNo = self.config['idNo_unregister']
        sql = 'UPDATE `YD_APP_USER` SET `carNo`=NULL, `idNo`={0}, `name`=\'{1}\', `portraitId`=NULL, `coreLoginId`={0},' \
              ' `custId`={2}, `isCarCertificate`=NULL, `isCardBindFlag`=NULL, `isCertifacate`=\'Y\', `portrait`=NULL,' \
              ' `pyAuthFlag`=\'0\', `pyAuthResult`=NULL, `clientId`=NULL, `introducerPhone`=NULL WHERE (`mobile`={3}' \
              ' and `source`=\'register\')'.format(idNo, name, custId, mobile)
        self.db.execute_sql(sql)

    def certificate_driver_info(self):
        custId = self.config['custId_unregister']
        mobile = self.config['mobile_unregister']
        name = self.config['name_unregister']
        idNo = self.config['idNo_unregister']
        sql = 'UPDATE `YD_APP_USER` SET `carNo`=\'皖A12345\', `idNo`={0}, `name`=\'{1}\', `portraitId`=NULL, `coreLoginId`={0},' \
              ' `custId`={2}, `isCarCertificate`=\'Y\', `isCardBindFlag`=NULL, `isCertifacate`=\'Y\', `portrait`=NULL,' \
              ' `pyAuthFlag`=\'0\', `pyAuthResult`=NULL, `clientId`=NULL, `introducerPhone`=NULL WHERE (`mobile`={3}' \
              ' and `source`=\'register\')'.format(idNo, name, custId, mobile)
        self.db.execute_sql(sql)

    def delete_wallet_driver(self):
        mobile = self.config['mobile_unregister']
        sql = 'UPDATE `YD_APP_MYBANK_OPEN_ACCOUNT` SET `accountOpened`=0 WHERE (`mobile`=\'{0}\' AND `accountOpened`=1);'.format(
            mobile)
        self.db.execute_sql(sql)

    def delete_waybill_driver(self, mobile):
        sql_select = 'SELECT id from YD_APP_TRANSPORTCASH where mobile = {0} and delStatus = 0'.format(mobile)
        waybill_list = self.db.execute_select_many_record(sql_select)
        for waybill_id in waybill_list:
            id = waybill_id[0]
            sql_del = 'UPDATE YD_APP_TRANSPORTCASH SET delStatus = 1 WHERE id = {0}'.format(id)
            self.db.execute_sql(sql_del)

    def select_waybill_state(self, mobile):
        sql_select = 'SELECT billStatus from YD_APP_TRANSPORTCASH where mobile = {0} and delStatus = 0'.format(mobile)
        state = self.db.execute_select_one_record(sql_select)
        return state

    def add_wallet_consignor(self, mobile):
        sql_select = 'SELECT loginId from YD_APP_USER where mobile = {0} and source = \'register\''.format(mobile)
        loginId = self.db.execute_select_one_record(sql_select)[0]
        sql_consignor = 'SELECT id FROM YD_APP_PAYMENT_RECEIVER WHERE loginId = \'{}\' ORDER BY id DESC LIMIT 1'.format(
            loginId)
        consignor_id = self.db.execute_select_one_record(sql_consignor)
        if consignor_id:
            sql_update = 'UPDATE YD_APP_PAYMENT_RECEIVER SET isAvailable = 1 , isDelete = 0 WHERE id = {0}'.format(
                consignor_id[0])
            self.db.execute_sql(sql_update)
        else:
            sql_insert = 'INSERT INTO YD_APP_PAYMENT_RECEIVER (`createDate`, `isOpenPayMent`, `loginId`, `receiverId`, ' \
                         '`receiverIdNo`, `receiverMobile`, `receiverName`, `receiverRelation`, `updateDate`, `comfirm`, ' \
                         '`isAvailable`, `receiverLoginId`, `isDelete`) VALUES (\'2018-11-01 15:16:18\', NULL, \'{0}\', ' \
                         'NULL, \'320621199210280523\', \'18020329066\', \'王燕\', \'其它\', NULL, 1, 1, ' \
                         '\'APP20170418150043iFVLP\', \'0\')'.format(loginId)
            self.db.execute_insert_sql(sql_insert)

    def delete_wallet_consignor(self, mobile):
        sql_select = 'SELECT loginId from YD_APP_USER where mobile = {0} and source = \'register\''.format(mobile)
        loginId = self.db.execute_select_one_record(sql_select)[0]
        sql_consignor = 'SELECT id from YD_APP_PAYMENT_RECEIVER where loginId = \'{0}\' and isAvailable = 1 and isDelete = 0'.format(
            loginId)
        consignor_list = self.db.execute_select_many_record(sql_consignor)
        for id in consignor_list:
            sql_delete = 'UPDATE YD_APP_PAYMENT_RECEIVER SET isAvailable = 0,isDelete = 1 WHERE id = {0}'.format(id[0])
            self.db.execute_sql(sql_delete)


if __name__ == '__main__':
    user = DbOperation().insert_wallet_consignor(18655148783)
