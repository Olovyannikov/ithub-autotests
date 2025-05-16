import logging
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_title(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.get_title() == "Your Store"

def test_phone_number(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.PHONE)

def test_wishlist_link(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    title = page.get_element_attribute(MainPageLocators.WISHLIST, "title")
    assert title == "Wish List (0)"

def test_cart_link(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.CART)

def test_checkout_link(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.CHECKOUT)

def test_my_account_dropdown(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.MY_ACCOUNT)

def test_search_box(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.SEARCH)

def test_logo(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.LOGO)

def test_contact_us_link(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.CONTACT_US)

def test_returns_link(driver, base_url):
    page = MainPage(driver, base_url)
    page.load()
    assert page.is_element_visible(MainPageLocators.RETURNS)