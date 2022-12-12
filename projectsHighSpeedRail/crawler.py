import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://www.thsrc.com.tw")
driver.implicitly_wait(0.5)

try:
    agree_btn = driver.find_element(
        by=By.CSS_SELECTOR, value=".swal2-confirm")
    agree_btn.click()
except Exception:
    print("同意出錯")


# 選取from
location1 = driver.find_element(by=By.ID, value="select_location01")
selected_location1 = Select(location1)
option_list = selected_location1.options
for item in option_list:
    print(item.get_attribute("value"))

# 要等至可以click時,才可以選取
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "select_location01")))
# selected_location1.select_by_value('TaiPei')
selected_location1.select_by_visible_text('台中')


# 選取to
location2 = driver.find_element(by=By.ID, value="select_location02")
selected_location2 = Select(location2)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "select_location02")))

selected_location2.select_by_visible_text('台南')

# 選取type
types = driver.find_element(by=By.ID, value="typesofticket")
selected_types = Select(types)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "typesofticket")))
selected_types.select_by_visible_text('單程')

# (input)單程
departDate01 = driver.find_element(by=By.ID, value="Departdate01")
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "Departdate01"))).click()

# 因為點選,所以必需執行javascript
now = datetime.today()
current_date = now.strftime("%Y.%m.%d")
current_hour = now.strftime("%H")
driver.execute_script(f'arguments[0].value = "{current_date}";', departDate01)

# (input)去程時間
outWardTime = driver.find_element(by=By.ID, value="outWardTime")
outWardTime.click()
driver.execute_script(
    f'arguments[0].value = "{current_hour}:30";', outWardTime)

# (selected)適用優惠
'''
dropdown = driver.find_element(by=By.CSS_SELECTOR, value="div.dropdown.show-tick")
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.dropdown.show-tick")))
dropdown.click()

offer = driver.find_element(by=By.ID, value="offer")
selected_offer = Select(offer)
option_list = selected_offer.options
for item in option_list:
    print(item.get_attribute("value"))
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"offer")))
selected_offer.select_by_visible_text('早鳥')
'''

# start-search
start_search = driver.find_element(by=By.ID, value="start-search")
start_search.click()

# 必需使用time
time.sleep(5)
html_code = driver.page_source
