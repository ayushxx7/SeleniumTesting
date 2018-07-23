from sys_config import path, chrome_options, webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from file_path import login_excel

### LOGGING ###
import coloredlogs,logging
coloredlogs.install()
# import logging
logging.basicConfig(level=logging.INFO)
# logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
# logger.setLevel(level)
# logger.propagate = False
### LOGGING ####

login_excel_dataframe = pd.read_excel(login_excel)

def login(driver, username, password):
#NEED TO CHECK IF CONNECTION IS ACTIVE OR NOT! 
    time.sleep(1)
    try:
        driver.get('https://apps.twitter.com/')
        logger.info('apps.twitter.com opened')
    except:
        logger.error("NOT CONNECTED TO THE INTERNET!") ###NEEDS IMPROVEMENT
        return '404'

    signIn = driver.find_element_by_xpath('//a[@href="https://twitter.com/login?redirect_after_login=https%3A//apps.twitter.com/"]');
    signIn.click()
    logger.info("Username:%s", username)

    email = driver.switch_to_active_element()#Maybe we will select element instead of this.
    time.sleep(3)
    email.send_keys(username)
    logger.info("email entered")
    email.send_keys(Keys.TAB)

    time.sleep(1)
    email = driver.switch_to_active_element()
    email.send_keys(password)
    email.send_keys(Keys.RETURN)
    logger.info("password entered")

    time.sleep(2)
    # print(driver.current_url)
    logger.info(driver.current_url)
    if(driver.current_url != 'https://apps.twitter.com/'):
      logger.error('Not an Active Account!')
      return False

    logger.info("Logged in successfully with username:%s",username)
    return True

def read_login_credentials():
    issues = []
    for username, password in zip(login_excel_dataframe.username, login_excel_dataframe.password):
        
        for i in range(3):
            driver = webdriver.Chrome(executable_path = path)
            logger.info("Chrome Driver Initiated")
            logger.info("Attempt #%i",i)
            status = login(driver, username, password)    
            if (status):
            # Will check through app creation later.
                logger.info("changing status to active")
                issues.append("active")
                break
            elif status == '404':
                logger.warning("status code 404 received, Stopping read_login_credentials execution!")
                break
            else:
                logger.info("changing status to not active")
                issues.append("not active")
            
            logger.info("Closing Chrome Driver")
            driver.close()
    login_excel_dataframe['issues'] = issues
    login_excel_dataframe.to_excel(login_excel)

def convert_to_dictionary():
    logger.info("Converting active users to credential dictionary")
    return {i:j for i, j, k in zip(login_excel_dataframe.username, login_excel_dataframe.password, login_excel_dataframe.issues) if k == 'active'}

# read_login_credentials()