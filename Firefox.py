from selenium import webdriver
from settings import valid_email, valid_password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.FirefoxOptions()


url = 'https://petfriends.skillfactory.ru/login'

driver = webdriver.Firefox()



def login():


    driver.get(url)
    driver.implicitly_wait(5)
    email_input = driver.find_element(By.ID, "email").send_keys(valid_email)
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(valid_password)
    password_input.send_keys(Keys.ENTER)




def my_pets():
    WebDriverWait(driver, 100).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))

    driver.find_element(By.XPATH, "(//a[@class='nav-link'])[1]").send_keys(Keys.ENTER)




login()
my_pets()












# images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
# names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
# descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
#
# for i in range(len(names)):
#         assert images[i].get_attribute('src') != ''
#         assert names[i].text != ''
#         assert descriptions[i].text != ''
#         assert ', ' in descriptions[i]
#         parts = descriptions[i].text.split(", ")
#         assert len(parts[0]) > 0
#         assert len(parts[1]) > 0


