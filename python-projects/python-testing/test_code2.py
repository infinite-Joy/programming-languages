import unittest

from code2 import get_data


class MockResponse:
    def __init__(self, url):
        self.url = url
        self.text = "mockdata"


class MockRequests:
    def get(url):
        return MockResponse(url)


class MockTransformer:
    def parse(data):
        return {"result": {"sector": "parsed " + data}}


class TestCode2(unittest.TestCase):
    def test_get_data(self):
        res = dict(get_data(client=MockRequests, transformer=MockTransformer))
        self.assertEqual(res['sector'], 'parsed mockdata')


if __name__ == '__main__':
    unittest.main()
