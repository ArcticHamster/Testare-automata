from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox() #instantiem clasa driverului web
time.sleep(2)


site_path = 'http://formy-project.herokuapp.com'
driver.get(site_path)
time.sleep(1)

# print(driver.title)
#
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element(By.ID,'first-name').send_keys('Selector ID')
# time.sleep(1)

# driver.find_element(By.CLASS_NAME, 'form-control').send_keys('Selector clasa')

# elements = driver.find_elements(By.CLASS_NAME, 'form-control')
# time.sleep(1)
# for element in elements:
#     print(element.id)
#     if element.id == '898d328a-2f53-4db4-ad8b-ba4b0a5bf337':
#         element.send_keys('Laurentiu')
#    print(f'text:{element.text}')

# elemente_control = driver.find_elements(By.CLASS_NAME,'form-control')
# print(f'Avem {len(elemente_control)} elemente cu clasa form-control')

lista_elemente = driver.find_elements(By.TAG_NAME,'a')
print(lista_elemente)
element_a = lista_elemente[1]
element_a.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.LINK_TEXT,'Autocomplete').click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,'Autoco').click()

