# Проект по автоматизации API и UI тестирования на Python для компании веб-сервиса Читай город

***
«Читай-город» – это самая большая в России сеть книжных магазинов и интернет-магазин.

Данная компания продает не только книги, а также канцтовары, сладости, подарочную упаковку и идеи для сюрпризов близким.
«Читай-город» разрабатывает дизайны для ежедневников, закладок, товаров для творчества и других интересных вещей.
Целью автоматизации является повышение качества и надежности веб-сайта, а также снижение затрат на ручное
тестирование.<br>
Для проекта был выбран функционал, доступный в веб-интерфейсе
и через REST API. Составлено 6 UI- и 5 API-автотестов, для формирования отчета о проведенных автотестах используется
инструмент Allure.

## Шаги

1. Склонировать проект `git clone https://github.com/....`
2. Установить зависимости
3. Запустить тесты с указанием пути к директории результатов тестирования `pytest --alluredir allure_files`
4. Открыть отчет `allure serve allure_files`

## Стек

- pytest<br>
- selenium<br>
- requests<br>
- allure<br>
- config<br>

## Структура

- ./test - тесты
    - \_\_init\_\_.py
    - /api_test.py - API-тесты
    - /ui_test.py - UI-тесты
- ./web_pages - описание страниц
    - /CompanyApi.py - описание API-методов
    - /MainPage.py - описание методов на главной странице
    - /ResultPage.py - описание результатов
- ./pytest.ini - файл конфигурации для pytest, который содержит настройки тестирования, такие как параметры командной
  строки и плагины.
- README.md - файл с документацией проекта, в котором описаны установка, использование, структура проекта и другие
  важные аспекты.
- requirements.txt - файл с используемыми зависимостями

## Полезные ссылки

- [Проект Читай город: тест план + отчет о тестировании ]
- [Веб-интерфейс сервиса Читай город ](https://www.chitai-gorod.ru/)

## Библиотеки

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests

## Запуск тестов

- `pytest -m ui_test.py` (запуск только UI тестов)
- `pytest -m api_test.py` (запуск только API тестов)
- `pytest --alluredir allure-result` (запуск тестов и сохранение отчета о результатах тестирования)
- `allure serve allure-result/` (формирование отчета о тестировании)
