from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_data_my_pets(driver):
    driver.get('https://petfriends.skillfactory.ru/login')
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('fandangoo@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    '''time.sleep(2)'''
    driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
    driver.implicitly_wait(3)
    names = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(1)')
    breeds = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(2)')
    ages = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(3)')
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    for i in range(len(pets_count)):
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''
    driver.save_screenshot('result_data_my_pets.png')
