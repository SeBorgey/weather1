import copy
import os

var = {'hours': [{'airTemperature': {'noaa': 23.48, 'sg': 23.48}, 'humidity': {'noaa': 35.48, 'sg': 35.48},
                  'time': '2018-07-16T12:00:00+00:00'},
                 {'airTemperature': {'noaa': 23.04, 'sg': 23.04}, 'humidity': {'noaa': 44.76, 'sg': 44.76},
                  'time': '2018-07-16T13:00:00+00:00'},
                 {'airTemperature': {'noaa': 22.59, 'sg': 22.59}, 'humidity': {'noaa': 54.05, 'sg': 54.05},
                  'time': '2018-07-16T14:00:00+00:00'},
                 {'airTemperature': {'noaa': 22.15, 'sg': 22.15}, 'humidity': {'noaa': 63.34, 'sg': 63.34},
                  'time': '2018-07-16T15:00:00+00:00'},
                 {'airTemperature': {'noaa': 20.29, 'sg': 20.29}, 'humidity': {'noaa': 69.1, 'sg': 69.1},
                  'time': '2018-07-16T16:00:00+00:00'},
                 {'airTemperature': {'noaa': 18.43, 'sg': 18.43}, 'humidity': {'noaa': 74.87, 'sg': 74.87},
                  'time': '2018-07-16T17:00:00+00:00'},
                 {'airTemperature': {'noaa': 16.57, 'sg': 16.57}, 'humidity': {'noaa': 80.63, 'sg': 80.63},
                  'time': '2018-07-16T18:00:00+00:00'},
                 {'airTemperature': {'noaa': 16.08, 'sg': 16.08}, 'humidity': {'noaa': 82.43, 'sg': 82.43},
                  'time': '2018-07-16T19:00:00+00:00'},
                 {'airTemperature': {'noaa': 15.59, 'sg': 15.59}, 'humidity': {'noaa': 84.22, 'sg': 84.22},
                  'time': '2018-07-16T20:00:00+00:00'},
                 {'airTemperature': {'noaa': 15.1, 'sg': 15.1}, 'humidity': {'noaa': 86.02, 'sg': 86.02},
                  'time': '2018-07-16T21:00:00+00:00'},
                 {'airTemperature': {'noaa': 14.61, 'sg': 14.61}, 'humidity': {'noaa': 87.81, 'sg': 87.81},
                  'time': '2018-07-16T22:00:00+00:00'},
                 {'airTemperature': {'noaa': 14.12, 'sg': 14.12}, 'humidity': {'noaa': 89.61, 'sg': 89.61},
                  'time': '2018-07-16T23:00:00+00:00'},
                 {'airTemperature': {'noaa': 13.63, 'sg': 13.63}, 'humidity': {'noaa': 91.4, 'sg': 91.4},
                  'time': '2018-07-17T00:00:00+00:00'},
                 {'airTemperature': {'noaa': 15.86, 'sg': 15.86}, 'humidity': {'noaa': 82.31, 'sg': 82.31},
                  'time': '2018-07-17T01:00:00+00:00'},
                 {'airTemperature': {'noaa': 18.09, 'sg': 18.09}, 'humidity': {'noaa': 73.21, 'sg': 73.21},
                  'time': '2018-07-17T02:00:00+00:00'},
                 {'airTemperature': {'noaa': 20.31, 'sg': 20.31}, 'humidity': {'noaa': 64.12, 'sg': 64.12},
                  'time': '2018-07-17T03:00:00+00:00'},
                 {'airTemperature': {'noaa': 21.77, 'sg': 21.77}, 'humidity': {'noaa': 57.79, 'sg': 57.79},
                  'time': '2018-07-17T04:00:00+00:00'},
                 {'airTemperature': {'noaa': 23.23, 'sg': 23.23}, 'humidity': {'noaa': 51.45, 'sg': 51.45},
                  'time': '2018-07-17T05:00:00+00:00'},
                 {'airTemperature': {'noaa': 24.68, 'sg': 24.68}, 'humidity': {'noaa': 45.12, 'sg': 45.12},
                  'time': '2018-07-17T06:00:00+00:00'},
                 {'airTemperature': {'noaa': 25.23, 'sg': 25.23}, 'humidity': {'noaa': 44.2, 'sg': 44.2},
                  'time': '2018-07-17T07:00:00+00:00'},
                 {'airTemperature': {'noaa': 25.77, 'sg': 25.77}, 'humidity': {'noaa': 43.28, 'sg': 43.28},
                  'time': '2018-07-17T08:00:00+00:00'},
                 {'airTemperature': {'noaa': 26.32, 'sg': 26.32}, 'humidity': {'noaa': 42.36, 'sg': 42.36},
                  'time': '2018-07-17T09:00:00+00:00'},
                 {'airTemperature': {'noaa': 26.24, 'sg': 26.24}, 'humidity': {'noaa': 43.64, 'sg': 43.64},
                  'time': '2018-07-17T10:00:00+00:00'},
                 {'airTemperature': {'noaa': 26.15, 'sg': 26.15}, 'humidity': {'noaa': 44.93, 'sg': 44.93},
                  'time': '2018-07-17T11:00:00+00:00'},
                 {'airTemperature': {'noaa': 26.07, 'sg': 26.07}, 'humidity': {'noaa': 46.22, 'sg': 46.22},
                  'time': '2018-07-17T12:00:00+00:00'},
                 {'airTemperature': {'noaa': 24.9, 'sg': 24.9}, 'humidity': {'noaa': 53.24, 'sg': 53.24},
                  'time': '2018-07-17T13:00:00+00:00'},
                 {'airTemperature': {'noaa': 23.72, 'sg': 23.72}, 'humidity': {'noaa': 60.26, 'sg': 60.26},
                  'time': '2018-07-17T14:00:00+00:00'},
                 {'airTemperature': {'noaa': 22.55, 'sg': 22.55}, 'humidity': {'noaa': 67.29, 'sg': 67.29},
                  'time': '2018-07-17T15:00:00+00:00'},
                 {'airTemperature': {'noaa': 20.78, 'sg': 20.78}, 'humidity': {'noaa': 72.76, 'sg': 72.76},
                  'time': '2018-07-17T16:00:00+00:00'},
                 {'airTemperature': {'noaa': 19.02, 'sg': 19.02}, 'humidity': {'noaa': 78.23, 'sg': 78.23},
                  'time': '2018-07-17T17:00:00+00:00'},
                 {'airTemperature': {'noaa': 17.25, 'sg': 17.25}, 'humidity': {'noaa': 83.7, 'sg': 83.7},
                  'time': '2018-07-17T18:00:00+00:00'},
                 {'airTemperature': {'noaa': 16.61, 'sg': 16.61}, 'humidity': {'noaa': 86.41, 'sg': 86.41},
                  'time': '2018-07-17T19:00:00+00:00'},
                 {'airTemperature': {'noaa': 15.97, 'sg': 15.97}, 'humidity': {'noaa': 89.11, 'sg': 89.11},
                  'time': '2018-07-17T20:00:00+00:00'},
                 {'airTemperature': {'noaa': 15.33, 'sg': 15.33}, 'humidity': {'noaa': 91.82, 'sg': 91.82},
                  'time': '2018-07-17T21:00:00+00:00'},
                 {'airTemperature': {'noaa': 15.06, 'sg': 15.06}, 'humidity': {'noaa': 92.67, 'sg': 92.67},
                  'time': '2018-07-17T22:00:00+00:00'},
                 {'airTemperature': {'noaa': 14.8, 'sg': 14.8}, 'humidity': {'noaa': 93.52, 'sg': 93.52},
                  'time': '2018-07-17T23:00:00+00:00'},
                 {'airTemperature': {'noaa': 14.54, 'sg': 14.54}, 'humidity': {'noaa': 94.37, 'sg': 94.37},
                  'time': '2018-07-18T00:00:00+00:00'},
                 {'airTemperature': {'noaa': 16.47, 'sg': 16.47}, 'humidity': {'noaa': 86.86, 'sg': 86.86},
                  'time': '2018-07-18T01:00:00+00:00'},
                 {'airTemperature': {'noaa': 18.4, 'sg': 18.4}, 'humidity': {'noaa': 79.35, 'sg': 79.35},
                  'time': '2018-07-18T02:00:00+00:00'},
                 {'airTemperature': {'noaa': 20.34, 'sg': 20.34}, 'humidity': {'noaa': 71.85, 'sg': 71.85},
                  'time': '2018-07-18T03:00:00+00:00'},
                 {'airTemperature': {'noaa': 21.64, 'sg': 21.64}, 'humidity': {'noaa': 66.2, 'sg': 66.2},
                  'time': '2018-07-18T04:00:00+00:00'},
                 {'airTemperature': {'noaa': 22.95, 'sg': 22.95}, 'humidity': {'noaa': 60.56, 'sg': 60.56},
                  'time': '2018-07-18T05:00:00+00:00'},
                 {'airTemperature': {'noaa': 24.25, 'sg': 24.25}, 'humidity': {'noaa': 54.91, 'sg': 54.91},
                  'time': '2018-07-18T06:00:00+00:00'},
                 {'airTemperature': {'noaa': 24.91, 'sg': 24.91}, 'humidity': {'noaa': 52.5, 'sg': 52.5},
                  'time': '2018-07-18T07:00:00+00:00'},
                 {'airTemperature': {'noaa': 25.58, 'sg': 25.58}, 'humidity': {'noaa': 50.08, 'sg': 50.08},
                  'time': '2018-07-18T08:00:00+00:00'},
                 {'airTemperature': {'noaa': 26.24, 'sg': 26.24}, 'humidity': {'noaa': 47.67, 'sg': 47.67},
                  'time': '2018-07-18T09:00:00+00:00'},
                 {'airTemperature': {'noaa': 25.48, 'sg': 25.48}, 'humidity': {'noaa': 52.05, 'sg': 52.05},
                  'time': '2018-07-18T10:00:00+00:00'},
                 {'airTemperature': {'noaa': 24.71, 'sg': 24.71}, 'humidity': {'noaa': 56.42, 'sg': 56.42},
                  'time': '2018-07-18T11:00:00+00:00'},
                 {'airTemperature': {'noaa': 23.95, 'sg': 23.95}, 'humidity': {'noaa': 60.8, 'sg': 60.8},
                  'time': '2018-07-18T12:00:00+00:00'}],
       'meta': {'cost': 1, 'dailyQuota': 50, 'end': '2018-07-18 12:00', 'lat': 56.85, 'lng': 60.61,
                'params': ['humidity', 'airTemperature'], 'requestCount': 10, 'start': '2018-07-16 12:00'}}
hours = var['hours']
print(hours)


air_point = copy.deepcopy(hours)
hum_point = copy.deepcopy(hours)
time_point = copy.deepcopy(hours)


for i in range(0, len(hours)):
    current_hour = hours[i]
    air = current_hour['airTemperature']
    hum = current_hour['humidity']
    time = current_hour['time']

    air_point[i] = air['noaa']
    hum_point[i] = hum['noaa']
    time_point[i] = time[:-9]
    # print(time_point,air_point,hum_point)

# for i in range(0, len(hours)):
#     print(time_point[i],air_point[i],hum_point[i])
# модуль создания содержимого файла
containing = 'дата/время;температура;влажность'
for i in range(0, len(hours)):
    containing = containing + f"\n{time_point[i]};{air_point[i]};{hum_point[i]}"
print(containing)



p = os.getcwd()
print(p)
c = os.path.split(os.getcwd())
c = os.path.split(c[0])
c = os.path.split(c[0])
print(c[0])
with open(f'{c[0]}\\file.csv', 'w') as f:
    f.write(containing)
    pass