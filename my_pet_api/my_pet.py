from config_my_pet import key_param


def test_key_param(key_param):
    res = key_param
    assert res.status_code == 200
