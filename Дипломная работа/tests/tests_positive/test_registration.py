from selenium.webdriver.common.by import By

# Для успешного завершения теста регистрации, в начале теста добавить свои данные!


def test_reg_valid(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Жмем зарегистрироваться
    driver.find_element(By.ID, 'kc-register').click()
    driver.implicitly_wait(5)
    # Вводим Имя
    (driver.find_element(By.CSS_SELECTOR,
                         'section#page-right > div > div > div > form > div > div > div > input').send_keys("Имя"))
    # Вводим Фамилию
    driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > '
                                         'div > input').send_keys("Фамилия")
    # Выбираем свой регион
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]').click()
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[67]').click()
    # Вводим Емайл или телефон
    driver.find_element(By.ID, 'address').send_keys("Телефон")
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys("Пароль")
    # Вводим подтверждаем пароль
    driver.find_element(By.ID, 'password-confirm').send_keys("Подтверждения пароля")
    # Жмем зарегистрироваться
    driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > button').click()
    # Проверяем, что мы оказались на главной странице пользователя
    driver.implicitly_wait(5)
    assert driver.current_url == ('https://b2c.passport.rt.ru/account_b2c/page?state=ac430121-8a61-410e-8d51'
                                  '-016d4d0a1a5b&client_id=account_b2c&theme=light#/')
