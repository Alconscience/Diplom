import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from web_pages.MainPage import MainPage
from web_pages.ResultPage import ResultPage


@pytest.mark.ui_test
@allure.title("Тест открытия страницы Корзины")
@allure.description("Проверка, что текст заголовка страницы Корзины соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_cart_page():
    """Тест для открытия страницы Корзины и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_cart()

        cart_page = ResultPage(browser)
        cart_text = cart_page.get_cart_text()

        with allure.step("Проверка текста заголовка Корзины"):
            assert cart_text == "КОРЗИНА", f"Expected 'Корзина' but got '{cart_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы Доставка и оплата")
@allure.description("Проверка, что текст заголовка страницы Доставка и оплата соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_promotions_page():
    """Тест для открытия страницы Доставка и оплата и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_delivery()

        delivery_page = ResultPage(browser)
        delivery_text = delivery_page.get_delivery_text()

        with allure.step("Проверка текста заголовка Доставка и оплата"):
            assert delivery_text == "ДОСТАВКА И ОПЛАТА", f"Expected 'ДОСТАВКА И ОПЛАТА' but got '{delivery_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы Подарочные сертификаты")
@allure.description("Проверка, что текст заголовка страницы Подарочные сертификаты соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_sales_page():
    """Тест для открытия страницы Подарочные сертификаты и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_gift()

        gift_page = ResultPage(browser)
        gift_text = gift_page.get_gift_text()

        with allure.step("Проверка текста заголовка Книга - лучший подарок"):
            assert gift_text == "Книга – лучший подарок", f"Expected 'Книга – лучший подарок' but got '{gift_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы Магазинов")
@allure.description("Проверка, что текст заголовка страницы Магазинов соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_shops_page():
    """Тест для открытия страницы Магазинов и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_shops()

        shops_page = ResultPage(browser)
        shops_text = shops_page.get_shops_text()

        with allure.step("Проверка текста заголовка Магазинов"):
            assert shops_text == "НАШИ МАГАЗИНЫ", f"Expected 'НАШИ МАГАЗИНЫ' but got '{shops_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Тест открытия страницы Что ещё почитать?")
@allure.description("Проверка, что текст заголовка страницы Что ещё почитать? соответствует ожидаемому.")
@allure.feature("Проверка страниц")
@allure.severity(allure.severity_level.NORMAL)
def test_open_articles_page():
    """Тест для открытия страницы Что ещё почитать? и проверки заголовка."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        main_page = MainPage(browser)
        main_page.open_articles()

        articles_page = ResultPage(browser)
        articles_text = articles_page.get_articles_text()

        with allure.step("Проверка текста заголовка Что ещё почитать?"):
            assert articles_text == "ЧТО ЕЩЁ ПОЧИТАТЬ?", f"Expected 'ЧТО ЕЩЁ ПОЧИТАТЬ?' but got '{articles_text}'"
    finally:
        browser.quit()


@pytest.mark.ui_test
@allure.title("Проверка заголовка первой книги после поиска")
@allure.description(
    "Проверяем, что заголовок первой книги на странице результатов поиска соответствует ожидаемому значению.")
@allure.feature("Поиск книг")
@allure.severity(allure.severity_level.NORMAL)
def test_find_first_book_title():
    search_value = "Стивен Кинг идет в кино"  # Ожидаемый заголовок первой книги
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        main_page = MainPage(browser)
        main_page.find_books(search_value)  # Ищем книгу по названию

        result_page = ResultPage(browser)
        first_book_title = result_page.get_book_title()  # Получаем заголовок первой книги

        assert first_book_title == search_value, f"Expected '{search_value}' but got '{first_book_title}'"
    finally:
        browser.quit()
