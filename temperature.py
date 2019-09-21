import requests
import json

# session=requests.Session()
a=input()
response = requests.post(
    url=f'https://api.openweathermap.org/data/2.5/weather?q={a}',
    params={'appid':'5d1c5370369029f2d3d9274729db73b2'},
)
data = response.json()
with open ('weather.txt','wt') as f:
    json.dump(data,f)

with open('weather.txt','rt') as f:
    new_obj=json.load(f)
lst=(new_obj['main']['temp'])
print('Temperature:',lst-273.15,'C')