import time
from selenium.webdriver.common.by import By


def test_petfriends(selenium):
    # Open PetFriends base page:
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!



    # click on the new user button
    btn_newuser = selenium.find_element(By.XPATH, "(//button[@onclick=\"document.location='/new_user';\"])")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("fandangoo@gmail.com")

    # add password
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("123456")

    # click submit button
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")