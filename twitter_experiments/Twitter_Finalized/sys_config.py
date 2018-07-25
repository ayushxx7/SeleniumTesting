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
		driver.close()
	except:
		path = chromedriver_win()
		driver = webdriver.Chrome(path,chrome_options = chrome_options)
		driver.close()
	return path

path = chromedriver_universal()
