from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_all_pets(driver):
    driver.get('https://petfriends.skillfactory.ru/login')
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
     # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    driver.implicitly_wait(10)
    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
    driver.save_screenshot('result_show_all_pets.png')