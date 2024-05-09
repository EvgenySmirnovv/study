import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.maximize_window()
    yield driver
    driver.quit()

def test_all_pets_in_my_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('fandangoo@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#navbarNav > ul > li > a')))
    driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    pets_number = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]').text.split('\n')[1].split('Питомцев: ')[1]
    assert len(pets_count) == int(pets_number)
    driver.save_screenshot('result_all_pets.png')