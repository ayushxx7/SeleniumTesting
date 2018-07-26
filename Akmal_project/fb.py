from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fblogin import username,password #shifted to seperate file

# from pynput.keyboard import Key, Controller

# import keyboard

# keyboard = Controller()

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(r'C:\testDir\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)

# wait = WebDriverWait(driver,10)

# def super_get(url):
#     driver.get(url)
#     driver.execute_script("window.alert = function() {};")

#driver = webdriver.Chrome(r'C:\Users\Ayush\Desktop\chromedriver_win32\chromedriver.exe')
driver.get('http://www.facebook.com/login')
# super_get('http://www.facebook.com/login')

driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(password)
driver.find_element_by_name('login').click()	
# time.sleep(2)
driver.maximize_window()
# time.sleep(6)
searchbox = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'q')))
searchbox.click()
# driver.find_element_by_name('q').send_keys('Ayush Mandowara' + Keys.RETURN)	
searchbox.send_keys('Ayush Mandowara' + Keys.RETURN)
# searchbox.click()

# time.sleep(5)
# element = wait.until(EC.presence_of_element_located((By.xpath, '//input[@placeholder="Search"]'))
# driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys('Ayush Mandowara' + Keys.RETURN)
# time.sleep(4)
def cover_pic_name():
	firstresult = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Ayush Mandowara")]')))
	firstresult.click()
	# driver.find_element_by_xpath('//div[contains(text(), "Ayush Mandowara")]').click()
	# time.sleep(8)
	coverpic = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.coverBorder')))
	coverpic.click()
# driver.find_element_by_class_name('coverBorder').click()
# time.sleep(2)


# for i in range(0,len(like)):
# 	liked = like[x].get_attribute("data-testid")
# 	if liked == "fb-ufi-likelink":
# 		like[x].click()

def liker():
	####LIKE
	actions = ActionChains(driver)

	time.sleep(8)

	for i in range(0,10):
		time.sleep(2)
		like = driver.find_elements(By.CSS_SELECTOR, ".UFILikeLink._4x9-._4x9_._48-k")
		x = len(like)-1
		print(like[x])
		time.sleep(1)
		liked = like[x].get_attribute("data-testid")
		print(liked)
		if liked == "fb-ufi-likelink":
			like[x].click()
		actions.send_keys(Keys.RIGHT)
		actions.perform()

		
		actions.send_keys(Keys.RIGHT)
		actions.perform()
		time.sleep(2)

	# driver.execute_script("var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');for(var i= 0;i<elems.length;i++){elems[i].click();}");
	#element.get_attribute("attribute name")
def comment():
	### COMMENT
	time.sleep(5)
	comment = driver.find_elements(By.CSS_SELECTOR, ".comment_link._5yxe")
	x = len(comment)-1
	comment[x].click()
	time.sleep(2)
	actions = ActionChains(driver)
	actions.send_keys('dummydata'+Keys.RETURN)
	
	actions.perform()

def share_to_own_timeline():
### SHARE

	time.sleep(8)
	is_displayed():
	share = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".share_action_link._5f9b")))
	time.sleep(6)

	image = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.spotlight')))
# time.sleep(10) #bottleneck
# share = driver.find_elements(By.CSS_SELECTOR, ".share_action_link._5f9b")

	share = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".share_action_link._5f9b")))
	while len(share) < 4:
		share = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".share_action_link._5f9b")))
		print('len(share):',len(share))
		# pass

	x = len(share)-1	
	if(share[x].is_displayed()):
		share[x].click()

def chooser_for_share()
	count = 0
	chooser = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-testid="share_on_own"]')))
	while len(chooser) < 2:
		chooser = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-testid="share_on_own"]')))
		print('len(chooser):',len(chooser))
		count += 1
		if count > 10:
			print('enough retries, breaking')
			break


	x = len(chooser)-1	
	if(chooser[x].is_displayed()):
		chooser[x].click()

def share_to_friend():
# ####### SHARE TO FRIEND
# shareToFriend = driver.find_elements_by_xpath('//span[@data-testid="share_to_person"]')
	chooser_for_share()
	shareToFriend = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-testid="share_to_person"]')))
	share2 = len(shareToFriend)-1
	shareToFriend[share2].click()
	element = driver.find_element_by_xpath("//button[contains(.,'Post')]")
	print(element)

	friendName = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,	'//input[@placeholder="Friend\'s name"]')))
	print(friendName)
	friendName[0].send_keys('mihir' + Keys.DOWN + Keys.RETURN)
	element.click()



def share_in_group():
#########SHARE IN GROUP
	chooser_for_share()
	shareInGroup = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-testid="share_to_group"]')))
	# shareToFriend = driver.find_elements_by_xpath('//span[@data-testid="share_to_person"]')
	share2 = len(shareInGroup)-1
	shareInGroup[share2].click()
	element = driver.find_element_by_xpath("//button[contains(.,'Post')]")
	print(element)

	groupName = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,	'//input[@placeholder="Group name"]')))
	print(groupName)
	groupName[0].send_keys('mihir' + Keys.DOWN + Keys.RETURN)
	element.click()


def share_to_event():
#########SHARE TO EVENT
	chooser_for_share()
	shareInEvent = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,'//span[@data-testid="share_to_event"]')))
	# shareToFriend = driver.find_elements_by_xpath('//span[@data-testid="share_to_person"]')
	share2 = len(shareInEvent)-1
	shareInEvent[share2].click()
	element = driver.find_element_by_xpath("//button[contains(.,'Post')]")
	print(element)

	eventName = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH,	'//input[@placeholder="Event name"]')))
	print(eventName)
	eventName[0].send_keys('mihir' + Keys.DOWN + Keys.RETURN)
	element.click()


