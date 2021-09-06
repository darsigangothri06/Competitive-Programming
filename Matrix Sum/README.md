You are given the dimensions MxN and elements of a matrix. If the matrix is not square, then convert it into a square matrix by assuming 1 in the place of all missing values.

```
Then find the sum S of all left diagonal elements which are repeated more than X times (X is a given integer) elsewhere in the matrix. The left diagonal is the diagonal which runs from top left to bottom right of the matrix.

If none of the diagonal elements are repeated more than X times elsewhere in the matrix, then print "0" as the output.
```

#### Constraints:

```
1 <= M <= 10
1 <= N <= 10
X >= 1
```

#### Sample Input1:

```
2 3
1 2 3
4 5 6
2
```

#### Sample Output1:

```
0
```

Explanation:
Given matrix is

```
1 2 3
4 5 6
```

Convert it into a square matrix:

```
1 2 3
4 5 6
1 1 1
```

Diagonal elements are 1,5 & 1 and X = 2, for an element to get added to sum, it should appear atleast thrice outside the diagonal only 2 times in the matrix outside the diagonal, 1 should not be added to calculate sum. 5 does not appear elsewhere and is therefore not added to sum.

#### Sample Input 2

```
3 2
4 5
5 5
4 6
1
```

#### Sample Output 2

```
6
```

#### Explanation 2

```
Given matrix is
4 5
5 5
4 6
```

Convert it into a square matrix

```
4 5 1
4 5 1
4 6 1

Diagonal elements are 4,5 & 1 and X = 1. Since X = 1 and 1 is repeated twice 
elsewhere in the matrix, 1 gets included in diagonal, 5 also gets included in sum.
Since 4 appears only once, 4 is ignored. So sum = 5 + 1 = 6 which is output
```

