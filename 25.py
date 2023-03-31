from selenium import webdriver
import time
from settings import valid_email, valid_password
import get_geckodriver
import pytest_selenium



url = 'https://petfriends.skillfactory.ru/login'

driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)

driver.save_screenshot('2.png')

time.sleep(2)






driver.close()

