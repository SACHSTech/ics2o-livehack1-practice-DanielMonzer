'''
Write a program that gets the temperature(celsius) and wind speed (km/h) then computes and outputs the windchill factor.
equation where T is temperature and V is windspeed.

For example, when the temperature (in Celsius) is 2 degrees, wind speed is 7 km/h, the wind chill is -0.08 Degrees Celsius.
'''

temperature = float(input("What is the temperature in celsius?: "))
wind_speed = float(input("What is the windspeed in km/h?: "))

windchill = 13.12 + (0.6215 * temperature) - (11.37 * wind_speed**0.16) + (0.3965 * temperature * wind_speed**0.16)

print("The windchill is",windchill,"Degrees Celsius")