#!/usr/bin/env python
# This is some secure program that uses security

# Remember that the spacing is very important in the if statement
# The indented lines of code after the if condition will run if the condition is true. If the condition is false and there is an else section, then the indented code after the else section will run

import sys

validPassword = 'secret' #this is our password

inputPassword = raw_input('Please Enter Password: ') # <== This will display the string given as a parameter to the function and then wait for the user to type input and hit enter. The input is returned by the function into the variable "inputPassword"

if inputPassword == validPassword:
	print 'You have access!'
else:
	print 'Access denied!'
	sys.exit(0) # <== Another thing new to you in this script is the sys.exit function, which is used to exit a python script. The zero as the parameter to sys.exit represents the return status of the script process

print 'Welcome!'
