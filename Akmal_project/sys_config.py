from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

def mac_abhishek():
    import os.path
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(PROJECT_ROOT, "/Users/tuffy/Desktop/pr/Chromedriver")
    return path

def pc_ayush():
	path = 'C:\\testDir\\chromedriver_win32\\chromedriver.exe'
	return path

def pc_akmal():
	path = "C:\\Users\\Admin\\Desktop\\chromedriver.exe"
	return path

path = pc_akmal()
