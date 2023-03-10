# Calculate (without using a calculator or the Python interpreter) the value returned by the following mathematical expression and write the result on line 1 (where result = ).

# int(6 % 5 + 9 - 2 - 4 ** 2 / 2)

# Then, add the proper logical operator between bool(result) and (7 + 2) == (3 ** 2) in order for x to be evaluated as boolean True.

result = int(6 % 5 + 9 - 2 - 4 ** 2 / 2)

x = bool(result) or (7 + 2) == (3 ** 2)

print(x)