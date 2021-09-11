You are given two strings A and B that are made of lowercase English alphabets. Find the number of different pairs (( i , j), (k, l)) such that the substrings A|i...j| and B|k..l| are equal and the value of j - i + 1 is minimum

### Example

Consider A = "abc" and B = "bcd". You must determine the answer such that it meets the given conditions

```
1. Let us choose a substring of length 1, those are 'b' and 'c'. The count is 2
2. Let us choose a substring of length 2, which is "bc". The count is 1
```

Since we need to minimize the length of matching substring hence the answer to the corresponding example is 2.

### Input

```
The first line consists of a string denoting A.
The second line consists of a string denoting B.
```

### Output

```
Print the number of different pairs (( i , j), (k, l)) such that the substrings A|i...j| and B|k..l| are equal and the value of j - i + 1 is minimum.
```

#### Constraints

```
1 <= |A|, |B| <= 10 ^ 5
```

#### Sample Input/Output

```
Input:
abcd
bd

Output:
2

Explanation:
Pairs are ((1,1), (0,0)) and ((2,2),(1,1))
```

