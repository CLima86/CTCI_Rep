"""
Prints the number of calls of a recursive Fibonacci
function with problem sizes that double.
"""
import math
from math import *
import numpy as np
import random
from collections import *
from collections import Counter
def fib(n, counter):
	##Count the number of calls of the fibonacci function.##
	counter.increment()
	if n < 3:
		return 1
	else:
		return fib(n - 1, counter) + fib(n - 2, counter)
	problemSize = 2
	print("%12s%15s" % ("ProblemSize", "Calls"))
	for count in range(5):
		counter = Counter()

		# The start of the algorithm
		fib(problemSize, counter)
		# End of the algorithm
		print("%12s%15s" % (problemSize, counter))
		problemSize *= 2


# Insertion Sort Algorithm #
a = []
for i in range(20):
	a.append(random.randrange(1, 100, 1))
	a.sort()
	print(a)