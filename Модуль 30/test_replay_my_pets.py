from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_replay_my_pets(driver):
    driver.get('https://petfriends.skillfactory.ru/login')
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('fandangoo@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('123456')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr')))
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    list_pets = []

    for i in range(len(pets_count)):
        list_pets.append(pets_count[i].text[:-2:])
        print(list_pets)

    set_pets = set(list_pets)
    print(set_pets)

    assert len(set_pets) == len(list_pets)
    driver.save_screenshot('result_all_pets.png')
