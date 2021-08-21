'''
You are given the dimensions MxN and elements of a matrix. If the matrix is not square, then convert it into a square matrix by
assuming 1 in yhr place of all missing values. Then find the sum S of all left diagonal elements which are repeated more than
X times (X is a given integer) elsewhere in the matrix. The left diagonal is the diagonal which runs from top left to bottom right
of the matrix.

If none of the diagonal elements are repeated more than X times elsewhere in the matrix, then print "0" as the output.

Constraints:
1 <= M <= 10
1 <= N <= 10
X >= 1

Sample Input1:
2 3
1 2 3
4 5 6
2

Sample Output1:
0

Explanation:
Given matrix is
1 2 3
4 5 6

Convert it into
