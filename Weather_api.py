import requests
import pandas as pd
from twilio.rest import Client

account_sid = 'ACfd5bbcb573babf4806e355959e3d856a'
auth_token = '4dd596fea0d3faae7f493e62b5d3aae1'
dict = {
    'key':'963dfe602c7140c78ab150820231901',
    "q": "Sargodha"
}
data_lsit_loc = ['name', 'region', 'country']
data_list_current = ['temp_c', 'temp_f', 'wind_degree', 'wind_dir', 'feelslike_c', 'last_updated']
data_dict = {
    'KEY': [],
    'VALUES': []
}
client = Client(account_sid, auth_token)
data = requests.get("http://api.weatherapi.com/v1/forecast.json?&days=2", params=(dict))
data.raise_for_status()
weather = data.json()
for item in data_lsit_loc:
    data_dict['KEY'].append(item)
    data_dict['VALUES'].append(weather["location"][item])

data_dict['KEY'].append('text')
data_dict['VALUES'].append(weather["current"]['condition']['text'])

for item in data_list_current:
    data_dict['KEY'].append(item)
    data_dict['VALUES'].append(weather["current"][item])

df = pd.DataFrame(data_dict)
df_without_index = df.to_string(index=False)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=str(df_without_index),
    to='whatsapp:+923020111017'
)
print(message.status)
