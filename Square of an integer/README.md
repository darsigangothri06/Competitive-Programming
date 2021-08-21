You are given two numbers M and N such that M <= N. Your task is to find the count of every integer K in the interval of numbers between M and N (inclusive) that satisfies the following conditions:

```
1. K is the square of an integer.
2. In the number K, every digit holds the following property: d1 < d2 > d3 < d4 and so on, where di represents a digit ok K.
```

Input:

The first line of input contains an integer M.

The second line of input contains an integer N.

Output:

Print the count of numbers in the given interval that satisfies the given requirements.

```
Constraints:
1 <= M <= N <= (10)^11
```

##### Example 1:

```
Input:
121
121
Output:
1

Explanation: 
There is one number in the given interval - 121
11^2 = 121
1 < 2 > 1
```

##### Example 2:

```
Input:
40
70
Output:
1  (49)
```

