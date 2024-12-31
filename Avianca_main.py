import pytest
from selenium import webdriver

import schedule_travel
from Utils.functions import Global_functions
from schedule_travel import Schedule_travel

driver = ""
f = ""


def test_airline():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    f = Global_functions(driver)
    driver.maximize_window()
    f.Browse("https://www.avianca.com/es/",5)
    st = Schedule_travel(driver)
    st.Booking_flight("ATL")
    st.Choose_fly()




