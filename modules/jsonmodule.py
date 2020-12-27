#!/usr/bin/python3


import json


employee_data='''
{
"people": [
{
"name" : "saurav",
"email": ["santu@gmail.com", "sauravkr@gmail.com"],
"gender": "male"
}
]

}

'''

print(employee_data)

data=json.loads(employee_data)


print(data)
