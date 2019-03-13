import requests
import xmltodict


class Pipeline:
    data = None

    def do_transformation(self):
        self.data = xmltodict.parse(self.data)
        self.data = self.data['result']
        return self.data

    def get_data(self):
        url = "http://localhost:8000/data.xml"
        self.data = requests.get(url)
        self.data = self.data.text
        return self.data


if __name__ == "__main__":
    p = Pipeline()
    p.get_data()
    p.do_transformation()
    print(p.data)
