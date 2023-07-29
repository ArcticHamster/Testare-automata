import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class ElefanTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("https://www.elefant.ro/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def test_open_site(self):
        time.sleep(2)

    def test_search_product(self):
        #search field
        search_field = self.driver.find_element(By.NAME, "SearchTerm")

        search_field.send_keys("iphone 14")
        time.sleep(2)
        #click search button

        search_button = self.driver.find_element(By.XPATH, "//a[@class='icon-search']//div[@class='icon-wrapper']//*[name()='svg']")
        search_button.click()
        time.sleep(4)
        #products
        products = self.driver.find_elements(By.CLASS_NAME, "product-title")
        self.assertGreaterEqual(len(products), 10)

    #extrageti din lista produsul cu pretul cel mai mic
    def test_lowest_price_product(self):
        products = self.driver.find_elements(By.XPATH, "//div[@class='current-price ']" )
        lowest_price = float("inf")

        for product in products:
            price_value = float(product.get_attribute("data-price"))
            if price_value < lowest_price:
                lowest_price = price_value

        print(f'Lowest price: {lowest_price}')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

# tema: sa folosim id-uri noi, sa facem css-uri