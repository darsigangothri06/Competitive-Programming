Given two integers m & n, find the number of possible sequences of length n such that each of the next element is greater than or equal to twice of the previous element but less than or equal to m.

##### Example 1:

```
Input:
m = 10, n = 4
Output:
4
Explaination: 
There should be n elements and 
value of last element should be at-most m. 
The sequences are {1, 2, 4, 8}, {1, 2, 4, 9}, {1, 2, 4, 10}, {1, 2, 5, 10}.
```

##### Example 2:

```
Input: m = 5, n = 2
Output: 6
Explaination: The sequences are {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}.
```

Expected Time Complexity: O(m*n)

Expected Auxiliary Space: O(1)

##### Constraints:

```
1 ≤ m, n ≤ 100
```

