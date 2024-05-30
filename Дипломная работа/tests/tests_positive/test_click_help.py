import time

from selenium.webdriver.common.by import By



def test_click_help(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c'
               '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope'
               '=openid&state=ac430121-8a61-410e-8d51-016d4d0a1a5b&theme=light&auth_type')
    driver.implicitly_wait(5)
    # Нажимаем кнопку Помощь
    driver.find_element(By.XPATH, '//*[@id="faq-open"]/a[1]').click()
    # Проверяем, что мы оказались на странице помощи
    assert (driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]').text ==
            "Ваш безопасный ключ к сервисам Ростелекома")
