from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
from fb_credentials import username, password
from sys_config import path, prefs
# username = "xxxxxxxxxxxxxxxxx"
# password = "xxxxxxxxxxxxxxxxx"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(path, chrome_options=chrome_options)

def login_to_facebook(driver):
    account = ("https://en-gb.facebook.com/login/")
    driver.get(account)
    time.sleep(2)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(password)
    driver.find_element_by_name("login").click()

def create_page(driver):
    driver.refresh()
    create = driver.find_elements_by_class_name('linkWrap')
    create[9].click()

    time.sleep(6)

    create_button = driver.find_element_by_css_selector('._60zj._4jy0._4jy4._4jy2._51sy.selected._42ft')
    create_button.click()

    time.sleep(5)


    # get_started = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._43rl")));

    get_started = driver.find_element_by_css_selector('._43rm')
    get_started.click()
    # get_started.send_keys(Keys.TAB)

    title = driver.find_element_by_xpath('//input[@placeholder="Name your Page"]').send_keys("ABC" + Keys.TAB)

    description = driver.switch_to_active_element()
    # description.send_keys("Just For Fun" + Keys.ENTER)
    description.send_keys(Keys.TAB)

    time.sleep(1)

    policy = driver.switch_to_active_element()
    policy.send_keys(Keys.TAB)

    time.sleep(1)

    Continue = driver.switch_to_active_element()
    Continue.send_keys(Keys.TAB)

    time.sleep(2)

    Social = driver.switch_to_active_element()
    Social.send_keys(Keys.TAB)

    page_name = driver.switch_to_active_element()
    page_name.send_keys("DC Comics" + Keys.TAB)

    time.sleep(1)

    category = driver.switch_to_active_element()
    # category.send_keys("Just For Fun" + Keys.TAB)
    category.send_keys("Just For Fun" + Keys.RETURN)


    time.sleep(1)

    # policy1 = driver.switch_to_active_element()
    # policy.send_keys(Keys.TAB)

    # time.sleep(3)

    # Continue = driver.switch_to_active_element()
    # Continue.send_keys(Keys.ENTER)
    continue1 = driver.find_elements_by_css_selector('._43rm')
    continue1[3].click()

    skip1 = driver.find_elements_by_xpath(("[@href='/pages/create/get_started/save_current_step/?step=profile_picture&page_id=397344647339974&event=skip_button_click']"))
    skip1.click()

    skip2 = driver.find_elements_by_xpath(("[@href='/pages/create/get_started/save_current_step/?step=cover_photo&page_id=397344647339974&event=skip_button_click']"))
    skip2.click()
login_to_facebook(driver)
create_page(driver)
