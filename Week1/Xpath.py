from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

LINK = 'https://formy-project.herokuapp.com/form'

driver.get(LINK)

driver.find_element(By.XPATH, '(//input[1]')