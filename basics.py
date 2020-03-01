import datetime
date = datetime.datetime.now()
nbr = 10
text = "Hello"
print("date is",datetime.datetime.now())
print(nbr,text)

# simple datatypes, int,float,str
x=10
y="10"
z=100

print(x+x)
print(y+y)

# compound datatypes, list
rain = ['today',11,5.5,[1,2,3]]
print(rain)

# dir(str)
# to get the list of methods for str associated with dir

# help(str.upper)
# tells more about the upper method

# print is a func which is not associated to any datatype

# dir(__builtins__)
# list of func in python
# help(hasattr)

list_num = [10,6.7,5]
sum_num = sum(list_num)
list_len = len(list_num)
mean = sum_num / list_len
print(mean)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
x = student_grades.count(10.0)
print(x)

username = "Python3"
x=username.lower()
print(x)
# Integers, Floats, Lists, Dictionaries, Tuples, dir, help
#  Positive/Negative Indexes, Slicing lists
# print("Hi %s, you have %s years of experience." % (name, experience_years))
# name = input("Enter your name: ")
# List Comprehensions Plus if else inline for

# *args > tuple
# **kwargs > dict

#  builtin libraries
# import sys
# sys.builtin_module_names
# import time
# dir(time)

# stanalone libraries
# import os
# sys.prefix > path of lib on mac
# dir(os)

# third party lib