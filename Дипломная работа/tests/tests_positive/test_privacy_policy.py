import time

from selenium.webdriver.common.by import By


def test_privacy_policy(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Нажимаем кнопку политика конфиденциальности
    driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/a[1]/span[1]').click()
    # Переходим на новую открытую вкладку
    driver.switch_to.window(driver.window_handles[-1])
    # Проверяем, что мы оказались на странице политика конфиденциальности
    assert driver.current_url == "https://msk.rt.ru/legal"
    assert (driver.find_element(By.XPATH,
            '//*[@id="block-rt-ru-super-content"]/article[1]/div[1]/div[1]/div[1]/div[1]/h2[1]').text ==
            "Политика конфиденциальности (условия обработки информации о пользователях)")
