from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ResultPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы результатов.

        :param driver: Объект WebDriver для взаимодействия с браузером.
        """
        self._driver: WebDriver = driver

    @allure.step("Получить текст Корзины")
    def get_cart_text(self) -> str:
        """
        Получить текст заголовка страницы Корзины.

        :return: Текст заголовка Корзины.
        """
        cart_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return cart_text.text

    @allure.step("Получить текст Доставка и оплата")
    def get_delivery_text(self) -> str:
        """
        Получить текст заголовка страницы Доставка и оплата.

        :return: Текст заголовка Доставка и оплата.
        """
        delivery_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return delivery_text.text

    @allure.step("Получить текст Книга - лучший подарок")
    def get_gift_text(self) -> str:
        """
        Получить текст заголовка страницы Подарочные сертификаты.

        :return: Текст заголовка Книга - лучший подарок.
        """
        gift_text = WebDriverWait(self._driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return gift_text.text

    @allure.step("Получить текст Магазинов")
    def get_shops_text(self) -> str:
        """
        Получить текст заголовка страницы Магазинов.

        :return: Текст заголовка Магазинов.
        """
        shops_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return shops_text.text

    @allure.step("Получить текст Что ещё почитать?")
    def get_articles_text(self) -> str:
        """
        Получить текст заголовка страницы Что ещё почитать?.

        :return: Текст заголовка Что ещё почитать?.
        """
        articles_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[class="app-title app-title--mounted content-list-page__title app-title--header-1 app-title--caps"'))
        )
        return articles_text.text

    @allure.step("Получить заголовок первой книги")
    def get_book_title(self) -> str:
        """
        Получить заголовок книги по заданному href и title.

        :return: Текст заголовка книги.
        """
        book_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/section/div/article[1]/div[2]/a/div/div[1]')
            )
        )
        return book_element.text
