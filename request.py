import requests
import json


# url = 'http://localhost:5000/results'
url = 'https://attendance-prediction.herokuapp.com/results'
r = requests.post(url,json={'Gender':0,'Weather Condition':1,'Service Day':4,
       'Service Time':2, 'Public Holiday':1, 'SMS Notification':0,
       'Email Notification':0, 'SMS Reminder':1, 'Email Reminder':0,
       'Free Transportation':1, 'External Speaker':0, 'Church Venue':1,
       'Outreach Program':0, 'Celebration':1, 'Love Feast':0,})

print("Status code: ", r.status_code)

print(r.json())
