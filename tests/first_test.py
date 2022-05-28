import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multyply_calculated_faild(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_multyply_calculated_fail_ore_true(self):
        assert self.calc.multiply(self, 2, 2) != 5
