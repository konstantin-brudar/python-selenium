# Тесты UI на Python и Selenium

## Задача

Автоматизировать тестирование логина на сайте https://skyrexio.com с использованием Python, PyTest и Selenium.

Реализовать паттерн проектирования Page Object Model (POM).

Настроить отчетность при помощи Allure.

## Запуск тестов и создание отчета

Запуск тестов из модуля `test_login` и запись результатов в каталог `allure-results`:

```
$ pytest tests/test_login.py --alluredir=allure-results
```

Запуск Allure отчета из каталога `allure-results`:

```
$ allure serve allure-results
```