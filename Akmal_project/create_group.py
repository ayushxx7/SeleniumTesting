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
from fb_credentials import username,Password
# username = "xxxxxxxxxxxx"
# Password = "xxxxxxxxxxx"
account = ("https://en-gb.facebook.com/login/")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\Users\Admin\Desktop\chromedriver.exe', chrome_options=chrome_options)
driver.get(account)

time.sleep(2)

driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_xpath("//input[@name= 'pass']").send_keys(Password)
driver.find_element_by_name("login").click()

time.sleep(10)

group = driver.find_elements_by_class_name('linkWrap')
group[4].click()

# create = driver.find_elements_by_class_name('_3-8_')
# create[0].click()

time.sleep(5)

create = driver.find_element_by_css_selector('._19a0._8i6._4jy0._4jy3._4jy2._51sy.selected._42ft')
create.click()
time.sleep(5)

group_name = driver.switch_to_active_element()
group_name.send_keys('Matru ki bijli ka mandola' + Keys.TAB)
time.sleep(4)

People = driver.switch_to_active_element()
People.send_keys('Shahrukh Khan, Amir Khan' + Keys.TAB)
time.sleep(4)

switch = driver.find_element_by_css_selector('._3-8y._3-90.rfloat._ohf.img.sp_ZDy4cnNmH7d.sx_75f53a')
switch.click()
time.sleep(3)

Public = driver.find_elements_by_class_name('_54nh')
Public[0].click()
time.sleep(3)

Public_new = driver.find_elements_by_class_name('_4hop')
Public_new.click()
Public_new.send_keys(Keys.TAB)

shortcut = driver.switch_to_active_element()
shortcut.send_keys(Keys.TAB)

Create_button = driver.switch_to_active_element()
# Create.send_keys(Keys.TAB)
Create_button.click()
# Create_group = driver.find_elements_by_class_name('_42ft')
# Create_group[19].click()

# Create_group = driver.find_elements_by_xpath('//button[contains(text(), "Create")]')
# Create_group.click()
# Public[0].click()
# Public[0].send_keys(Keys.TAB)

# shortcut = driver.switch_to_active_element()
# shortcut.send_keys(Keys.TAB)
# create = driver.find_elements_by_xpath("//button[@title='Create']")
# create.click()
# create = driver.find_elements_by_css_selector('._42ft._4jy0.layerConfirm._29bh.uiOverlayButton._4jy3._4jy1.selected._51sy')
# create.click()