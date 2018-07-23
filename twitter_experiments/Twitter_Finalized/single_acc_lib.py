from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from file_path import user_keys_excel
#
from bs4 import BeautifulSoup
# from check_login_status import login


#Get the access tokens of the already created apps.
def get_keys_of_first_app(driver):
    driver.get('https://apps.twitter.com/')
    elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    elem.click()
    driver.get(driver.current_url[:-4] + "keys")
    page = (driver.page_source)

    tokenSoup = BeautifulSoup(page,"html.parser")

    consumer_tokens = tokenSoup.select(".app-settings > .row > span")
    consumer_key = consumer_tokens[1].string
    consumer_secret = consumer_tokens[3].string
    print("consumer_key:", consumer_key, "consumer_secret:", consumer_secret, sep = '\n')
    
    try:
        get_access = driver.find_element_by_name("op")
        get_access.click()
        time.sleep(2)
        driver.refresh()
    except:
        print("No access button found")

    page = (driver.page_source)
    tokenSoup = BeautifulSoup(page,"html.parser")
    
    access_tokens = tokenSoup.select(".access > .row > span")
    access_token = access_tokens[1].string
    access_token_secret = access_tokens[3].string
    print("access_token:", access_token, "access_token_secret:", access_token_secret, sep = '\n')

    user_key_list = [consumer_key,consumer_secret,access_token,access_token_secret]
    print('USER KEY LIST:',user_key_list)
    return user_key_list


def create_app(driver, app_name):
    driver.get('https://apps.twitter.com/')

    New_app = driver.find_element_by_xpath("//a[@href ='/app/new']")
    New_app.send_keys(Keys.RETURN)

    name = driver.find_element_by_name("name")
    name.send_keys(app_name)
    name.send_keys(Keys.TAB)

    description = driver.switch_to_active_element()
    description.send_keys("Trying out the twitter APIs")
    description.send_keys(Keys.TAB)

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
    try:
        elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
    except:
        create_app(driver, app_name)
    try:
        put_to_excel(get_keys_of_first_app(driver), username, user_keys_excel)
    
    except Exception as e:
        print("ERROR:",e,"in getting app credentials for", username)
      ### PHONE VERIFY
    driver.close()


def put_to_excel(user_key_list, username, user_keys_excel):
    df = pd.read_excel(user_keys_excel, sheet_name = "Sheet1")
    print(df)
    try:
        df_index = int(df[df.username == username].index.to_native_types()[0])
        df.loc[df_index, 'consumer_key'] = user_key_list[0]
        df.loc[df_index, 'consumer_secret'] = user_key_list[1]
        df.loc[df_index, 'access_token'] = user_key_list[2]
        df.loc[df_index, 'access_token_secret'] = user_key_list[3]
        print(df)
    except IndexError:
        df = df.append(pd.DataFrame([[username] + user_key_list], columns=['username','consumer_key','consumer_secret','access_token','access_token_secret']),ignore_index=True)
        print(df,"[INDEX ERROR] username not found, appending in excel. ")
    except Exception as e:
        print('ERROR:',e)
    try:
        df.to_excel(user_keys_excel)
        print(df)
    except:
        print('ERROR IN TO EXCEL')

def delete_first_app(driver, username):
    driver.get('https://apps.twitter.com/')
    try:
        elem = driver.find_element_by_css_selector("div.app-details > h2 > a")
        elem.click()
        driver.get(driver.current_url[:-4] + "delete")
        elem = driver.find_element_by_name("op")
        time.sleep(4)
        elem.click()
        time.sleep(4)
        print("App deleted")
        #Removing the username entry from the excel file.
        #This will remove multiple entries as well.
        df = pd.read_excel(user_keys_excel, sheet_name = "Sheet1")
        df = df[df.username != username]
        df.to_excel(user_keys_excel)
    except:
        print("Error: No app found, or error in excel deletion.")

def delete_from_excel(username):
    df = pd.read_excel(user_keys_excel, sheet_name = "Sheet1")
    df = df[df.username != username]
    df.to_excel(user_keys_excel)

#driver - webdriver.Chrome(executable_path = path)
# login(driver, username, password)
# delete_first_app(driver, username)
# create_app(driver, app_name = 'trial___1')
#put_to_excel(get_keys_of_first_app(driver), username, user_keys_excel)
# print(get_keys_of_first_app(driver))
#delete_from_excel(username)
# create_or_get_keys(driver, app_name = "trail___1", login_excel = login_excel)

## PHONE VERIFY CODE
  # df = pd.read_excel(login_excel)
        # df_index = int(df[df.username == username].index.to_native_types()[0])
        # print(df_index)
        # df.loc[df_index]['issues'] = 'phone verify'
        # df.to_excel(login_excel)}
