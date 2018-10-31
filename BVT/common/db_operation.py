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
        sql = 'UPDATE `YD_APP_MYBANK_OPEN_ACCOUNT` SET `accountOpened`=0 WHERE (`mobile`=\'{0}\' AND `accountOpened`=1);'.format(mobile)
        self.db.execute_sql(sql)


if __name__ == '__main__':
    user = DbOperation().delete_wallet_driver()
