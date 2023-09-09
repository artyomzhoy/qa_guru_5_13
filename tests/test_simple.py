import random

import pytest
import time


# применение ко всем тестам файла этого skip
# pytestmark = pytest.mark.skip(reason='Тест флакает/нестабилен, исправляется в рамках TASK-1234')


@pytest.fixture()
def browser():
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


@pytest.mark.fast
def test_1(browser):
    time.sleep(1)


@pytest.mark.slow
def test_2(browser):
    time.sleep(5)


@pytest.mark.skip(reason='Тест флакает/нестабилен, исправляется в рамках TASK-1234')
def test_3(browser):
    time.sleep(5)


@pytest.mark.skip(reason='Тест ещё не реализован в рамках TASK-1234')
def test_4(browser):
    time.sleep(5)


# @pytest.mark.skipif(reason='Тест ещё не реализован в рамках TASK-1234')
# def test_5(browser):
#     time.sleep(5)


@pytest.mark.xfail(reason='')
def test_5(browser):
    user1 = random.randint(0, 100)
    user2 = random.randint(0, 100)
    assert user1 == user2


def test_6(browser):
    user1 = random.randnt(0, 100)
    user2 = random.randint(0, 100)

    # лучшее применение xfail, чтобы отслеживать, что ошибка осталось той же
    assert user1 <= 100
    assert user2 <= 100
    try:
        assert user1 == user2
    except AssertionError:
        pytest.xfail('TASK-1234')
