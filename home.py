import numpy

from fib import fibonacci
from sort import bubble

print(fibonacci(9))
my_matrix = numpy.matrix('1 2; 3 4')
print(my_matrix.getI() * my_matrix)
my_list = [12, 5, 13, 8, 99, 65, 1]
my_list = bubble(my_list)
for index in range(1, 6):
    if my_list[index] < my_list[index - 1]:
        print("failure")
print("bye")
