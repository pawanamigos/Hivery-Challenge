import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import OrderedDict

def launch_amazon_get_product_details_iphone11(url):
    driver = webdriver.Chrome(r'C:\Users\Pawan\PycharmProjects\Hivery\venv\utils\chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('iPhone11')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
    time.sleep(4)
    listed_prices = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-price-whole']")
    product_names = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-size-base-plus a-color-base a-text-normal']")
    product_links = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    for list in listed_prices:
        list = str(list.text).replace(",","")
        all_prices.append(int(list))
    for products in product_names:
        all_products.append(products.text)
    for links in product_links:
        all_links.append(links.get_attribute('href'))
    return all_products, all_prices, all_links

def launch_ebay_get_product_details_iphone11(url):
    driver = webdriver.Chrome(r'C:\Users\Pawan\PycharmProjects\Hivery\venv\utils\chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="gh-ac"]').send_keys('iPhone11')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gh-btn"]').click()
    time.sleep(4)
    listed_prices = driver.find_elements(By.XPATH,"//div[@class='s-item__info clearfix']//span[@class='s-item__price']")
    product_names = driver.find_elements(By.XPATH,"//div[@class='s-item__info clearfix']//div[@class='s-item__title']")
    product_links = driver.find_elements(By.XPATH,"//div[@class='s-item__info clearfix']//a[@class='s-item__link']")
    for list in listed_prices:
        list = str(list.text).replace("AU", '')
        try:
            list = list[2:5:1]
            all_prices.append(int(list))
        except ValueError as ve:
            print("")
    for products in product_names:
        all_products.append(products.text)
    for links in product_links:
        # print(links.get_attribute('href'))
        all_links.append(links.get_attribute('href'))
    return all_products, all_prices, all_links
    driver.close()



if __name__ == "__main__":
    list_dict = {}
    new_dict = {"": {"price": "", "link": ""}}
    all_prices = []
    all_products = []
    all_links = []
    launch_amazon_get_product_details_iphone11('https://www.amazon.com.au/')
    launch_ebay_get_product_details_iphone11('https://www.ebay.com.au/')
    new_dict = dict(map(lambda x, y, z : (str(x), {"price": y ,"link": str(z)}), all_products, all_prices, all_links))
    sorted_dict = OrderedDict(sorted(new_dict.items(), key=lambda i:i[1]['price']))
    for key,value in sorted_dict.items():
       print(key, value)



