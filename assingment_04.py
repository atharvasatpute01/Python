# *Hands-on Assignment (30 Marks)*

# Create a Student Information System that:

# Input : Student Name, College Name, Course, City.

# Display : Student Name, First Character of Name, Last Character of Name, Length of Name, Whether "AI" exists in the Course name, Data type of each input using type().


#----------------------------
# Student Information System
#----------------------------

student_name = input("Enter Student Name : ")
college_name = input("Enter College Name : ")
course = input("Enter Course : ")
city = input("Enter City : ")

print("\n==========================")
print("STUDENT INFORMATION SYSTEM")
print("==========================")


print("\n------ Student Details ------")
print("-----------------------------")
print("Student Name : ",student_name)
print("College Name : ",college_name)
print("Course       : ",course)
print("City         : ",city)

print("\nFirst Character of Name   : ",student_name[0])
print("Last Character of Name    : ",student_name[-1])
print("Length of name            : ",len(student_name))
print("Contains AI               : ","AI" in course)

print("\n------ Data Types ------")
print("------------------------")
print("Student Name :",type(student_name))
print("College Name :",type(college_name))
print("Course       :",type(course))
print("City         :",type(city))




# Sample Output :

# Enter Student Name : Atharva
# Enter College : ABC College
# Enter Course : AI and Data Science
# Enter City : Pune

# Student Details
# ---------------
# Name             : Atharva
# College          : ABC College
# Course           : AI and Data Science
# City             : Pune

# First Character  : A
# Last Character   : a
# Length of Name   : 7
# Contains AI      : True

# Data Types
# ----------
# Name    : <class 'str'>
# College : <class 'str'>
# Course  : <class 'str'>
# City    : <class 'str'>