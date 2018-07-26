from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from fb_credentials import username,Password
# username = "xxxxxxxxx"
# Password = "xxxxxxxxx"
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

time.sleep(3)
search = driver.find_element_by_name('q')
search.send_keys("Shahrukh Khan" + Keys.RETURN)
# driver.find_element_by_xpath('//input[@placeholder = "Search"]').send_keys("Shahrukh Khan" + Keys.RETURN)

time.sleep(5)

people = driver.find_elements_by_class_name('_4jq5')
# people = WebDriverWait(driver, 30).until(EC.presence_of_elements_located((By.CSS_SELECTOR, '._4jq5')))
people[2].click()

time.sleep(3)

SendReq = driver.find_elements_by_css_selector('._42ft._4jy0.FriendRequestAdd.addButton._4jy3._517h._51sy')
# driver.execute_script("window.scrollTo(0, 1080)")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

for i in range(3) :
	SendReq[0].send_keys(Keys.PAGE_DOWN)
	time.sleep(20)
	SendReq[0].send_keys(Keys.END)
	time.sleep(20)
	SendReq = driver.find_elements_by_css_selector('._42ft._4jy0.FriendRequestAdd.addButton._4jy3._517h._51sy')
	
	for i in SendReq :
	
	# i.click()
	# time.sleep(5)
	# driver.executse_script("window.scrollTo(0, 1080)")
		try :
			i.click()
			time.sleep(3)
		# driver.execute_script("window.scrollTo(0, 1080)")

		except :
		# confirm = driver.find_element_by_css_selector('._42ft._4jy0.layerConfirm.uiOverlayButton._4jy3._4jy1.selected._51sy')
		# confirm.click()
		
			try:
		   
				confirm = driver.find_element_by_css_selector('._42ft._4jy0.layerConfirm.uiOverlayButton._4jy3._4jy1.selected._51sy')
				confirm.click()
				time.sleep(2)
	
			except :

			# Close = driver.find_elements_by_class_name('autofocus')
				Close = driver.find_element_by_css_selector('.autofocus.layerCancel._4jy0._4jy3._4jy1._51sy.selected._42ft')
				Close.click()



# print(len(SendReq))
# counter = 0



# for i in range(3) :
# 	SendReq[0].send_keys(Keys.PAGE_DOWN)
# 	time.sleep(2)
# 	SendReq[0].send_keys(Keys.END)
# 	time.sleep(3)
# 			# print("No Confirm Button")

		# try : 

		# 	Close = driver.find_element_css_selector('.autofocus.layerCancel._4jy0._4jy3._4jy1._51sy.selected._42ft')
		# 	Close.click()
		# except:
		# 	print('Good to go')
# confirm = driver.find_element_by_css_selector('._42ft._4jy0.layerConfirm.uiOverlayButton._4jy3._4jy1.selected._51sy')
# confirm.click()

# for i in range(5):
# 	sentcount = 0
# 	send_req_all = driver.find_elements_by_css_selector('._42ft._4jy0.FriendRequestAdd.addButton._4jy3._517h._51sy')
#     confirm = driver.find_element_by_css_selector('._42ft._4jy0.layerConfirm.uiOverlayButton._4jy3._4jy1.selected._51sy')
# confirm.click()


# 	print(len(send_req_all))
# 	print(send_req_all)
# 	for i in send_req_all:
# 		print(i.text)

# 	for i in join_list:
# 		print(i.text)
# 		try:
# 			if(i.text == 'Join'):
# 			# i.click()
# 				driver.execute_script("arguments[0].click();", i)
# 				sentcount += 1	
# 				totalrequest += 1
# 				# try:
# 				# 	time.sleep(3)
# 				# 	answer_for_group = driver.find_element_by_xpath('//textarea[title="Write an answer..."]')
# 				# 	# for i in answer_for_group:

# 				# 	answer_for_group.send_keys('I am a big fan of Aam Aadmi Party, Arvind Sir is doing a good job! Hope he wins in all future elections! He has done a great job in Delhi!')
# 				# except:
# 				# 	print('nahi mila khushi hai')
# 				# 	pass		
# 		except:
# 			print('hamse na ho payega')
# 			pass
# 	driver.refresh()
# 	print('Request Sent:',sentcount)
# 	print('Total Request Sent:',totalrequest)