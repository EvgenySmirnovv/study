from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()
passwordValid = os.getenv("passwordValid")
phoneValid = os.getenv("phoneValid")


def test_phone_valid(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Вводим телефон
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(phoneValid)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(passwordValid)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button#kc-login').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.current_url == ('https://b2c.passport.rt.ru/account_b2c/page?state=ac430121-8a61-410e-8d51'
                                  '-016d4d0a1a5b&client_id=account_b2c&theme=light#/')
