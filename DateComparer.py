print("This program gathers 2 dates, and displays which date comes first.")
print("Gathering the first date...")
year1 = input("Enter the year: ")
month1 = input("Enter the month")
day1 = input("Enter the day: ")
print("Gathering the second date...")
year2 = input("Enter the year: ")
month2 = input("Enter the month: ")
day2 = input("Enter the day: ")

date1 = "{0}/{1}/{2}".format(year1, month1, day1)
date2 = "{0}/{1}/{2}".format(year2, month2, day2)
print("The dates are :\n{}\n{}".format(date1,date2))
print('\n\n')

if (year1 < year2):
    print("{} comes first".format(date1))
else:
    if(year2 <= year1):
        print("{} comes second".format(date2))
if(month1 < month2):
    print("{} comes first".format(date1))
else:
    if(month2 < month1):
        print("{} comes second".format(date2))
if(day1 < day2):
    print("{} comes first".format(date1))
else:
    if(day2 < day1):
        print("{} comes second".format(date2))
    else:
        print("Both dates are the same")
