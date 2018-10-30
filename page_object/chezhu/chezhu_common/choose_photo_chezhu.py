#! /usr/bin/python3
# -*- coding:utf-8 -*-
# author: vin
from page_object.chezhu.chezhu import CheZhu
from util.driver.project_decorator import catch_exception


class ChoosePhotoCheZhu(CheZhu):
    # -*- VIVO -*-
    __vivo_photo_file = {'identifyBy': 'ids', 'path': ['com.vivo.gallery:id/dreamway_folder_info', 0]}
    __id_card_front = {'x': 0.625, 'y': 0.1875}
    __id_card_back = {'x': 0.361, 'y': 0.1875}
    __driving_license_front = {'x': 0.125, 'y': 0.1875}
    vivo_photo_page_1 = 'com.android.gallery3d.app.Gallery'
    vivo_photo_page_2 = 'com.android.gallery3d.vivo.NewPageActivity'

    @catch_exception
    def choose_id_card_front(self):
        self.driver.wait_activity(self.vivo_photo_page_1)
        self.driver.click_element(self.__vivo_photo_file)
        self.driver.wait_activity(self.vivo_photo_page_2)
        front_image_coordinate = [self.__id_card_front['x'], self.__id_card_front['y']]
        self.driver.click_by_coordinate([front_image_coordinate], duration=500)

    @catch_exception
    def choose_id_card_back(self):
        self.driver.wait_activity(self.vivo_photo_page_1)
        self.driver.click_element(self.__vivo_photo_file)
        self.driver.wait_activity(self.vivo_photo_page_2)
        front_image_coordinate = [self.__id_card_back['x'], self.__id_card_back['y']]
        self.driver.click_by_coordinate([front_image_coordinate], duration=500)

    @catch_exception
    def choose_driving_license_front(self):
        self.driver.wait_activity(self.vivo_photo_page_1)
        self.driver.click_element(self.__vivo_photo_file)
        self.driver.wait_activity(self.vivo_photo_page_2)
        front_image_coordinate = [self.__driving_license_front['x'], self.__driving_license_front['y']]
        self.driver.click_by_coordinate([front_image_coordinate], duration=500)

    @catch_exception
    def choose_image(self):
        self.driver.wait_activity(self.vivo_photo_page_1)
        self.driver.click_element(self.__vivo_photo_file)
        self.driver.wait_activity(self.vivo_photo_page_2)
        front_image_coordinate = [self.__driving_license_front['x'], self.__driving_license_front['y']]
        self.driver.click_by_coordinate([front_image_coordinate], duration=500)
