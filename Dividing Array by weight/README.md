A box consists of N pieces of stones with each stone having certain weights assigned to it. The task is to manage all stones into two parts such that both parts should have equal weight of stones.

Print "TRUE" if the partition is possible otherwise print "FALSE"

### Example 1

```
Input:
4 - Value of N represents size of Arr
2 - Value of Arr[0], represents weight of 1st stone
9 - Value of Arr[1], represents weight of 2nd stone
3 - Value of Arr[2], represents weight of 3rd stone
4 - Value of Arr[3], represents weight of 4th stone

Output:
TRUE

Explanation:
The stones can be partitioned as {9} and {2,3,4}
```

### Example 2

```
Input:
4 - Value of N represents size of Arr
12 - Value of Arr[0], represents weight of 1st stone
1 - Value of Arr[1], represents weight of 2nd stone
4 - Value of Arr[2], represents weight of 3rd stone
8 - Value of Arr[3], represents weight of 4th stone

Output:
FALSE
```

#### Constraints

```
2 <= N <= 20
1 <= Arr[i] <= 10000
```

