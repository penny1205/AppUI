#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin

import datetime
import random
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.db.dbutil import DBUtil
from util.http.headerdict import HeaderDict
from util.http.httpclient import HttpClient
from interface.wuliuyun.wayBill.getProjectsList import GetProjectsList


class CompanyProject(object):
    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.db = DBUtil(host=self.config['Mysql_host'], port=self.config['Mysql_port'],
                         user=self.config['Mysql_user'], passwd=self.config['Mysql_passwd'],
                         dbname=self.config['Mysql_dbname'], charset=self.config['Mysql_charset'])
        self.today = str(datetime.date.today())
        self.endDate = str(datetime.date.today() + datetime.timedelta(days=1))
        self.partnerNo = self.config['partnerNo']

    def select_project(self):
        sql = 'SELECT projectId FROM YD_TMS_PROJECT where partnerNo = \'{0}\' '.format(self.config['partnerNo'])
        projects_list = self.db.execute_select_many_record(sql)
        return projects_list

    def add_project(self):
        header = HeaderDict().wuliuyun_header()
        url = 'https://{0}/api/tms/customer/addProject'.format(self.config['tms_api_host'])
        body_dict = {
            "projectName": "自动化测试",  # 项目名称，必填，长度大于0不超过20的字符串，唯一性校验：一个公司下的项目名唯一
            "custId": '',  # 客户ID，非必填
            "startTime": self.today,  # 开始日期，必填，格式：'yyyy-MM-dd'
            "endTime": self.endDate  # 结束日期，必填，格式：'yyyy-MM-dd'
        }
        try:
            response = HttpClient().post_json(url=url, header_dict=header, body_dict=body_dict)
            self.logger.info('#####  请求消息头：{0}  #####'.format(response.request.headers))
            self.logger.info('#####  请求消息体：{0}  #####'.format(response.request.body))
            self.logger.info('#####  返回消息体：{0}  #####'.format(response.json()))
            return response
        except Exception as error:
            self.logger.info('####  发生错误：{0}  ####\t\t####  返回None  ####'.format(error))
            return None

    def get_project(self):
        projects_list = self.select_project()
        if projects_list:
            projects = []
            for project in projects_list:
                projects.append(project[0])
            # 更新项目有效时间，使项目生效，返回生效项目列表
            project_id = random.choice(projects)
            sql = 'UPDATE YD_TMS_PROJECT set endTime=\'{0}\'  where partnerNo = \'{1}\' and projectId = \'{2}\''.format(
                self.endDate, self.config['partnerNo'], project_id)
            self.db.execute_sql(sql)
            the_projects = GetProjectsList().get_projectlist().json()['content']['dataList']
            return the_projects
        else:
            self.add_project()
            the_projects = GetProjectsList().get_projectlist().json()['content']['dataList']
            return the_projects


if __name__ == '__main__':
    project = CompanyProject().add_project()
    print(project)
    # projects = []
    # for key in project:
    #     projects.append(key[0])
    # print(projects)
