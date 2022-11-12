from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options

# Navigate to result page
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.geekbuying.com/')

driver.maximize_window()

x = driver.find_element("xpath", '//*[@class="close_btn line_close close_sub"][1]')
x.click()

search = driver.find_element("xpath", '//div[@class="search_input"]/input[2]')
search.click()

search.send_keys('e bike')

search.send_keys(Keys.ENTER)

