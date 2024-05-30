import time

import pytest
from selenium.webdriver.common.by import By


def english_chars():
    return 'abcdefghijklmnopqrstuvwxyz'


def num_chars():
    return '1234567890'


def generate_string(num):
    return "8" * num


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.mark.parametrize("line",
                        [
                            english_chars()
                            , english_chars().upper()
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                        ],
                        ids =
                        [
                            'english'
                            , 'English'
                            , 'russian'
                            , 'RUSSIAN'
                            , 'chinese'
                        ])
def test_param_line_phone(line, driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем телефон
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим параметризацию
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(line)
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает сравнение
    assert data != line

    """Так же сделал отдельно тесты в случае если надо проверить одно значения, а не все.
    Так как раз отдельно проверка проходит где сравнение должно быть '!=' или проверка спецсимволов у поле 'телефон'
    так как '+' должен приниматься в поле """


def test_english_upper_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)

    # Выбираем логин
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Вводим кириллицу заглавными
    up = english_chars().upper()
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(up)
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    print(up)
    # Принимает заглавные русские буквы
    assert data == up


def test_english_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем логин
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Вводим кириллицу
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(english_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает русские буквы
    assert data == english_chars()


def test_russian_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим кириллицу
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(russian_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, ввод должен принимать только цифры
    assert data != russian_chars()


def test_russian_upper_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    up = russian_chars().upper()
    # Вводим кириллицу
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(up)
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, ввод должен принимать только цифры
    assert data != up


def test_chinese_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим китайские символы
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(chinese_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, ввод должен принимать только цифры
    assert data != chinese_chars()


def test_special_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим спецсимволы
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(special_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, должен принимать только один спецсимвол "+"
    assert data == "+"


def test_generate_string_phone_255(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим необходимое число символов
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(generate_string(255))
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, он не должен быть столько символов
    assert data != generate_string(255)
    # Проверяем что кол-во цифр соответствует нужному кол-ву
    count = sum(1 for i in data if i.isdigit())
    assert count == 11
    """Комментарий: тут нужно было бы проверить еще на соответствие номеров. Если номер начинается на +7 то будет 11 
    цифр, а если на +375 то их должно быть 12. По умолчанию номера начинаются с +7"""


def test_generate_string_phone_1000(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим необходимое число символов
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(generate_string(1000))
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, тем более не должен быть столько символов
    assert len(data) != 1000


def test_num_chars_phone(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим цифры
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(num_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Так как это номер телефона, должны быть все цифры
    assert data == "+7 123 456-78-90"
