import copy

from weather.table_creator.api.api import API


class LocalFiles:
    def __init__(self):
        self.api = API()

    def get_values(self, lat, lng, start, end):
        response = self.api.send_request(lat, lng, start, end)
        var = response.json()
        hours = var['hours']
        self.air_point = copy.deepcopy(hours)
        self.hum_point = copy.deepcopy(hours)
        self.time_point = copy.deepcopy(hours)
        for i in range(0, len(hours)):
            current_hour = hours[i]
            air = current_hour['airTemperature']
            hum = current_hour['humidity']
            time = current_hour['time']
            self.air_point[i] = air['noaa']
            self.hum_point[i] = hum['noaa']
            self.time_point[i] = time[:-9]

    def transformation(self):
        self.containing = 'дата/время;температура;влажность'
        for i in range(0, len(self.air_point)):
            self.containing = self.containing + f"\n{self.time_point[i]};{self.air_point[i]};{self.hum_point[i]}"
        return self.containing

    def create_name(self):
        self.api.lat = str(self.api.lat)
        self.api.lng = str(self.api.lng)
        self.api.lat = self.api.lat.replace('.', '')
        self.api.lng = self.api.lng.replace('.', '')
        self.api.start = self.api.start.replace('-', '')
        self.api.end = self.api.end.replace('-', '')
        self.name_file = f'{self.api.lat} {self.api.lng} {self.api.start}-{self.api.end}'
        return self.name_file

    def record(self):
        with open(f'{self.name_file}.csv', 'w') as f:
            f.write(self.containing)
            pass
        return 'успех'