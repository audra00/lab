import pytest
from account import *


class Test:

    def setup_method(self):
        self.account1 = Account('Jeremy')

    def teardown_method(self):
        del self.account1

    def test_init(self):
        assert self.account1.get_name() == 'Jeremy'
        assert self.account1.get_balance() == 0

    def test_withdraw(self):
        # negative, zero, positive invalid, positive valid
        assert self.account1.withdraw(-5) is False
        assert self.account1.get_balance() == 0

        assert self.account1.withdraw(0) is False
        assert self.account1.get_balance() == 0

        assert self.account1.withdraw(10) is False
        assert self.account1.get_balance() == 0

        self.account1.deposit(5)
        assert self.account1.withdraw(5) is True
        assert self.account1.get_balance() == 0

    def test_deposit(self):
        #negative, zero, valid (positive)
        assert self.account1.deposit(-5) is False
        assert self.account1.get_balance() == 0

        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == 0

        assert self.account1.deposit(5) is True
        assert self.account1.get_balance() == 5
