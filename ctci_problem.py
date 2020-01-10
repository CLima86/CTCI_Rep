# Problem 4 Chapter 4. Checking to see if the binary tree is balanced with a function.
def check_height(root):
	if root is None:
		return [True, 0]
	[left_balanced, left_height] = check_height(root.left)
	[right_balanced, right_height] = check_height(root.right)
	return [left_balanced and right_balanced and abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)]

def is_balanced(root):
	"""
	For the purposes of this problem, we may assume that a
	balanced tree is one such that the height of the nodes of each sub-tree
	never differ by a factor of more than 1.
	"""
	return check_height(root)[0]




### COMPUTE THE NTH FIBONACCI NUMBER: RECURSIVE ALG. ###

def F_n(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return (F_n(i-1) + F_n(i-2))
print(F_n(25))
print("\nRecursive Implementation.")

### ZERO MATRIX PROBLEM ###
class Solution:
	# @param matrix, a list of lists of integers
	# RETURN MOTHING, MODIFY matrix IN PLACE.
	def setZeroes(self, matrix):
		# Empty matrix
		if len(matrix) == 0 or len(matrix[0]) == 0: return
		row = [False] * len(matrix)
		column = [False] * len(matrix[0])
		# Record the rows and columns with element(s) being zero.
		for rowIndex in xrange(len(matrix)):
			for colIndex in xrange(len(matrix[0])):
				if matrix[rowIndex][colIndex] == 0:
					row[rowIndex] = True
					column[colIndex] = True
		# Set the qualified entire row(s) and column(s) to zero.
		for rowIndex in xrange(len(matrix)):
			for colIndex in xrange(len(matrix[0])):
				if row[rowIndex] == True or column[colIndex] == True:
					matrix[rowIndex][colIndex] = 0

		return Solution
