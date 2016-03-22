#!/usr/bin/env python
# Years till 100
import sys
import optparse # <== This script imports the optparse package in order to make use of the class OptionParser

# The OptionParse class will allow you to add options to your script and it will generate a help option based on the options you provide. In this example, we are adding two options: -n (or --name) and -a (or --age)

parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your Name') # <== The first parameter to add_option is the short option and the 2nd is the long option, it is quite common in the Unix & Linux environment to add a short and long version of an option The next optional parameters to the add_option function are dest=, which is the variable name created, help=, which is the help text generated and type=, which gives the type for the variable. By default the type is string, but for age, we want to make it int

parser.add_option('-a', '--age', dest='age', help='Your Age', type=int)

(options, args) = parser.parse_args() # <== we call the parse_args function, which will return an options object and an args list object. We can access the variables defined in "dest=" when adding options on the options object returned. So it will have two options, options.name and options.age. If one of the variables wasn't passed in, we can check by using the "if variableName is None" condition

if options.name is None:
    options.name = raw_input('Enter Name:')

if options.age is None:
    options.age = int(raw_input('Enter Age:'))

sayHello = 'Hello ' + options.name + ','

if options.age == 100:
    sayAge = 'You are already 100 years old!'
elif options.age < 100:
    sayAge = 'You will be 100 in ' + str(100 - options.age) + ' years!'
else:
    sayAge = 'You turned 100 ' + str(options.age - 100) + ' years ago!'

print sayHello, sayAge