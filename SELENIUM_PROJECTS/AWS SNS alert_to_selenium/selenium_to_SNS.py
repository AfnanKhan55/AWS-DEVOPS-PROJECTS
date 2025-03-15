from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import boto3

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://alnafi.com/auth/sign-in")

try:
    element = driver.find_element(By.NAME, "email1")
    print("Element Found")
except:
    print("Element not found. Test Failed.")
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:050451388866:seleniumtestfailure:0c4a4bd8-8521-424a-a91f-be0928fe5551',
        Message='Selenium test failed. Check logs for details.'
    )

driver.quit()

