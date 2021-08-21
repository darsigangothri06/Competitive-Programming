Given a number K and string str of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of str at most K times.

##### Example 1:

```
Input:
K = 4
str = "1234567"
Output:
7654321
Explanation:
Three swaps can make the input 1234567 to 7654321, 
swapping 1 with 7, 2 with 6 and finally 3 with 5
```

##### Example 2:

```
Input:
K = 3
str = "3435335"
Output:
5543333
Explanation:
Three swaps can make the input 3435335 to 5543333, 
swapping 3 with 5, 4 with 5 and finally 3 with 4
```

 

Expected Time Complexity: O(n!/(n-k)!) , where n = length of input string

Expected Auxiliary Space: O(n)

```
Constraints:
1 ≤ |str| ≤ 30
1 ≤ K ≤ 10
```

