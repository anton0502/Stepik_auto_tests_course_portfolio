from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE)
        price = product_price.text
        print(price)
        price_in_basket_ = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket = price_in_basket_.text
        print(price_in_basket)
        assert price == price_in_basket, f'цена продукта не равна цене в корзине'

    def product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product = product_name.text
        print(product)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        product_in_basket = product_name_in_basket.text
        print(product_in_basket)
        assert product == product_in_basket, f'имя продукта в корзине не совпадает с именем продукта на странице'
