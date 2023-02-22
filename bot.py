import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def download_file(url, file_path):
    from requests import get
    reply = get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in reply.iter_content(chunk_size=1024): 
            if chunk:
                file.write(chunk)

driver = webdriver.Chrome()

driver.get("https://online-audio-converter.com/fr/")
driver.implicitly_wait(3)

# close popup
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[@class='x']")
    )
).click()

# wait until slider is rendered
slider_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "slider_2_button")
    )
)
# drag slider
move = ActionChains(driver)
move.click_and_hold(slider_button).move_by_offset(350, 0).release().perform()

# get filename from command line arguments
filename = sys.argv[1]
# upload file
upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
upload_button.send_keys(f"{os.getcwd()}/{filename}")

# wait until file is uploaded
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//li[@class='file_item']")
    )
)
# press convert button
convert_button = driver.find_element(By.ID, "converter")
convert_button.click()

# get download element
download_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.ID, "download_file_link")
    )
)
# get file link
url = download_element.get_attribute("href")
download_file(url, f"{os.getcwd()}/{filename}.converted")