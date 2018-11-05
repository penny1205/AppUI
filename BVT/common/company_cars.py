#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
import os
from util.log.log import Log
from util.config.yaml.readyaml import ReadYaml
from util.file.fileutil import FileUtil
from util.http.headerdict import HeaderDict
from util.http.httpclient import HttpClient


class CompanyCars(object):
    def __init__(self):
        self.logger = Log()
        self.config = ReadYaml(FileUtil.getProjectObsPath() + '/config/config.yaml').getValue()
        self.partnerNo = self.config['partnerNo']

    def get_company_cars(self):
        cars = self.select_cars()
        if cars:
            return cars
        else:
            self.add_cars()
            new_cars = self.select_cars()
            return new_cars

    def get_company_drivers_mobile(self):
        drivers = self.select_driver()
        if drivers:
            drivers_list = drivers
        else:
            self.add_company_driver()
            new_drivers = self.select_driver()
            drivers_list = new_drivers
        company_drivers = []
        for driver in drivers_list:
            company_drivers.append(driver['mobile'])
        return company_drivers

    def select_cars(self):
        cars_list = GetCarList().get_carlist().json()['content']['dataList']
        return cars_list

    def select_driver(self):
        header = HeaderDict().wuliuyun_header()
        url_select_driver = 'https://{0}/api/tms/driver/listDrivers'.format(self.config['tms_api_host'])
        param_dict = {
            'currentPage': 1,
            'rows': 10
        }
        try:
            response = HttpClient().get(url=url_select_driver, header_dict=header, param_dict=param_dict)
            self.logger.info('#####  请求header：{0}  #####'.format(response.request.headers))
            self.logger.info('#####  请求body：{0}  #####'.format(response.request.body))
            self.logger.info('#####  请求body：{0}  #####'.format(response.json()))
            driver_list = response.json()['content']['dataList']
            return driver_list
        except Exception as error:
            self.logger.info('####  发生错误：{0}  ####\t\t####  返回None  ####'.format(error))
            return None

    def add_cars(self):
        header = HeaderDict().wuliuyun_header()
        url_add_cars = 'https://{0}/api/tms/car/createCar'.format(self.config['tms_api_host'])
        # photos = self.upload_photo()
        body_dict = {
            "carNo": self.config['CompanyCarNo'],  # 车牌号
            "carModel": self.config['CompanyCarModel'],  # 车型
            "carLength": self.config['CompanyCarLength'],  # 车长
            "carLoad": 8,  # 装载吨位
            "carAge": '',  # 车龄
            "photoDriverCard": '',  # 行驶证照片
            "photoCar": '',  # 车辆照片
            "buycarTime": '',  # 购车时间
            "carBrand": '',  # 车辆品牌,
            "partnerNo": self.config['partnerNo'],  # 物流公司标示,
            "accesCarMobile": ''  # 随车电话
        }
        try:
            response = HttpClient().post_json(url=url_add_cars, header_dict=header, body_dict=body_dict)
            self.logger.info('#####  请求header：{0}  #####'.format(response.request.headers))
            self.logger.info('#####  请求body：{0}  #####'.format(response.request.body))
            self.logger.info('#####  请求body：{0}  #####'.format(response.json()))
            return response
        except Exception as error:
            self.logger.info('####  发生错误：{0}  ####\t\t####  返回None  ####'.format(error))
            return None

    def add_company_driver(self):
        header = HeaderDict().wuliuyun_header()
        url_add_driver = 'https://{0}/api/tms/driver/createDriver'.format(self.config['tms_api_host'])
        body_dict = {
            'name': "测试",
            'mobile': self.config['CompanyDriver'],
            'partnerNo': self.config['partnerNo'],
            'backIdCard': "",
            'frontIdCard': "",
            'idNo': "",
            'photoDriverCard': ""
        }
        try:
            response = HttpClient().post_json(url=url_add_driver, header_dict=header, body_dict=body_dict)
            self.logger.info('#####  请求header：{0}  #####'.format(response.request.headers))
            self.logger.info('#####  请求body：{0}  #####'.format(response.request.body))
            self.logger.info('#####  请求body：{0}  #####'.format(response.json()))
            return response
        except Exception as error:
            self.logger.info('####  发生错误：{0}  ####\t\t####  返回None  ####'.format(error))
            return None

    # def upload_photo(self):
    #     file1 = FileUtil.getProjectObsPath() + os.sep + 'config' + os.sep + 'image' + os.sep + 'receipt0.png'
    #     file2 = FileUtil.getProjectObsPath() + os.sep + 'config' + os.sep + 'image' + os.sep + 'photoReceipt0.png'
    #     photo = PostUploadFile().post_upload_file(file1=file1, file2=file2).json()['content']
    #     photo_dict = {'photoDriverCard': photo[0]['bigImgRtnPath'],
    #                   'photoCar': photo[1]['bigImgRtnPath']}
    #     return photo_dict


if __name__ == '__main__':
    response = CompanyCars().add_cars()
    print(response.json())
