# from _datetime import datetime

# Print data
# p_name =("John Smith")
# p_age = (20)
# p_User = ('New User')
# print(p_name,p_age,p_User)

# Taking input (Type conversion)
# name = input("What is ur name ? ")
# print("Hello " + name)
# birth_year = input("What is ur birth year : ")
# age = 2023 - int(birth_year)
# print("Your age :"+ str(age))

# variable
# first = input("Enter first number ")
# second = input("Enter Second number ")
#  sum = float(first)+float(second)
#  print("Sum:" +str(sum))25
#  print( sum)
#  Or
# first = float(input("Enter first number "))
# second =float( input("Enter Second number "))
# sum = first + second
# print( "Sum : " +str( sum))


# Strings ( is a oject) using methods to a string object

# course = 'Python For Beginners'
# print(course)
# print(course.replace('Python','Java'))
#  # in operator to  find Python in course string object
# print('Python' in course)
# print(course.find('P'))
#  print(course.upper())
# print(course.lower())

# Arithmetic operators( +-*/)
# x = int(input("enter a number "))
# y = int(input("number to be multiplied by "))
# print( x * y)

# operatorprededence
# where multiplication and division get higher precedent
# where which need to be evaluted first then need to be mentioned within ( )
# x = 10
# x +=3
# print(x)

# x =  (10+3)*2
# print(x)

# comparison operator ( > < <= >= == != )
#
# x = 3>2
# print(x)
#
# x = 3>=2
# print(x)
#
# x = 3==2
# print(x)
#
# x = 3!=2
# print(x)

# Logical operator
#  and  (both)which returns true if both expression return true
#  or   (at least one) which returns true if atleast one is true
#  not (Inverses ) which inverses any value we give


# And
# price =25
# print(price >10 and price <30)
# # or
# price = 55
# print(price >10 or price <30)
# # Not
# price = 5
# print(not price >10)

# if Statements

# temparature = 34 #manual Input prediscribed input
# temparature =int(input("enter your weather temperature ")) #take input from automatically
#
# if temparature >= 32:
#     print ("Its a hot day ")
#     print ("Drink plenty of water ")
# elif temparature >= 20:
#     print("it a beautiful pleasant day  ")
# elif temparature >= 10:
#     print("it a bit cold day  ")
# else:
#     print ( "Its a Cold day , have a Hot Coffee ")
# print( " " )
# print( "Done .....thank u " )

#find the weight if kg and lbs(pounds) exercise

# weight = float(input("enter Your weight: "))# int if the data is integer or use float for decimals
# unit = input ("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("weight in (L)bs " + str(converted) )
# else:
#     converted = weight * 0.45
#     print("weight in (K)g " + str(converted))
#

# While Loops

# i = 1
# while i<=10:   #print 1-10 using loops
#     print(i)
#     i=i+1

# i = 1
# while i<=10:   #print *  using loops
#     print(i * '*')  # multiplying string using multpling with i value
#     i=i+1

#Primitive/basic types

#   1           Interger
#   1.36        Float
#   'a'         String
#  True/False   Boolean

# Complex types  usefull in building real application
#
# Lists ---  we use list when ever we want represent a list of objects ,ie numbers ,names etc
#

# names =["Abhishek","Akshay","Lokanatha","Shobha"]
# names[2] ="logu" #renaming / correcting
# print(names[1])    #print only names to see full list
# print(names)
# print (names[0:2])
# print(names)

# List methods
#
# "a". when we click a dot we get a lot of functions to a Strings where we can add and remove strings

# numbers = [1,2,3,4,5]
# numbers.append(6)      #append is used to add a value at the end
# # numbers.insert(0,2)  # insert is used to add a value at anywhere using a index value and needed to add a object value
# # numbers.remove(3)    # remove is used to remove a index value mentioned within brackets
# #numbers.clear()       #clear is used to clear all the index values
# print(numbers)
# print(1 in numbers)     #this a expression which in operator where this will  return true/false if the 1 is in the numbers
# print(len(numbers))     #len is a builtin function which is used to check the elements in the list

# For Loops

# numbers = [1,2,3,4,5]
# for item in numbers:                   # for loop is used to repated output
#     print(item)
#
# # while loop
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i=i+1

#both used for same output but in for loop it was simple and easy

#The range() Function

#this function is used to gerenrate a sequence of numbers

# numbers = range(5)                  # a range object is a object which can store a sequence of number
# print(numbers)
#
# numbers = range(5)
# for number in numbers:
#     print(number)
#
# numbers = range(5,10)
# for number in numbers:
#     print(number)
#
# numbers = range(5,10,2) # odd numbers with  5 7 9
# for number in numbers:
#     print(number)

# for number in range(5):
#     print(number)

# Tuples
#tuples are kind of list to store a sequence of objects ,
#tuples are imuatable ,we cannot change them once creating them


# numbers =(1,2,3,4,5)
# #numbers[0] = 10 # unable as number value as been assigned and which cannot be rechanged
# print(numbers)
 #most of the time u use only a list , but if the value shouldnot be changed then use tupple.



# first_name = "abhishek"
# last_name = "lokanatha "
# print(first_name.capitalize()+ ' ' + last_name.capitalize()) #capitalize create a cpital first letter of the output
# #     Abhishek Lokanatha this is the output with cpital letters first

# Custom string formatting (string concatination)

# first_name = "abhishek"
# last_name = "lokanatha"

# print("Hello , " + first_name + " " + last_name)
# print("Hello , {} {} " .format(first_name,last_name))  # use .format for ease to get custom format output
# print("Hello , {0} {1}" .format(first_name,last_name))
# output = f'Hello , {first_name} {last_name}'
# print(output)
#                                                                 #Different menthods for same outputs
# same output for above all print formats

# Hello , abhishek lokanatha
# Hello , abhishek lokanatha
# Hello , abhishek lokanatha
# Hello , abhishek lokanatha # output from .f format function


#inputs

# first_name = "abhishek"
# last_name = "lokanatha"
# output = f'hello,{first_name} {last_name}' #here f is mentioned hence that value is taken from stored variable
# print(output)

# outputs

#hello,abhishek lokanatha                      #with (f) ie formating concatinaltion menthod

#hello,{first_name} {last_name}                       #without (f) ie formating concatinaltion menthod

# current_date = datetime.now() # date time now is used take todays date and current time
# print("today is "+ str(current_date))

