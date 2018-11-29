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

    def certificate_driver_info(self, mobile):
        custId = self.config['custId_unregister']
        name = self.config['name_unregister']
        idNo = self.config['idNo_unregister']
        sql = 'UPDATE `YD_APP_USER` SET `carNo`=\'皖A12345\', `idNo`={0}, `name`=\'{1}\', `portraitId`=NULL, `coreLoginId`={0},' \
              ' `custId`={2}, `isCarCertificate`=\'Y\', `isCardBindFlag`=NULL, `isCertifacate`=\'Y\', `portrait`=NULL,' \
              ' `pyAuthFlag`=\'0\', `pyAuthResult`=NULL, `clientId`=NULL, `introducerPhone`=NULL WHERE (`mobile`={3}' \
              ' and `source`=\'register\')'.format(idNo, name, custId, mobile)
        self.db.execute_sql(sql)

    def select_wallet_state(self, mobile):
        # 查询手机号已开通钱包个数
        sql_select = 'select COUNT(*) FROM YD_APP_MYBANK_OPEN_ACCOUNT where mobile = \'{0}\' and accountOpened = 1'.format(mobile)
        state = self.db.execute_select_one_record(sql_select)[0]
        return state

    def delete_wallet_driver(self, mobile):
        sql_select = 'SELECT id from YD_APP_MYBANK_OPEN_ACCOUNT where mobile =\'{0}\''.format(mobile)
        ids = self.db.execute_select_many_record(sql_select)
        print(ids)
        if ids:
            for id in ids:
                sql_del = 'DELETE FROM `YD_APP_MYBANK_OPEN_ACCOUNT` WHERE id=\'{0}\' '.format(id[0])
                self.db.execute_sql(sql_del)

    def delete_waybill_driver(self, mobile):
        sql_select = 'SELECT id from YD_APP_TRANSPORTCASH where mobile = {0} and delStatus = 0'.format(mobile)
        waybill_list = self.db.execute_select_many_record(sql_select)
        for waybill_id in waybill_list:
            id = waybill_id[0]
            sql_del = 'UPDATE YD_APP_TRANSPORTCASH SET delStatus = 1 WHERE id = {0}'.format(id)
            self.db.execute_sql(sql_del)

    def select_waybill_state(self, mobile):
        # 返回运单状态数组
        sql_select = 'SELECT billStatus from YD_APP_TRANSPORTCASH where mobile = {0} and delStatus = 0 and partnerNo = \'jUTViKluU\''.format(mobile)
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

    def update_wallet_card_state(self, mobile):
        sql_select = 'SELECT c.id from YD_APP_MYBANK_OPEN_ACCOUNT a LEFT JOIN YD_APP_USER b on a.loginId = b.loginId  LEFT JOIN YD_APP_MYBANK_BIND_CARD c on a.mybankId = c.mybankId where b.mobile = \'{}\' ORDER BY c.id DESC LIMIT 1'.format(mobile)
        card_id = self.db.execute_select_one_record(sql_select)[0]
        sql_update = 'UPDATE YD_APP_MYBANK_BIND_CARD SET ifBindCardSuccess = 1, isUsable = 1 WHERE id = {}'.format(card_id)
        self.db.execute_sql(sql_update)

    def shipper_bankcard_del(self, shipper_mobile):
        # 将用户已绑定银行卡设置为失效
        sql_select = 'SELECT a.id from YD_APP_SPECIAL_BANK_BIND a LEFT JOIN YD_APP_APPROVAL_USER b on a.loginId = b.loginId where b.mobile = \'{0}\''.format(shipper_mobile)
        bankcard_ids = self.db.execute_select_many_record(sql_select)
        if bankcard_ids:
            for card_id in bankcard_ids:
                sql_update = 'UPDATE YD_APP_SPECIAL_BANK_BIND SET  cardStatus=\'N\' WHERE (id=\'{0}\')'.format(card_id[0])
                self.db.execute_sql(sql_update)

    def shipper_bankcard_add(self, shipper_mobile):
        # 将用户之前绑定的第一张银行卡设置为生效
        sql_select = 'SELECT a.id from YD_APP_SPECIAL_BANK_BIND a LEFT JOIN YD_APP_APPROVAL_USER b on a.loginId = b.loginId where b.mobile = \'{0}\''.format(
            shipper_mobile)
        bankcard_ids = self.db.execute_select_many_record(sql_select)
        if bankcard_ids:
            sql_update = 'UPDATE YD_APP_SPECIAL_BANK_BIND SET  cardStatus=\'V\' WHERE (id=\'{0}\')'.format(bankcard_ids[0][0])
            self.db.execute_sql(sql_update)
        else:
            sql_insert = 'INSERT INTO YD_APP_SPECIAL_BANK_BIND (`acctName`, `bankCity`, `bankName`, `bankPrinc`, `cardName`, `cardNo`, `cardStatus`, `cardType`, `createTime`, `idNo`, `idType`, `loginId`, `logoUrl`, `mobile`, `orgCode`, `subbranchBankName`, `bank`) VALUES (\'刘新宇\', \'340100\', \'建设银行\', \'340000\', \'龙卡通\', \'6217001630031143297\', \'V\', \'借记卡\', \'2018-11-09 13:48:22\', \'142201199305027054\', \'01\', \'APPSHIPPER20180829100001MgiIm\', \'http://yudian.ufile.ucloud.com.cn/019bd30c-39bb-4680-a32c-1d8703f90136.jpg?UCloudPublicKey=ucloudtangshd@weifenf.com14355492830001993909323&Expires=&Signature=pPx9/MwLLhB80/JgqSS8UPOeIh8=\', \'18056070532\', \'01050000\', \'测试建设支行\', \'建设银行\')'
            self.db.execute_sql(sql_insert)

if __name__ == '__main__':
    state = DbOperation().delete_wallet_driver('18000001111')
    # print(state[0])
