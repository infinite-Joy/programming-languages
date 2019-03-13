import unittest
from unittest.mock import patch

from code4 import Pipeline


class MockResponse:
    def __init__(self, url):
        self.url = url
        self.text = "mockdata"


class TestCode2(unittest.TestCase):
    def setUp(self):
        self.p = Pipeline()

    def tearDown(self):
        pass

    @patch('code4.requests.get')
    def test_get_data(self, mock_client):
        mock_client.return_value = MockResponse("abc")
        res = self.p.get_data()
        self.assertEqual(res, 'mockdata')

    @patch('code4.xmltodict')
    def test_do_transform(self, mock_transformer):
        mock_transformer.parse.return_value = {"result": {"sector": "parsed md"}}
        res = self.p.do_transformation()
        self.assertEqual(res['sector'], 'parsed md')


if __name__ == '__main__':
    unittest.main()
