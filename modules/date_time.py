#!/usr/bin/python3


import datetime

print(datetime.date.today())


now= datetime.datetime.today()

other= datetime.datetime(1994,10,20,23,12)

print(now - other)


#d=datetime.date(2019,7,28)

d=datetime.date.today()
#print(d.day)
print(d.weekday())
