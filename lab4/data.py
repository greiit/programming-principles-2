#1
from datetime import datetime, timedelta
days_substract = timedelta(days = 5)
timeSubstracted = datetime.now() - days_substract
print(timeSubstracted)


#2
from datetime import date, timedelta
today = date.today() 
oneday = timedelta(days = 1)
tomorrow = today + oneday
yesterday = today - oneday
print(today, tomorrow, yesterday)

#3
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M"))

#4
import datetime
d1 = datetime.datetime(2023, 2, 12, 2, 25, 50, 13)
d2 = datetime.datetime(2023, 2, 12, 2, 22, 12, 12)
print((d1 - d2).seconds)