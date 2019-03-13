import requests
import json
import xmltodict

def do_transformation(data, transformer=xmltodict):
    data = transformer.parse(data)
    return data['result']


def get_data(client=requests):
    #url = "https://api.data.gov.in/resource/ee081658-b9e8-4b8f-afe4-f47c27e24971?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=xml&offset=0&limit=10"
    url = "http://localhost:8000/data.xml"
    data = client.get(url)
    return data.text

if __name__ == "__main__":
    data = get_data()
    data = do_transformation(data)
    print(data)
