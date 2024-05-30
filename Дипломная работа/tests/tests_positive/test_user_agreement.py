import time

from selenium.webdriver.common.by import By


def test_user_agreement(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Нажимаем кнопку пользовательского соглашения
    driver.find_element(By.ID, 'rt-auth-agreement-link').click()
    # Переходим на новую открытую вкладку
    driver.switch_to.window(driver.window_handles[-1])
    # Проверяем, что мы оказались на странице пользовательского соглашения
    assert driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
