#!/usr/bin/env python
# Years till 100
# Source: http://www.dreamsyssoft.com/python-scripting-tutorial/variables-tutorial.php

import sys # <== In order to access the command line arguments in a python script, you must first use the import keyword and import the sys package. The arguments can then be accessed by the sys.argv variable, which is an array containing the command line arguments.

name = sys.argv[1] # <== To access the values in an array, you use the [] operator. For instance, to access the first item in the command line, you would access sys.argv[0]. Which would return the name of the script being run.
age = int(sys.argv[2]) # <== The arguments passed to the script are stored in the array starting with index 1. Let's make our script take the 2 arguments name and age which will be indexes 1 and 2 respectively. We can assign these values to a named variable and then print them.
diff = 100 - age # <== We will create a 3rd variable called "diff", which will hold the number of years until you will be 100 years old.
# One more thing to note, when setting the variable "age", we must first tell python that the incoming sys.argv variable is an integer, so we use the int keyword to typecast the string sys.argv[2] to an int.

print 'Hello',name + ', you will be 100 in', diff, 'years!'

