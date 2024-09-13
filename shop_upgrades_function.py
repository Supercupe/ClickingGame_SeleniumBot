from selenium.webdriver.common.by import By


class ShopUpgradeHandler:
    def __init__(self, driver):
        self.driver = driver

    def click_upgrade0(self):
        try:
            upgrade_button = self.driver.find_element(By.CSS_SELECTOR, "div #upgrade0")
            upgrade_button.click()
        except Exception as e:
            print(f"Error clicking upgrade0: {e}")
