#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:13:38 2018

@author: tuffy
"""
import time
from pandas import read_excel
from file_path import user_keys_excel
from sys_config import path, webdriver
from single_acc_lib import delete_first_app, create_or_get_keys
from check_login_status import convert_to_dictionary, login
### LOGGING ###
import coloredlogs,logging
coloredlogs.install()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# logger.propagate = False
### LOGGING ####
credential_dict = convert_to_dictionary()
# print(credential_dict)
# print(len(credential_dict))

def create_apps_save_keys():
    app_name_index = 0
    counter = 0
    for username in credential_dict.keys():
        driver = webdriver.Chrome(executable_path = path)
        while(True):  ### MIGHT NEED CHANGE
            counter += 1 
            if(login(driver, username, credential_dict[username])):
                break
            if counter > 10:
                print("Unable to access even after 10 attempts, breaking, please check credentials_dict for username",username,'or check your internet access')
                return 
        create_or_get_keys(driver, "trial__" + str(app_name_index), username, user_keys_excel)
        app_name_index += 1

def delete_multiple_apps():
    df = read_excel(user_keys_excel)
    for username in df.username:
    # for username in credential_dict.keys():
        driver = webdriver.Chrome(executable_path = path)
        try:
            while(True):
                if(login(driver, username, credential_dict[username])):
                    break
            delete_first_app(driver, username)
        except:
            print("not found")
        driver.close()


def login_and_wait():
    """
    Note: Login is done on only those credentials whose access details are there.
    """
    df = read_excel(user_keys_excel)
    # for username in credential_dict.keys():
    for username in df.username:
        driver = webdriver.Chrome(executable_path = path)
        login(driver, username, credential_dict[username])
    time.sleep(30)

###### FUNCTION CALLING
# print(credential_dict)
# delete_multiple_apps()
create_apps_save_keys()
# login_and_wait()
# collect_keys_multiple_apps()
