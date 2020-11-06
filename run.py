from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pathlib import Path
import os
import time   


notebook_url = 'https://colab.research.google.com/github/mengwangk/dl-projects/blob/master/04_03_auto_ml_1.ipynb'
chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = Config.GOOGLE_CHROME_BIN
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(notebook_url)

# run all cells
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.F9)
time.sleep(5)

# click to stay connected
start_time = time.time()
current_time = time.time()
max_time = 11*59*60 #12hours

while (current_time - start_time) < max_time:
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    driver.find_element_by_xpath('//*[@id="top-toolbar"]/colab-connect-button').click()
    time.sleep(30)
    current_time = time.time()
