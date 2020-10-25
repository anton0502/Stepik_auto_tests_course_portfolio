from .pages.product_page import ProductPage
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.price_in_basket()
    page.product_in_basket()
    time.sleep(10)
