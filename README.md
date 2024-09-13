This project is an automated version of the popular Cookie Clicker game, initially inspired by an exercise from Angela Yu's Udemy course on Python programming. The project has been expanded to include several other features, such as purchasing upgrades and usage of classes.

Features:
Cookie Clicking Automation: The bot automatically clicks the cookie at regular intervals to increase your cookie count.
Item Purchasing: The bot purchases items from the shop, prioritizing the most expensive items that you can afford to maximize efficiency.
Upgrades Management: In addition to items, the bot can also purchase available upgrades to enhance gameplay.
Object-Oriented Design: The code has been structured into classes for better modularity and readability, handling cookie clicking, item purchasing, and upgrades in separate components.
Key Classes:
ShopHandler: Handles the identification and purchase of in-game items, sorts them by price, and attempts to buy the most expensive affordable item.
ShopUpgradeHandler: Manages in-game upgrades, including identifying and purchasing available upgrades.
Technologies Used:
Python: The core logic and game automation.
Selenium: Used for web automation to interact with the Cookie Clicker game elements in the browser.
