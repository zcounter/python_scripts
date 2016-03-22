#!/usr/bin/env python
# Version 2.0
# Years till 100

# With this script, you do input in several ways. You can give the name and age on the command line, you can give just the name on the command line and read the age from user input, or you can give nothing on the command line and read name and age from user input

import sys

if len(sys.argv) > 1: # <== len($), will return the length (the number of items) of an object
	name = sys.argv[1]
else:
	name = raw_input('Enter Name:') # <== If the prompt argument is present (referring to raw_input function), it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

if len(sys.argv) > 2:
	age = int(sys.argv[2]) # <== When reading from user input to a number (integer) variable, you must use the int() cast just like you do for reading sys.argv. 
else:
	age = int(raw_input('Enter Age:'))

sayHello = 'Hello ' + name + ','

if age == 100:
	sayAge = 'You are already 100 years old!'
elif age < 100: # <== This script also introduces a new keyword, elif this is the "else if" of python. Notice that our if conditions now have 3 checks, if the age is 100, if the age is less than 100, and everything else (age > 100). We could have put elif age > 100 in place of the else keyword, but they would do the same thing in this situation

	sayAge = 'You will be 100 in ' + str(100 - age) + ' years!' # <== Also, when appending to a string with the + operator, you must cast any int value (such as "100 - age") to a string with the str() cast
	
else:
	sayAge = 'You turned 100 ' + str(age - 100) + ' years ago!'

print sayHello, sayAge

## NOTES: We introduced two new built-in functions into the script. These functions are built into python and are always available. They are len($) and raw_input().
## The int() function will return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x is a number, it can be a plain integer, a long integer, or a floating point number. If x is floating point, the conversion truncates towards zero. If the argument is outside the integer range, the function returns a long object instead.
## https://docs.python.org/2/library/functions.html