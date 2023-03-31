from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Firefox import driver





def all_pets_with_photo():
   #ждем что находимся на текущей странице
   WebDriverWait(driver, 100).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))


   # Сохраняем в переменную ststistic элементы статистики
   statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   images = driver.find_elements(By.CSS_SELECTOR, ".table.table-hover img")

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   print(number)
   number = number[1].split(' ')
   print(number)
   number = int(number[1])
   half = number // 2


   number_of_photos = 0

   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_of_photos += 1

   assert number_of_photos >= half

   print(f'количество петов с фото больше половины и составляет: {number_of_photos}')
   driver.quit()



all_pets_with_photo()

