'''
Write a program that lets you enter a number of minutes, and that will calculate
the number of days, hours and minutes that represents (Hint: use the modulus operator).
'''
'''
minutes = float(input("Number of minutes: "))
days = minutes//1440
hours = minutes/60
minutes2 = minutes%60

print(minutes,"minutes =",int(days),"days,",int(hours),"hours and",minutes2,"minutes")
'''

minute = float(input("Enter number of minutes: "))

day = minute // (1440)
minute = minute % (1440)

hour = minute // 60
minute = minute % 60

minutes = minute // 1
minute = minute % 1
print(int(day),"day(s),",int(hour),"hour(s) and",minutes,"minute(s)")
