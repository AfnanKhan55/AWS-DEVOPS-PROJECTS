from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import boto3
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

s3 = boto3.client('s3')

driver.get("https://aws.amazon.com/")
driver.save_screenshot("screenshot.png")

bucket_name = 'sel-test-bucket1'
object_name = 'screenshot.png'
s3.upload_file('screenshot.png', bucket_name, object_name)

time.sleep(10)
driver.quit()

