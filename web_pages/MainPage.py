from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация главной страницы.

        :param driver: Объект WebDriver для взаимодействия с браузером.
        """
        self._driver: WebDriver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
       
    @allure.step("Открыть Корзину")
    def open_cart(self) -> None:
        """
        Кликнуть на кнопку "Корзина".

        :return: None
        """
        cart_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
        )
        cart_button.click()

    @allure.step("Открыть страницу Доставка и оплата")
    def open_delivery(self) -> None:
        """
        Кликнуть на кнопку "Доставка и оплата".

        :return: None
        """
        delivery_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/delivery"]'))
        )
        delivery_button.click()

    @allure.step("Открыть страницу Подарочные сертификаты")
    def open_gift(self) -> None:
        """
        Кликнуть на кнопку "Подарочные сертификаты".

        :return: None
        """
        gift_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/certificate"]'))
        )
        gift_button.click()

    @allure.step("Открыть страницу Магазинов")
    def open_shops(self) -> None:
        """
        Кликнуть на кнопку "Магазины".

        :return: None
        """
        shops_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/shops"]'))
        )
        shops_button.click()

    @allure.step("Открыть страницу Что ещё почитать?")
    def open_articles(self) -> None:
        """
        Кликнуть на кнопку "Что ещё почитать?".

        :return: None
        """
        articles_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/collections"]'))
        )
        articles_button.click()

    @allure.step("Найти книгу")
    def find_books(self, value: str):
        self._driver.find_element(By.CSS_SELECTOR, "input.header-search__input").send_keys(value + Keys.RETURN)


