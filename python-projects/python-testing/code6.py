import requests


# This is my target class
class CustomSession(requests.Session):
    def __init__(self):
        super().__init__()
        self.headers.update({'User-agent': 'CustomSession',
                             'Accept': 'application/xml'})

    def get_data(self, url, **kwargs):
        print('Performing GET on {}'.format(url))
        resp = self.get(url=url, **kwargs)
        resp.raise_for_status()
        print('{} returned status: {}'.format(url, resp.status_code)) # a suprising dependency.
        return resp


# An example and usage
class MyAppClient(CustomSession):
    URL = 'http://localhost:8000/data.xml'

    def get_stuff(self):
        resp = super().get_data(url='{}'.format(self.URL))
        return resp


if __name__ == "__main__":
    c = MyAppClient()
    resp = c.get_stuff()
    print(resp.text)