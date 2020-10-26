from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), f"Корзина не пустая"

    def should_be_empty_basket_message(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text,\
            f"нет сообщения 'корзина пуста'"
