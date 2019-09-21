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
lst1=(new_obj['main']['pressure'])
print('Pressure:',lst1)
lst2=(new_obj['wind']['speed'])
print('The speed of the wind is:',lst2)
lst3=(new_obj['wind']['deg'])
if lst3>0 and lst3<90:
    print('The wind is from the north-east')
elif lst3==90:
    print('The wind is from the east')
elif lst3>90 and lst3<180:
    print('The wind is from the south-east')
elif lst3==180:
    print('The wind is from the south')
elif lst3>180 and lst3<270:
    print('The wind is from the south-west')
elif lst3==270:
    print('The wind is from the west')
elif lst3>270 and lst3<360:
    print('The wind is from the north-west')
else:
    print('The wind is from the nord')