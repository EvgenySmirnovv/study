from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv


load_dotenv()
passwordValid = os.getenv("passwordValid")
phoneValid = os.getenv("phoneValid")


def test_phone_valid(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope'
               '=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps'
               '%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22252D8757-1C60-4457-A5C3-5681373CE5BD%22%7D')
    driver.implicitly_wait(5)
    # Вводим телефон или почту
    driver.find_element(By.CSS_SELECTOR, 'input#address').send_keys(phoneValid)
    # Нажимаем кнопку
    driver.find_element(By.ID, 'otp_get_code').click()
    # Нажимаем кнопку "Изменить номер"
    driver.find_element(By.ID, 'otp-back').click()
    # Проверяем, что мы вернулись на страницу ввода телефона или почты
    assert driver.current_url == ('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution'
                                  '=400655d2-c988-4155-a840-341f26e97255&client_id=lk_b2c&tab_id=FP8GAc-gYfs')
    assert driver.find_element(By.ID, 'card-title').text == 'Авторизация по коду'

