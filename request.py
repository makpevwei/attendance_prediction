import requests
import json


# url = 'http://localhost:5000/results'
url = 'https://attendance-flask.herokuapp.com/results'
r = requests.post(url,json={'Gender':1,'Weather Condition':1,'Service Day':4,'Service Time':2, 'Public Holiday':1, 'SMS Notification':1,
       'Email Notification':1, 'SMS Reminder':1, 'Email Reminder':1,
       'Free Transportation':1, 'External Speaker':1, 'Church Venue':1,
       'Outreach Program':1,'Love Feast':1})

print("Status code: ", r.status_code)

print(r.json())
