import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utils.functions import Global_functions

t = time.sleep(3)
class Schedule_travel():

     def __init__(self,driver):
        # Inicializa el controlador
        self.driver = driver

     #Here we booking the flight
     def Booking_flight(self,city):
          driver = self.driver
          try:
               f = Global_functions(driver)
               time.sleep(5)
               mainpage = driver.find_element(By.XPATH, "//img[@alt='avianca']")
               mainpage.is_displayed()
               f.Xpath_text("//input[@placeholder='Hacia']", city, 3)
               f.Click_ID_Check("ATL", 3)
               time.sleep(5)
               f.Click_Xpath_Check(
                    "//div[@aria-label='17-1-2025']//span[@class='custom-day_day'][normalize-space()='17']", 4)
               f.Click_Xpath_Check(
                    "//div[@aria-label='21-1-2025']//span[@class='custom-day_day'][normalize-space()='21']", 4)
               f.Click_Xpath_Check("//div[@class='ui-num-ud']/button[@class='ui-num-ud_button plus']", 4)
               f.Click_ID_Check("searchButton", 4)
               time.sleep(3)

          except TimeoutException as ex:
               print(ex.msg)
               print("Element is not displayed")

     def Choose_fly(self):
          driver = self.driver
          try:
               f = Global_functions(driver)
               f.Click_Xpath_Check("//button[@class='journey_price_button ng-tns-c12-3 ng-star-inserted']",3)
               f.Click_Xpath_Check("//div[@class='fare-control fare8 fare-recommended cro-new-classic-button']//button[@class='fare_button']",3)
               f.Click_Xpath_Check("//div[@class='cro-button cro-no-accep t-upsell-button']",3)






          except TimeoutException as ex:
               print(ex.msg)
               print("Element is not displayed")







