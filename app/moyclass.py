import requests


class APIMoyClass:
    def __init__(self):
        self.base_url = 'https://api.moyklass.com/v1/company/'

    def get_filials(self):
        res = requests.get(self.base_url + f'filials')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
