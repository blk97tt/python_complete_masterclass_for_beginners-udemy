# Considering the tuple below, write a slice on line 3 using positive indexes and a step that will extract the elements 'Love' and 'SQL'.

# my_tuple = (101, [], 10.1, 1.01, 'Love', 'Python', 'Java', 'C++', 'C#', 'SQL', 0, 0.1, (80,))

my_tuple = (101, [], 10.1, 1.01, 'Love', 'Python', 'Java', 'C++', 'C#', 'SQL', 0, 0.1, (80,))

x = my_tuple[4::5]

print(x)