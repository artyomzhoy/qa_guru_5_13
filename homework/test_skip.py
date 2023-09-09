"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1366, 768), (375, 667), (667, 375), (480, 800)],
                ids=['desktop', 'desktop', 'desktop', 'mobile', 'mobile', 'mobile'])
def browser_size(request):
    size = request.param
    ids = request.node.callspec.id

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    browser.config.driver = driver

    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = size[0]
    browser.config.window_height = size[1]

    yield browser, ids
    browser.close()


def test_github_desktop(browser_size):
    web_browser, ids = browser_size
    if 'mobile' in ids:
        pytest.skip('Соотношение сторон не для десктопа.')
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_size):
    web_browser, ids = browser_size
    if 'desktop' in ids:
        pytest.skip('Соотношение сторон не для мобильных устройств.')
    browser.open('')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
