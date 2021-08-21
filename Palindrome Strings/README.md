Given two integers N and K, the task is to find the count of palindromic strings of length lesser than or equal to N, with first K characters of lowercase English language, such that each character in a string doesn’t appear more than twice.

##### Example 1:

```
Input:
N = 3, K = 2
Output:
6
Explanation: 
The possible strings are:
"a", "b", "aa", "bb", "aba", "bab".
```



##### Example 2:

```
Input: 
N = 4, K = 3
Output: 
18
Explanation: 
The possible strings are: 
"a", "b", "c", "aa", "bb", "cc", "aba","aca", "bab", "bcb", "cac", "cbc", 
"abba", "acca", "baab", "bccb", "caac", "cbbc". 
```

Expected Time Complexity: O(K2)

Expected Auxiliary Space: O(K2)

##### Constraints:

```
1 ≤ K ≤ 26
1 ≤ N ≤ 52
N ≤ 2*K
```

