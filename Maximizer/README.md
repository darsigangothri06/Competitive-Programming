Three people are playing a game in which one person is selected first, the second person gives the selected person a number N, and the third person also gives the selected person a number M.



The selected person has to maximize the number given by the second person in a way that:

```
1. (S)he can maximize the number given by the second person only by swapping the adjacent two digits of the number.
2. The number that the third person gives is the maximum number of swaps allowed.
```

Find the maximum number that the selected person can achieve

##### Input Specification:
```
input1 : The number N
input2: Thenumber M
Note: The number N is given in the string format as input.
```

##### Output Specification:

```
The maximum number the person can achieve in M swaps.
```

##### Example 1:

```
input1: 1234
input2: 2

Output:
3124

Explanation:
Here, the number can be swapped as 1234 -> 1324 -> 3124
```

##### Example 2:

```
input1: 1123
input2: 1

Output: 1213
Explanation:
Here, the number can be swapped as 1123 -> 1213
```