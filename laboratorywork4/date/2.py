import datetime
from datetime import timedelta
x=datetime.datetime.now()-timedelta(1)
print("Yesterday:"+" "+str(x))
y=datetime.datetime.now()
print("Today:"+" "+str(y))
z=datetime.datetime.now()+timedelta(1)
print("Tomorrow:"+" "+str(z))