import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    language = request.config.getoption("language")
    browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    yield browser
    print("\nquit browser..")
    browser.quit()
