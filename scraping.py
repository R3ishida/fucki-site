import requests
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/ryozo/Downloads/chromedriver")
driver.get("google.com")
