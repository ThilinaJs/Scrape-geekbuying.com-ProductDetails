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

search.send_keys('Kitchen Appliance')

search.send_keys(Keys.ENTER)

product_name =driver.find_elements("xpath", '//li[@class="searchResultItem"]/div/div[2]/a[1]')
product_new_price = driver.find_elements("xpath", '//li[@class="searchResultItem"]/div/div[3]')
product_old_price = driver.find_elements("xpath", '//li[@class="searchResultItem"]/div/div[3]/span')
likes = driver.find_elements("xpath", '//li[@class="searchResultItem"]/div/div[5]/div/span')

w=[]
for i in product_new_price:
    w.append(i.text[0:3])

df = pd.DataFrame(columns=['Product Name','Product New Price','Product Old Price','No of Likes'])

for i in range(len(product_name)):
    df = df.append({'Product Name':product_name[i].text,'Product New Price':w[i],'Product Old Price':product_old_price[i].text,'No of Likes':likes[i].text}, ignore_index=True)

df.to_excel('KitchenApplianceDetails.xlsx',index=False)