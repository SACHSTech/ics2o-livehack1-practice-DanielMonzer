'''
Write a program that lets you enter a number of hours, and that converts it to days and hours. For example, 111 hours = 4 days and 15 hours. (Hint: use the modulus operator).
'''

hours = float(input("Number of hours: "))
days = hours//24
hours2 = hours%24

print(hours,"hours =",int(days),"day(s) and",hours2,"hours")