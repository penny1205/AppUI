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


if __name__ == '__main__':
    user = DbOperation().initialize_driver_info('18056070532')
