# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
print(x)
x.append(4)
print(x)
print("---")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
print(x)
x.extend(y)
print(x)
print("---")

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
print(x)
x.remove(8) 
# OR
# x.pop(-2) or x.pop(4)
# OR
# del x[4] or del x[-2]
print(x)
print("---")

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
print(x)
x.insert(-1, 99)
print(x)
print("---")

# Print the length of list x
# YOUR CODE HERE 
print(len(x))
print("---")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i * 10)