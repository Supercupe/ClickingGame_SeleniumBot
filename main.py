import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from shop_function import ShopHandler
from shop_upgrades_function import ShopUpgradeHandler

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

consent_button = driver.find_element(By.CLASS_NAME, "fc-primary-button")
consent_button.click()

time.sleep(3)

language_selector = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_selector.click()

shop_handler = ShopHandler(driver)
shop_upgrade_handler = ShopUpgradeHandler(driver)

time.sleep(3)

cookie_button = driver.find_element(By.ID, "bigCookie")

measure = time.time()
while time.time() - measure < 300:
    end_time = time.time() + 8
    while time.time() < end_time:
        cookie_button.click()
    shop_upgrade_handler.click_upgrade0()
    shop_handler.buy_items()

print("Finished baking.")
time.sleep(5)


driver.quit()
