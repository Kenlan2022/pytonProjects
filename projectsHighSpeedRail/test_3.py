# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_3(self):
    self.driver.get("https://www.thsrc.com.tw/")
    self.driver.set_window_size(851, 852)
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    self.driver.find_element(By.LINK_TEXT, "時刻表與票價").click()
    self.driver.find_element(By.ID, "select_location01").click()
    dropdown = self.driver.find_element(By.ID, "select_location01")
    dropdown.find_element(By.XPATH, "//option[. = '台北']").click()
    self.driver.find_element(By.ID, "select_location02").click()
    dropdown = self.driver.find_element(By.ID, "select_location02")
    dropdown.find_element(By.XPATH, "//option[. = '台南']").click()
    self.driver.find_element(By.ID, "typesofticket").click()
    dropdown = self.driver.find_element(By.ID, "typesofticket")
    dropdown.find_element(By.XPATH, "//option[. = '去回程']").click()
    self.driver.find_element(By.ID, "Departdate03").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .day:nth-child(4)").click()
    self.driver.find_element(By.ID, "outWardTime").click()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) .fa-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) .fa-chevron-up").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) .fa-chevron-up")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-down").click()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-down").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-down")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "Returndate03").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .day:nth-child(5)").click()
    self.driver.find_element(By.ID, "returnTime").click()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) .fa-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) .fa-chevron-up").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) .fa-chevron-up")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-up").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-up")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) .fa-chevron-down").click()
    self.driver.find_element(By.CSS_SELECTOR, ".filter-option-inner-inner").click()
    self.driver.find_element(By.CSS_SELECTOR, ".filter-option-inner-inner").click()
    self.driver.find_element(By.ID, "start-search").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ttab-01_prevPage > .mb-0").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ttab-01_prevPage > .mb-0").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ttab-01_nextPage > .mb-0").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#ttab-01_nextPage > .mb-0")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#ttab-01_nextPage > .mb-0").click()
  
