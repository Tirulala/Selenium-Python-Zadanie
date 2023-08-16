import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    """Добавление опции командной строки.
    В командную строку передается параметр '--language=es' / '--language=fr'
    По умолчанию английский язык интерфейса
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    # Передача из командной строки параметра language в переменную browser_language
    browser_language = request.config.getoption('language')

    # Инициализация опции браузера
    options = Options()

    # Передача в опции webdriver параметра из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    browser.quit()



#pytest -v --tb=line --language=en test_main_page.py.
# Здесь и далее мы будем использовать эту команду для запуска.
# В этой команде мы использовали опцию PyTest --tb=line, которая указывает,
# что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.