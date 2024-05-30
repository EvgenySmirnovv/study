import time

import pytest
from selenium.webdriver.common.by import By


def english_chars():
    return 'abcdefghijklmnopqrstuvwxyz'


def num_chars():
    return '1234567890'


def generate_string(num):
    return "x" * num


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
                            , generate_string(255)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            , num_chars()
                        ],
                        ids =
                        [
                            'english'
                            , 'English'
                            , '255 symbols'
                            , 'russian'
                            , 'RUSSIAN'
                            , 'chinese'
                            , 'specials'
                            , 'digit'
                        ])
def test_param_line_email(line, driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим параметризацию
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(line)
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает сравнение
    assert data == line

    """Так же сделал отдельно тесты в случае если надо проверить одно значения, а не все.
    Так как раз отдельно проверка проходит где сравнение должно быть '!=' или проверка спецсимволов у поле 'телефон'
    так как '+' должен приниматься в поле """


def test_english_upper_chars_email(driver):
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


def test_english_chars_email(driver):
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


def test_russian_chars_email(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим кириллицу
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(russian_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает русские буквы
    assert data == russian_chars()


def test_russian_upper_chars_email(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    up = russian_chars().upper()
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим кириллицу заглавными
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(up)
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает заглавные русские буквы
    assert data == up
    '''Комментарий: Тест не проходит, хотя написан правильно. Есть не большая фитча, при переходи с номера телфона на 
        логин или емайл, авто тест не может отправить в строку большие буквы. В ручном тестирование большие буквы
        вписываются и в деволтулс командой "document.querySelector('input[id=/"username/"]').value = 'ЛОГИН';" буквы 
        прописываются большими. С ментором не получилось разобрать это, сказали оставить пока так.'''


def test_chinese_chars_email(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим китайские символы
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(chinese_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает китайские символы
    assert data == chinese_chars()


def test_special_chars_email(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим спецсимволы
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(special_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает все спецсимволы
    assert data == special_chars()


def test_generate_string_email_255(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим необходимое число символов
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(generate_string(255))
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Строка принимает такое кол-во символов
    assert len(data) == 255


def test_generate_string_email_1000(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим необходимое число символов
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(generate_string(1000))
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Строка должна принимать меньше количество символов
    assert len(data) != 1000


def test_num_chars_email(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим цифры
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(num_chars())
    time.sleep(1)
    # Выводим текст в переменную
    data = driver.find_element(By.CSS_SELECTOR, 'input#username').get_attribute('value')
    print(data)
    # Принимает все цифры
    assert data == num_chars()
