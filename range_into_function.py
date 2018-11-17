def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i]
    return x

# This code doesn't work
# print(my_function(range(0, 3)))
