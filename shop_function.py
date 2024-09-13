from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re


class ShopHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cookie_count(self):
        try:
            count_element = self.driver.find_element(By.CSS_SELECTOR, "div #cookies ")
            count = count_element.text
            match = re.search(r'([\d,]+)', count)
            if match:
                count_text = match.group(1).replace(",", "")
                number_of_cookies = int(count_text)
                return number_of_cookies

        except Exception:
            print(f"Unexpected error retrieving item.")

    def get_shop_items(self):
        items = []
        large_price = 999999999999999999999

        for i in range(0, 3):
            item = self.driver.find_element(By.ID, f"product{i}")

            item_class = item.get_attribute('class')
            if "product unlocked enabled" in item_class:
                price_text = item.find_element(By.CLASS_NAME, "price").text
                print(f"Item {i} price text: '{price_text}'")

                if price_text.strip():
                    try:
                        price = int(price_text.replace(",", ""))
                    except ValueError:
                        price = large_price

                items.append((f"product{i}", price))

        items.sort(key=lambda x: x[1], reverse=True)
        return items

    def buy_items(self):
        while True:
            cookies = self.get_cookie_count()
            if cookies is None:
                print("Failed to retrieve cookie count. Exiting.")
                break

            items = self.get_shop_items()
            bought_something = False

            for item_id, price in items:

                while cookies >= price:
                    self.purchase_item(item_id)
                    bought_something = True

                    new_cookies = self.get_cookie_count()
                    cookies = new_cookies

                else:
                    break

            if not bought_something:
                break

    def purchase_item(self, item_id):
        item = self.driver.find_element(By.ID, item_id)
        item.click()
