from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from file_path import user_keys_excel
#
from bs4 import BeautifulSoup
# from check_login_status import login
### LOGGING ###
import coloredlogs,logging
coloredlogs.install()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# logger.propagate = False
### LOGGING ####


#Get the access tokens of the already created apps.
def get_keys_of_first_app(driver):
    driver.get('https://apps.twitter.com/')
    logger.info('fetching apps.twitter.com')
    elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    elem.click()
    driver.get(driver.current_url[:-4] + "keys")
    logger.info('converting current url to api url & parsing that page through BeautifulSoup')
    
    page = (driver.page_source)
    tokenSoup = BeautifulSoup(page,"html.parser")

    consumer_tokens = tokenSoup.select(".app-settings > .row > span")
    consumer_key = consumer_tokens[1].string
    consumer_secret = consumer_tokens[3].string

    logger.info("consumer_key:%s", consumer_key)
    logger.info("consumer_secret:%s", consumer_secret)
    
    try:
        logger.info('locating & clicking access token button')
        get_access = driver.find_element_by_name("op")
        get_access.click()
        time.sleep(2)
        driver.refresh()
    except:
        logger.warn("No access button found, must be already clicked")

    logger.info('parsing again')
    page = (driver.page_source)
    tokenSoup = BeautifulSoup(page,"html.parser")
    
    access_tokens = tokenSoup.select(".access > .row > span")
    access_token = access_tokens[1].string
    access_token_secret = access_tokens[3].string
    logger.info("access_token:%s", access_token)
    logger.info("access_token_secret:%s", access_token_secret)

    user_key_list = [consumer_key,consumer_secret,access_token,access_token_secret]
    logger.info('USER KEY LIST:%s',user_key_list)
    return user_key_list


def create_app(driver, app_name):
    driver.get('https://apps.twitter.com/')
    logger.info('fetched apps.twitter.com, starting process to create new app')
    New_app = driver.find_element_by_xpath("//a[@href ='/app/new']")
    New_app.send_keys(Keys.RETURN)

    name = driver.find_element_by_name("name")
    name.send_keys(app_name)
    name.send_keys(Keys.TAB)

    description = driver.switch_to_active_element()
    description.send_keys("Trying out the twitter APIs")
    description.send_keys(Keys.TAB)
    ## PROBABLY NEED TO RANDOMIZE DESCRIPTION & WEBSITE LINK SOMEHOW
    website = driver.switch_to_active_element()
    website.send_keys("https://www.google.com")
    time.sleep(1)

    website.send_keys(Keys.TAB)
    time.sleep(1)

    Oauth = driver.switch_to_active_element()
    Oauth.send_keys(Keys.TAB)
    time.sleep(1)

    URL = driver.switch_to_active_element()
    URL.send_keys(Keys.TAB)
    time.sleep(1)

    URL_Tab = driver.switch_to_active_element()
    URL_Tab.send_keys(Keys.TAB)
    time.sleep(1)

    Confirm = driver.switch_to_active_element()
    Confirm.send_keys(Keys.SPACE)
    Confirm.send_keys(Keys.TAB)
    time.sleep(1)

    link = driver.switch_to_active_element()
    link.send_keys(Keys.TAB)
    time.sleep(1)

    Create = driver.switch_to_active_element()
    Create.send_keys(Keys.RETURN)

def create_or_get_keys(driver, app_name, username, user_keys_excel):
    driver.get('https://apps.twitter.com/')
    logger.info('fetched apps.twitter.com')
    try:
        logger.info('trying fetch first app')
        elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    except:
        logger.warn("no app found creating new app")
        create_app(driver, app_name)
    try:
        logger.info('trying to put api details to user_keys.xlsx')
        put_to_excel(get_keys_of_first_app(driver), username, user_keys_excel)
    
    except Exception as e:
        logger.error("ERROR:%s in getting app credentials for %s", e, username)
      ### PHONE VERIFY
    driver.close()


def put_to_excel(user_key_list, username, user_keys_excel):
    user_keys_dataframe = pd.read_excel(user_keys_excel, sheet_name = "Sheet1")
    # print(user_keys_dataframe)
    logger.info('read user_keys_excel')
    try:
        logger.info("if %s found in user_keys_excel overwrite api credentials",username)
        index = int(user_keys_dataframe[user_keys_dataframe.username == username].index.to_native_types()[0])
        user_keys_dataframe.loc[index, 'consumer_key'] = user_key_list[0]
        user_keys_dataframe.loc[index, 'consumer_secret'] = user_key_list[1]
        user_keys_dataframe.loc[index, 'access_token'] = user_key_list[2]
        user_keys_dataframe.loc[index, 'access_token_secret'] = user_key_list[3]
        # print(user_keys_dataframe)
        logger.info('found and overwritten')
    except IndexError:
        logger.warn('%s not found, appending to user_keys_excel',username)
        user_keys_dataframe = user_keys_dataframe.append(pd.DataFrame([[username] + user_key_list], columns=['username','consumer_key','consumer_secret','access_token','access_token_secret']),ignore_index=True)
    except Exception as e:
        logger.error('error thrown: %s',e)
    try:
        logger.info('put data to user_keys_excel')
        user_keys_dataframe.to_excel(user_keys_excel)
        # print(user_keys_dataframe)
    except:
        logger.error('ERROR IN DF TO USER KEYS EXCEL')

def delete_first_app(driver, username):
    driver.get('https://apps.twitter.com/')
    logger.info('fetched apps.twitter.com')
    try:
        first_app = driver.find_element_by_css_selector("div.app-details > h2 > a")
        first_app.click()
        driver.get(driver.current_url[:-4] + "delete")
        delete_button = driver.find_element_by_name("op")
        time.sleep(4)
        delete_button.click()
        time.sleep(4)
        logger.info("App deleted")
        #Removing the username entry from the excel file.
        #This will remove multiple entries as well.
        delete_from_excel(username)
        ####### PROBABLY WILL WORK COMMENTED BELOW LINES
        # df = pd.read_excel(user_keys_excel, sheet_name = "Sheet1")
        # df = df[df.username != username]
        # df.to_excel(user_keys_excel)
    except:
        logger.error("Error: No app found, or error in excel deletion.")

def delete_from_excel(username):
    logger.info("deleting from excel")
    user_keys_dataframe = pd.read_excel(user_keys_excel, sheet_name = "Sheet1")
    user_keys_dataframe = user_keys_dataframe[user_keys_dataframe.username != username]
    user_keys_dataframe.to_excel(user_keys_excel)

#driver - webdriver.Chrome(executable_path = path)
# login(driver, username, password)
# delete_first_app(driver, username)
# create_app(driver, app_name = 'trial___1')
#put_to_excel(get_keys_of_first_app(driver), username, user_keys_excel)
# print(get_keys_of_first_app(driver))
# delete_from_excel('akansha009verma@gmail.com')
# create_or_get_keys(driver, app_name = "trail___1", login_excel = login_excel)

## PHONE VERIFY CODE
  # df = pd.read_excel(login_excel)
        # df_index = int(df[df.username == username].index.to_native_types()[0])
        # print(df_index)
        # df.loc[df_index]['issues'] = 'phone verify'
        # df.to_excel(login_excel)}
