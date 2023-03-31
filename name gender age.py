from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Firefox import driver


def name_gender_age():
    WebDriverWait(driver, 100).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pets_data = driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")
    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
    # с ожидаемым результатом
    for i in range(len(pets_data)):
        data_pet = pets_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)

        assert result >= 3

    print(f'name gender and age: заполнены')
    driver.quit()




name_gender_age()