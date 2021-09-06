You are given a list of numbers. Write an algorithm to remove all the duplicate numbers of the list so that the list contains only distinct numbers in the same order as they appear in the input list.

#### Input

```
The first line of the input consists of an integer size, representing the number of elements in the list (N).

The second line consists of N space separated integers
arr[0],arr[1],arr[2],.....,arr[N]
representing the list of positive integers
```

#### Output

Print space separated integers representing the distinct elements obtained by removing all the duplicate elements from the given list.

#### Constraints

```
0 < N < 10^5
-10^6 < arr[i] < 10^6
0 <= i <= N
```

#### Example

```
Input: 
8
1 1 3 2 1 4 5 4

Output:
1 3 2 4 5

Explanation:
Remove all the duplicate elements from the list (i.e., 1 and 4)
The final list is {1,3,2,4,5}
```

#### Follow up

Can you do this without taking new list/array (modifying the same list)