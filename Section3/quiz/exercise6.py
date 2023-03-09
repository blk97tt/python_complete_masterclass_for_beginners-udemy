# Considering the following string: my_string = "a0:12:90:00:80:43"
# Write code in between the parentheses of the print() function that will return a list consisting of the elements of this string which are 
# delimited by a colon, using a string-specific method.

my_string = "a0:12:90:00:80:43"

print(my_string.split(':'))