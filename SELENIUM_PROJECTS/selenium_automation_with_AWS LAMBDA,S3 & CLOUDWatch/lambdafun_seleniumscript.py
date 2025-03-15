import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def lambda_handler(event, context):
	options = Options()
	options.headless = True
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
	try:
    	driver.get(event['url'])
    	title = driver.title
    	driver.quit()
    	return {
        	'statusCode': 200,
        	'body': json.dumps(f"Title: {title}")
    	}
	except Exception as e:
    	driver.quit()
    	return {
        	'statusCode': 500,
        	'body': json.dumps(str(e))
    	}

