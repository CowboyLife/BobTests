from seleniumbase import BaseCase
import pytest
import allure


class TestBilling(BaseCase):

    @pytest.mark.order(0)
    def test_bills(self):
        if 1 == 2:
            assert False

    @pytest.mark.order(1)
    def test_finance(self):
        if 1 == 1:
            assert False

    @pytest.mark.order(2)
    @pytest.mark.dependency(depends=['test_finance'])
    def test_money(self):
        if 1 == 2:
            assert False
