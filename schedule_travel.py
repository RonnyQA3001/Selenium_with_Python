import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Functions.functions import Global_functions

driver = webdriver.Chrome()

driver.get("https://www.avianca.com/es/")
driver.maximize_window()
t = 3

try:
     WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='avianca']")))
     f = Global_functions(driver)
     time.sleep(5)
     Mainpage = driver.find_element(By.XPATH,"//img[@alt='avianca']")
     Mainpage.is_displayed()
     f.Xpath_text("//input[@placeholder='Hacia']","ATL",2)
     f.Click_ID_Valida("ATL",3)
     time.sleep(5)
     f.Click_Xpath_Valida("//div[@aria-label='17-1-2025']",4)
     f.Click_Xpath_Valida("//div[@aria-label='21-1-2025']",4)
     f.Click_Xpath_Valida("//div[@class='ui-num-ud']/button[@class='ui-num-ud_button plus']",4)


except TimeoutException as ex:
    print(ex.msg)
    print("Element is not displayed")
