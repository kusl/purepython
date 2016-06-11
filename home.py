import numpy

from fib import fibonacci
from sort import bubble

print(fibonacci(9))
my_matrix = numpy.matrix('1 2; 3 4')
print(my_matrix.getI() * my_matrix)
my_list = [12, 5, 13, 8, 9, 65]
print(bubble(my_list))
print("bye")