#### CODE WRITTEN WHILE TESTING. MIGHT BE USEFUL.
# time.sleep(9) #bottleneck

# x = len(share)-1	
# if(share[x].is_displayed()):
# 	share[x].click()
# else:

# 	share = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".share_action_link._5f9b")))
# 	x = len(share)-1	
# 	share[x].click()


# time.sleep(12)

# share2 = driver.find_elements(By.CSS_SELECTOR, "._1jlx")
# share2.click()#share_on_own
# time.sleep(10) #unable to overcome this hurdle, need to figure it out 
#img class = spotlight
# chooser = driver.find_element_by_xpath('//span[@data-testid="share_on_own"]')
# chooser[len(chooser)-1].click()
# chooser.click()
# time.sleep(6)
# chosen = len(chooser)-1
# # parent = chooser[chosen].find_element_by_xpath('..')
# # print(parent.get_attribute(''))
# chooser[chosen].click()



# friendName.click()
# actions = ActionChains(driver)
# actions.send_keys(Keys.RETURN)
# actions.perform()
# element.click()

# # + Keys.DOWN + Keys.RETURN)
# actions.perform()

# placeholder="Friend's name"
# element.click()
# share_action_link _5f9b

# actions = ActionChains()
# keyboard.write('The quick brown fox jumps over the lazy dog.')
# keyboard.type('Hello World')

# comment[x].send_keys('')
# y = comment[x].click()
# y.send_keys('asd')
# for x in range(0,len(comment)):
# 	    if comment[x].is_displayed():
# 	        comment[x].click()
# element = driver.find_element_by_xpath('//a[contains(text(), "Like")]')
# driver.find_element_by_class_name('coverBorder').send_keys("l")
# print(element)
# driver.execute_script("arguments[0].click();", element)
# element = driver.find_element_by_xpath("//button[contains(.,'comment')]")

# element = driver.find_element_by_xpath('//input[@placeholder="Write a comment..."]').send_keys('pro')
# element.click()
'''
if file name is selenium there will be error

FACEBOOK CLASS:
<div class="_524d"><div class="_42nr _1mtp"><span class="_1mto"><div class="_khz _4sz1 _4rw5 _3wv2"><a aria-pressed="true" class="UFILikeLink _4x9- _4x9_ _48-k UFILinkBright" data-testid="fb-ufi-unlikelink" href="#" role="button" tabindex="0" style="color: rgb(53, 120, 229);">Like</a><div class="_2r6l accessible_elem"><div class="_1oxj uiLayer hidden_elem" style="opacity: 1; left: 499px; top: 358px; z-index: 301;"><div class="_49v-"><div height="52" class="_1oxk"><div class="_iu- _628b _1ef3" data-testid="UFIReactionsMenu" aria-label="Reactions" role="toolbar"><span aria-pressed="true" aria-label="Like" class="_iuw" data-testid="reaction_1" href="#" role="button" tabindex="0"><div class="_39m _1ef2" data-reaction="1"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Like</div></div></div></div></span><span aria-pressed="false" aria-label="Love" class="_iuw" data-testid="reaction_2" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="2"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Love</div></div></div></div></span><span aria-pressed="false" aria-label="Haha" class="_iuw" data-testid="reaction_4" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="4"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Haha</div></div></div></div></span><span aria-pressed="false" aria-label="Wow" class="_iuw" data-testid="reaction_3" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="3"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Wow</div></div></div></div></span><span aria-pressed="false" aria-label="Sad" class="_iuw" data-testid="reaction_7" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="7"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Sad</div></div></div></div></span><span aria-pressed="false" aria-label="Angry" class="_iuw" data-testid="reaction_8" href="#" role="button" tabindex="-1"><div class="_39m _1ef2" data-reaction="8"><div class="_39n _6a9w"><div class="_1ef0" style="display: inline-block; line-height: 0; font-size: 0px;"><canvas width="39" height="39" style="width: 39px; height: 39px;"></canvas></div><div class="_d6l"><div class="_4sm1">Angry</div></div></div></div></span></div><div class="_41nt" style="height: 52px;">
</div></div></div></div></div></div></span><span class="_1mto"><span class="_6a _15-7 _3h-u _4k43"><a class="comment_link _5yxe" role="button" href="#" title="Leave a comment" data-ft="{ &quot;tn&quot;: &quot;S&quot;, &quot;type&quot;: 24 }">Comment</a></span></span><span class="_1mto"><span class="_27de _4noj"><a href="/ajax/sharer/?s=2&amp;appid=2305272732&amp;id=1121385471215631&amp;p[0]=1121385471215631&amp;sharer_type=all_modes&amp;av=100011339780683&amp;feedback_referrer=%2Fayush.mandowara&amp;feedback_source=17" rel="dialog" class="share_action_link _5f9b" role="button" tabindex="0" data-ft="{ &quot;tn&quot;: &quot;J&quot;, &quot;type&quot;: 25 }" title="Send this to friends or post it on your Timeline.">Share</a></span></span></div></div>


<a class="comment_link _5yxe" role="button" href="#" title="Leave a comment" data-ft="{ &quot;tn&quot;: &quot;S&quot;, &quot;type&quot;: 24 }">Comment</a>


data-offset-key="fvq43-0-0"
'''

########## Default EC LIST

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

##########
