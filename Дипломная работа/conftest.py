import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def driver(request):
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()

    yield driver

    # Получаем скриншот результата
    driver.save_screenshot("./screen/result" + str(uuid.uuid4()) + '.png')
    driver.quit()
