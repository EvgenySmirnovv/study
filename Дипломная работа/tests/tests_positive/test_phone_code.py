import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()
passwordValid = os.getenv("passwordValid")
phoneValid = os.getenv("phoneValid")


def test_phone_valid(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope'
               '=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps'
               '%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22252D8757-1C60-4457-A5C3-5681373CE5BD%22%7D')
    driver.implicitly_wait(5)
    # Вводим телефон
    driver.find_element(By.CSS_SELECTOR, 'input#address').send_keys(phoneValid)
    # Нажимаем кнопку
    driver.find_element(By.ID, 'otp_get_code').click()
    # Вводим одноразовый код. Ставим задержку в 30 сек для ввода кода с телефона
    # После того как ввели код, сайт автоматически сам проверяет его
    time.sleep(30)
    # Ждем загрузки главной страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "root")))
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.current_url == 'https://start.rt.ru/?tab=main'
