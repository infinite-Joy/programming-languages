import unittest

from code5 import Pipeline


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
    def setUp(self):
        self.p = Pipeline(MockRequests, MockTransformer)

    def tearDown(self):
        pass

    def test_get_data(self):
        res = self.p.get_data()
        self.assertEqual(res, 'mockdata')

    def test_do_transform(self):
        self.p.data = 'md'
        res = self.p.do_transformation()
        self.assertEqual(res['sector'], 'parsed md')


if __name__ == '__main__':
    unittest.main()
