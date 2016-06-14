import numpy

from fib import fibonacci
from sort import bubble

print(fibonacci(9))
my_matrix = numpy.matrix('1 2; 3 4')
print(my_matrix.getI() * my_matrix)
my_list = [12, 5, 13, 8, 9, 65]
my_new_list = bubble(my_list)
for index in range(1, 6):
    if my_new_list[index] < my_new_list[index - 1]:
        print("failure")
print("bye")
