from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Firefox import driver



def all_pets_with_different_names():
    WebDriverWait(driver, 100).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))




    pet_data = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    print(len(pet_data))
    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('x', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

        # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
        # Проверяем, если r == 0 то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
                r += 1

    if r > 0:
        assert r > 0
        print('есть повторяющиеся имена')
        driver.quit()
    else:
        assert r == 0
        print(pets_name)
        print('повторяющихся имен нет')
        driver.quit()





all_pets_with_different_names()