import pytest


@pytest.mark.parametrize('browser', ['Chrome', 'Firefox', 'Safari'])
def test_with_param1(browser):
    assert browser in ['Chrome', 'Firefox', 'Safari']


@pytest.mark.parametrize('browser, version',
                         [('Chrome', 94),
                          ('Firefox', 85),
                          ('Safari', 13.2)],
                         ids=['Chrome', 'Firefox', 'Safari']
                         # убираем ненужную информацию кортежей, задаём имя параметризации
                         )
def test_with_param2(browser, version):
    assert browser in ['Chrome', 'Firefox', 'Safari']


# итого 9 тестов
@pytest.mark.parametrize('browser', ['Chrome', 'Firefox', 'Safari'])
@pytest.mark.parametrize('user', ['guest', 'manager', 'admin'])
def test_with_param3(browser, user):
    pass


@pytest.mark.parametrize('browser',
                         [
                             pytest.param('Chrome', id='Chrome'),
                             pytest.param('Firefox', marks=[pytest.mark.slow]),
                             pytest.param('Safari', marks=[pytest.mark.xfail(reason='TASK-1234')])
                         ]
                         )
@pytest.mark.parametrize('user', ['guest', 'manager', 'admin'])
def test_with_param4(browser, user):
    pass
