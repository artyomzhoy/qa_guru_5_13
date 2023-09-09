"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1366, 768)])
def browser_size_desktop(request):
    size = request.param

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    browser.config.driver = driver

    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = size[0]
    browser.config.window_height = size[1]

    yield browser
    browser.close()


@pytest.fixture(params=[(375, 667), (667, 375), (480, 800)])
def browser_size_mobile(request):
    size = request.param

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    browser.config.driver = driver

    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = size[0]
    browser.config.window_height = size[1]

    yield
    browser.close()


def test_github_desktop(browser_size_desktop):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_size_mobile):
    browser.open('')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
