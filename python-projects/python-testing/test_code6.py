import unittest

from code6 import CustomSession


class MockResponse:
    def __init__(self, url, **kwargs):
        self.url = url
        self.text = "mockdata"
        self.status_code = 200

    def raise_for_status(self):
        pass


class MockSession:
    def get(self, url, **kwargs):
        return MockResponse(url)


class TestAppClient(MockSession, CustomSession):
    pass


class TestCode6(unittest.TestCase):
    def setUp(self):
        self.c = TestAppClient()

    def tearDown(self):
        pass

    def test_get_data(self):
        res = self.c.get_data("http://dummy.com/uri")
        self.assertEqual(res.text, 'mockdata')


if __name__ == '__main__':
    unittest.main()
