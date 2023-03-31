
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Firefox import driver


def all_pets():
   WebDriverWait(driver, 100).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))

   statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   pets = driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")
   number = statistic[0].text.split('\n')
   print(number)
   number = number[1].split(' ')
   print(number)
   number = int(number[1])



   number_of_pets = len(pets)


   assert number == number_of_pets
   print(f'количество животных:{number_of_pets}')

   driver.quit()


all_pets()

