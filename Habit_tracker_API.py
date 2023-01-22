import datetime as dt
import requests

# END_POINT = "https://pixe.la/v1/users"
# graph_url = "https://pixe.la/v1/users/abdulhaseeb/graphs"
TOKEN = "34lkj23jhd39c345v"
USERNAME = "abdulhaseeb"
user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_data = {
    "id": "graph1",
    "name": "Code Habit",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
date = dt.datetime
now = date.now()
current_date = now.strftime("%Y%m%d")


Posting_pixel = 'https://pixe.la/v1/users/abdulhaseeb/graphs/graph1'
update = {
    "date": current_date,
    "quantity": input("Enter minutes:"),
}
response = requests.post(url=Posting_pixel, json=update, headers=headers)
print(response.text)
