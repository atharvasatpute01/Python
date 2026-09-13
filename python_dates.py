# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.


# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()

print(x)


# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.




# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))




# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)




# The strftime() Method

# The datetime object has a method for formatting data objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# Example:

# Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))