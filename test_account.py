from pytest import *
from account import *


class Test:

    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'

    def test_deposit(self):
        # negative, zero, positive
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(1.5) is True
        assert self.a1.get_balance() == 1.5

    def test_withdraw(self):
        # negative, zero, positive invalid, positive valid
        assert self.a1.withdraw(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        self.a1.deposit(1.5)
        assert self.a1.withdraw(3.5) is False
        assert self.a1.get_balance() == 1.5

        assert self.a1.withdraw(1.0) is True
        assert self.a1.get_balance() == .5
