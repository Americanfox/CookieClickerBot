from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("D:\dev-tools\chromedriver.exe")
driver = webdriver.Chrome(service=service)

def check_score():
    score = driver.find_element(By.ID, "money")
    print(int(score.text))

def check_upgrades():

    buy_cursor = driver.find_element(By.ID, "buyCursor").text.split()[2]
    buy_grandma = driver.find_element(By.ID, "buyGrandma").text.split()[2]
    buy_factory = driver.find_element(By.ID, "buyFactory").text.split()[2]
    buy_mine = driver.find_element(By.ID, "buyMine").text.split()[2]
    buy_shipment = driver.find_element(By.ID, "buyShipment").text.split()[2]
    buy_alchemy = driver.find_element(By.ID, "buyAlchemy lab").text.split()[3]
    buy_portal = driver.find_element(By.ID, "buyPortal").text.split()[2]
    buy_timemachine = driver.find_element(By.ID, "buyTime machine").text.split()[3]

def launchbrowser():
    launch = True
    driver.get(
        "http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID, "cookie")
    click_cookie = True
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    item_ids = [item.get_attribute("id") for item in items]
    # print(item_ids)
    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    price = [p.text for p in all_prices]
    print(price)
    print(all_prices)
    while click_cookie:
        cookie.click()





    while launch:
         pass

launchbrowser()
