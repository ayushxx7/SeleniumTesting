import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

def chromedriver_mac():
    import os.path
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(PROJECT_ROOT, "chromedriver/Chromedriver")
    return path

def chromedriver_win():
	abs_dir_path = os.path.abspath(__file__) # absolute file path
	req_path = abs_dir_path.rpartition('\\')
	chrome_driver_path = req_path[0] + '\\chromedriver\\chromedriver.exe'
	return chrome_driver_path

def chromedriver_universal():
	try:
		path = chromedriver_mac()
		driver = webdriver.Chrome(path,chrome_options = chrome_options)
		# print(os.path.isfile(path))
		# print(os.path.exists(path))

	except:
		path = chromedriver_win()
		# print(os.path.exists(path))
		
		# print(os.path.isfile(path))
		
		# print(os.listdir(path))

		driver = webdriver.Chrome(path,chrome_options = chrome_options)
	return (path, driver)	

# cd_u = chromedriver_universal()
# for i in cd_u:
# 	print(i)
path,driver = chromedriver_universal()
# driver = chromedriver_universal()[1]
# path = chromedriver_win()
