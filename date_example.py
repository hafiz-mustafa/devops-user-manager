from datetime import datetime

myDate = datetime.now()


hh = myDate.hour
mm = myDate.minute
ss = myDate.second
day = myDate.day
month = myDate.month
year = myDate.year
wd = myDate.weekday()
name = "Ali"


print(f"Time Now is : {hh} : {mm} : {ss}")

if(wd == 5):
    print("happy saturday")
print(wd)

