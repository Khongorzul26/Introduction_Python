#Lecture code for week 2


my_string = "Zulaa"
type(my_string)

my_int = -15
type(my_int)

my_float = 15.78
type(my_float)

my_bool = False #True
type(my_bool)

import datetime
today = datetime.date.today()
today.year
today.month
today.day

datetime.datetime.strptime("2017-01-22","- %M - %D") #Convert string to datetime
today.strftime,("%Y - %M - %")
