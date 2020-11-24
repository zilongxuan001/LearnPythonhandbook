from datetime import datetime,timedleta
today = datetime.now()
print('Today is ' + str(today))

# timedelta is used to define a period of time
one_day =timedelta(days=1)
yesterday = today-one_day
print('Yesterday was: ' + str(yesterday))
