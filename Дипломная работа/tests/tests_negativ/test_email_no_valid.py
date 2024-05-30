from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()
password = os.getenv("passwordValid")
email = os.getenv("mailNoValid")


def test_email_no_valid(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Выбираем почту
    driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    # Вводим email
    driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys(email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button#kc-login').click()
    # Проверяем, что мы не перешли на страницу пользователя
    assert driver.current_url == ('https://b2c.passport.rt.ru/account_b2c/page?state=ac430121-8a61-410e-8d51'
                                  '-016d4d0a1a5b&client_id=account_b2c&theme=light#/')
    assert driver.find_element(By.XPATH, '//*[@id="form-error-message"]').text == "Неверный логин или пароль"
