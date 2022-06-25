import pytest
from app.moyclass import APIMoyClass

mcl = APIMoyClass()


class TestMoyCl:
    # def setup(self):
    #     self.moyCl = APIMoyClass

    def test_get_filials(self):
        status, result = mcl.get_filials()
        assert status == 200

