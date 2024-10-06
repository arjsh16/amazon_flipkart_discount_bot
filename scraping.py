#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#function to scrape amazon
def amazon_lookup(book_link):
    #service=Service(ChromeDriverManager().install())
    service=Service(executable_path=r'the path to chrome driver')
    driver=webdriver.Chrome(service=service) #opens browser
    driver.get(book_link) #opens the product link
    time.sleep(7) #gives time for the page to load
    discount_percentage_xpath = "//span[@class='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage']" #this pin points the discount
    discount_percentage_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, discount_percentage_xpath))) #waits for the discount element to become interactable
    discount_percentage = float(discount_percentage_element.text.replace("%","")) #turns the discount into a float type data for comparision
    driver.quit#closes browser
    return (-1*discount_percentage)
#works in the same manner as the amazon code but for flipkart
def flipkart_lookup(book_link):
    service = Service(executable_path=r'the path to chrome driver')
    driver = webdriver.Chrome(service=service)
    driver.get(book_link)
    time.sleep(7)

    discount_percentage_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='UkUFwK WW8yVX']/span")))
    discount_percentage = float(discount_percentage_element.text.strip().replace("%", "").replace("off",""))

    driver.quit()
    return discount_percentage
