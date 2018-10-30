# __author__ = 'penny'
# -*- coding:utf-8 -*-

import pymysql
import redis
import re
from util.config.yaml.readyaml import ReadYaml
from util.log.log import Log
from util.file.fileutil import FileUtil


class DBUtil(object):
    """操作mysql数据库"""

    def __init__(self, host, port, user, passwd, dbname, charset):
        self.logger = Log()
        try:
            self.connect = pymysql.Connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=dbname,
                charset=charset
            )
        except Exception as e:
            self.logger.error('Database Initialization Connection Failed 1 : {0}'.format(e))
            raise

    def execute_sql(self, sql):
        """执行sql语句"""
        self.logger.info('sql:{0}'.format(sql))
        try:
            self.connect.ping(reconnect=True)  # 检查数据库连接，未连接时重试
            cur = self.connect.cursor()
            cur.execute(sql)
            cur.close()  # 关闭游标
            self.connect.commit()  # 提交事务
            # self.connect.close()  # 关闭连接
            return
        except Exception as e:
            self.logger.info('Execute sql failed ! : {0}'.format(e))
            self.connect.rollback()
            self.connect.close()
            raise

    def execute_select_one_record(self, query):
        """执行sql语句：select,返回结果只包含一条数据"""
        self.logger.info('query:{0}'.format(query))
        try:
            cur = self.connect.cursor()
            cur.execute(query)
            self.connect.close()
            return cur.fetchone()
        except Exception as e:
            self.logger.info('Execute sql failed ! : {0}'.format(e))
            self.connect.close()
            raise

    def execute_select_many_record(self, query):
        """执行sql语句：select，返回结果包含多条数据"""
        self.logger.info('query:{0}'.format(query))
        try:
            cur = self.connect.cursor()
            cur.execute(query)
            self.connect.close()
            return cur.fetchall()
        except Exception as e:
            self.logger.info('Execute sql failed ! : {0}'.format(e))
            self.connect.close()
            raise

    def execute_insert_sql(self, query):
        """执行sql语句：insert,返回插入数据的主键id"""
        self.logger.info('query:{0}'.format(query))
        try:
            conn = self.connect
            cur = self.connect.cursor()
            cur.execute(query)
            insert_id = conn.insert_id()
            conn.commit()
            self.connect.close()
            return insert_id
        except Exception as e:
            self.logger.info('Execute sql failed ! : {0}'.format(e))
            self.connect.close()
            raise


class RedisDb(object):
    """操作Redis数据库"""

    def __init__(self):
        self.logger = Log()
        config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.host = config['Redis_host']
        self.port = config['Redis_port']
        self.pwd = config['Redis_pwd']
        self.db = config['Redis_db']

    def get_code(self, name, key):
        self.logger.info('### Redis查询参数  name:{0};key:{1}  ###'.format(name, key))
        redis_db = redis.Redis(host=self.host, port=self.port, decode_responses=True, password=self.pwd, db=self.db)  # 连接Redis数据库
        code = redis_db.hget(name=name, key=key)  # 获取Hash类型数据
        return re.findall('\d+', code)[0]

    def get_key(self, name):
        redis_db = redis.Redis(host=self.host, port=self.port, decode_responses=True)
        txt = redis_db.hgetall(name)
        return txt

if __name__ == '__main__':
    test = RedisDb()
    code = test.get_code(name='AppLoginVerifyCode', key='"18056070690"')
    print(code)
    # code = test.get_key('YUDIAN-QUARTZ-JOB-TASK')
    # print(code)
    # host = '106.75.114.47'
    # test = DBUtil(host=host, port=23306, user='kk_hf2', passwd='keking456', dbname='YDAPPDB1',
    #               charset='utf8')
    # sql = 'SELECT id from YD_APP_TRANSPORTCASH where partnerNo = \'WeiBo\' AND transStatus = \'C\' AND delStatus = \'0\''
    # waybill = test.execute_select_many_record(sql)
    # print(waybill)
    # res = re.findall("\d+", str(waybill))
    # for i in res:
    #     print(i)
    #     sql = 'UPDATE YD_APP_TRANSPORTCASH SET delStatus = \'1\' WHERE id = {0} '.format(i)
    #     test.execute_sql(sql)
