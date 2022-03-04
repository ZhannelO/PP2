import datetime
x = datetime.datetime.now()
k=x.strftime("%Y-%m-%d %H:%M:%S") #strftime-takes one parameter and convert into string (table of the parameters)
print(k)