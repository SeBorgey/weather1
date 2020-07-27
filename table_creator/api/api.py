import requests

from weather.table_creator.api.constants import BASE_URL, AUTHORISATION


class API:
    def __init__(self, url='''https://www.googleapis.com/youtube/v3/search''', aut=AUTHORISATION):
        self.url = url
        self.aut = aut

    def send_request(self, lat, lng, start, end):
        self.params = {
            'params': ','.join(['humidity', 'airTemperature']),
            'lat': lat,
            'lng': lng,
            'start': f'{start} 00:00',
            'end': f'{end} 00:00'
        }
        self.lat = lat
        self.lng = lng
        self.start = start
        self.end = end
        self.response = requests.get(self.url, params=self.params, headers=self.aut)
        # json_data = self.response.json()
        return self.response




