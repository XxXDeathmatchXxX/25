from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Firefox import driver


def no_same_pets():
    WebDriverWait(driver, 100).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))

    pet_data = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    print(len(pet_data))
    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('x', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
    # и между ними вставляем пробел

    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')
    print(list_line)

    # Превращаем список в множество
    set_list_line = set(list_line)
    print(set_list_line)

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)
    print(a)
    print(b)
    # Из количества элементов списка вычитаем количество элементов множества
    result = a - b
    if result > 0:
        print(f'Есть повторяющиеся  в количестве: {result}')
        driver.quit()
    # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    else:
        assert result == 0
        print('повторяющихся карточек животных нет')
        driver.quit()



no_same_pets()


