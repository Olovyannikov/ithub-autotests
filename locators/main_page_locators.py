from selenium.webdriver.common.by import By

class MainPageLocators:
    PHONE = (By.XPATH, "//span[text()='123456789']")
    WISHLIST = (By.ID, "wishlist-total")
    CART = (By.XPATH, "//a[contains(@title, 'Shopping Cart')]")
    CHECKOUT = (By.XPATH, "//a[contains(@title, 'Checkout')]")
    MY_ACCOUNT = (By.XPATH, "//a[contains(text(), 'My Account')]")
    SEARCH = (By.NAME, "search")
    LOGO = (By.XPATH, "//div[@id='logo']/a/img")
    CONTACT_US = (By.LINK_TEXT, "Contact Us")
    RETURNS = (By.LINK_TEXT, "Returns")