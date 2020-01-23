from datetime import datetime
from datetime import timezone
'''
expectedFormat = '%Y-%m-%d %H:%M%S'
dt = datetime.strptime(date, expectedFormat)
'''
YearV = False
#year
while YearV == False:
    print("Please input a year: ")
    year = input()
    #Must be between 1900-2020
    try:
       year = int(year)
    except Exception as e:
       print("That's not an year!" + str(e))
       year = False
       
    if isinstance(year,int):
        #year = int(year)
        if year >= 1900 and year <= 2020:
            year = str(year)
            YearV = True
        else:
            print("Year Not Valid!")
            yearV = False
MonthV = False
#Month
while MonthV == False:        
    print("Please input month: ")
    month = input()
    try:
       month = int(month)
    except ValueError:
       month = month

    if isinstance(month, int):
        if month >= 1 and month <= 9:
            month = str(month)
            month = '0' + month
        elif month > 9 and month <= 12:
            month = str(month)
            monthV = True
        else:
            print("Month not valid")
            monthV = False
    else:
        if len(month) > 4:
            try:
                d = datetime.strptime(month, '%B')
                month = (d.strftime('%m'))
                MonthV = True
            except Exception as e:
                print('Month is spelled wrong!' + str(e))
                MonthV = False
        else:
            try:
                d = datetime.strptime(month, '%b')
                month = (d.strftime('%m'))
                MonthV = True
            except Exception as e:
                print('Abreviation is spelled wrong!'+ str(e))
                MonthV = False
    
#days
DaysV = False
#Not all months have the sme days
while DaysV == False:
    print("Please input day: ")
    day = input()
    try:
        day = int(day)
    except :
        print('not converteted to number')
    if day >= 1 and day < 10:
        day = '0' + str(day)
        DaysV = True
    elif day > 9 and day <= 31:
        day = str(day)
        DaysV = True
    try:
        checkDate = datetime(int(year),int(month),int(day))
    except Exception as e:
        DaysV = False
        print('not valid day in this month' + str(e))

#Hours
HoursV = False
while HoursV == False:
    print("Please input the hour in 24 hour time: ")
    hour = input()
    hour = int(hour)
    try:
        if hour >= 0 and hour < 24:
            if hour < 10:
                hour = '0' + str(hour)
                HoursV = True
            else:
                hour = str(hour)
                HoursV = True
        else:
            HoursV = False
            print('Not a valid hour!')
    except Exception as e:
        print('Hour not an integer' + str(e))

#Minute
MinuteV = False
while MinuteV == False:    
    print("Please input the minute: ")
    minute = input()
    minute = int(minute)
    try:
        if minute >= 0 and minute < 60:
            if minute < 10:
                minute = '0' + str(minute)
                MinuteV = True
            else:
                minute = str(minute)
                MinuteV = True
        else:
            MinuteV = False
            print('Minute entered is not valid!')
    except Exception as e:
        print('Minute not an integer' + str(e))

#Seconds
SecondsV = False
while SecondsV == False:   
    print("Please input the second: ")
    second = input()
    second = int(second)
    try:
        if second >= 0 and second < 60:
            if second < 10:
                second = '0' + str(second)
                SecondsV = True
            else:
                second = str(second)
                SecondsV = True
        else:
            SecondsV = False
            print('Seconds entered not valid!')
    except Exception as e:
        print('Second not an integer' + str(e))

combinedDT= year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second

expectedFormat = '%Y-%m-%d %H:%M:%S'
dt = datetime.strptime(combinedDT, expectedFormat)
print(dt)

UnixTime = dt.replace(tzinfo=timezone.utc).timestamp()
print(UnixTime)    
t =t 
