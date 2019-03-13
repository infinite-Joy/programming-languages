import unittest

from code3 import get_data
from code3 import do_transformation


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
        res = get_data(client=MockRequests)
        self.assertEqual(res, 'mockdata')

    def test_do_transform(self):
        data = 'md'
        res = do_transformation(data, transformer=MockTransformer)
        self.assertEqual(res['sector'], 'parsed md')


if __name__ == '__main__':
    unittest.main()
