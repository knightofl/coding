import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


option = Options()
option.headless = True

browser = webdriver.Chrome(
    executable_path='/home/lupin3se/Downloads/chromedriver',
    options=option)
browser.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')

time.sleep(3)
tag_names = browser.find_element_by_css_selector('.rank_top1000_list')\
    .find_elements_by_tag_name('li')

for tag in tag_names:
    print(tag.text.split('\n'))
