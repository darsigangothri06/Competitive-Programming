from itertools import chain
given_matrix = [[1,2,3,4],[1,5,3,6],[8,9,10,4],[2,5,8,11]]
n = int(input("Enter the value of n: "))
all_matrix_elements = list(chain(*given_matrix))
# Removing duplicates from the matrix elements
matrix_elements = set(all_matrix_elements)
# sorting the elements
ordered_matrix_elements = sorted(list(matrix_elements),reverse = True)
# our elements are distinct and in descending order
# we will have our nth maxima in (n-1)th index
print("The given matrix is {0}".format(given_matrix))
print("{0} maxima is {1}".format(n,ordered_matrix_elements[n-1]))
