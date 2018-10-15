from selenium.webdriver import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import selenium
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://www.linkedin.com/')
time.sleep(2)
elem = browser.find_element_by_name('session_key')
elem.clear()
elem.send_keys() # your email id 
elem = browser.find_element_by_name('session_password')
elem.clear()
elem.send_keys() # your password
submit = browser.find_element_by_xpath("//*[@type='submit']")
actions = ActionChains(browser)
actions.click(submit)
actions.perform() 

def group_post(url):
    browser.get(url) #group link
    browser.refresh()
    post=browser.find_element_by_class_name("sharing-posting-options--is-disabled")
    post.click() #focus element
    enter_text=browser.find_element_by_class_name("mentions-texteditor__content")
    actions = ActionChains(browser)
    actions.click(enter_text)
    actions.send_keys("Image") #text to post
    photo=browser.find_element_by_class_name("sharing-share-action-media__upload-input-label  ")
    photo=photo.find_element_by_xpath("//input[@type='file']")
    photo.send_keys('test.png') #image to upload
    time.sleep(2)
    actions.perform() 
    post=browser.find_element_by_xpath('//div[@class="sharing-share-box__post-button-container"]')
    button=post.find_element_by_tag_name("button")
    click=post.find_element_by_id(button.get_property("id"))
    time.sleep(1)
    click.send_keys(Keys.SPACE)
    
    
#Enter the url for the group
group_post() # group url 
