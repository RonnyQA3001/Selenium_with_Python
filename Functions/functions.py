import time
import unittest
from sys import executable

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class Global_functions():

    def __init__(self,driver):
        self.driver = driver

    def Timer(self,ti):
        t = time.sleep(ti)
        return t

    def Browse(self,url,timer):
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(timer)
        return t

    def Xpath_text(self,xpath,txt,timer):
        val = self.driver.find_element(By.XPATH, xpath)
        val.clear()
        val.send_keys(txt)
        t = time.sleep(timer)
        return t

    def ID_text(self,id,txt,timer):
        val = self.driver.find_element(By.ID, id)
        val.clear()
        val.send_keys(txt)
        t = time.sleep(timer)
        return t

    def Click_Xpath_Valida(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def Click_ID_Valida(self,id,tiempo):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID,id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)

