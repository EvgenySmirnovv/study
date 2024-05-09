'''from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://google.com')'''
import time

def test_search_example(driver):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    driver.get('https://google.com')

    time.sleep(0)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = driver.find_element("name", "q")


    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = driver.find_element("name", 'btnK')
    search_button.click()

    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    driver.save_screenshot('result.png')