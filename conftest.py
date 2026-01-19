# conftest.py
import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

@pytest.fixture
def browser_context(pw):
    # Change headless=True -> False when you want to see browser UI
    #browser = pw.chromium.launch(headless=False)
    # conftest.py (browser_context fixture)
    browser = pw.chromium.launch(headless=False)  # see the browser during debugging

    context = browser.new_context()
    yield context
    context.close()
    browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
