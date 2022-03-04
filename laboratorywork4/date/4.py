import datetime
#1 day-86400 seconds
def difsec(data1,data2):
    timedif=data2-data1
    return timedif.days*86400+timedif.seconds
date1=datetime.datetime(2021,3,4)
date2=datetime.datetime.now()
print(difsec(date1,date2))