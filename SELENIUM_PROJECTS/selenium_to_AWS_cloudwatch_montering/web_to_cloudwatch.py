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

driver.get("https://sourcecode.academy/")

start_time = time.time()
driver.get("https://sourcecode.academy/")
end_time = time.time()
load_time = end_time - start_time

cloudwatch = boto3.client('cloudwatch')

cloudwatch.put_metric_data(
    Namespace='WebPerformance',
    MetricData=[
        {
            'MetricName': 'PageLoadTime',
            'Value': load_time,
            'Unit': 'Seconds',
            'Dimensions': [
                {
                    'Name': 'WebPage',
                    'Value': 'sourcecode.com'
                },
            ]
        },
    ]
)

driver.quit()
