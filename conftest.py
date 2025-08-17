import pytest
from playwright.sync_api import BrowserContext
from pages.create_account_page import CreateAccount
from pages.eco_friendly_pages import EcoFriendly
from pages.sale_page import SalePage
from pages.product_card_page import ProductCard


@pytest.fixture(scope='function')
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    # pages.set_default_navigation_timeout(4000)
    # pages.set_default_timeout(4000)
    return page


@pytest.fixture()
def create_account(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale(page):
    return SalePage(page)


@pytest.fixture()
def product_card(page):
    return ProductCard(page)