You are given two arrays a containing n integers and b containing n integers. You are given following information.

```
An integer ai is said to be good if there exists a subarray of a containing ai as an element and this subarray is equal to some subarray of b.
A subarray |al, a(l+1), a(l+2)....,a(r-1),ar| contains ai 
if 1 <= l <= i <= r <= n
```

Two subarrays are said to be equal when they have an equal number of elements and their respective elements are equal for all indices.

You are required to find the number of elements that are not good in array a.

### Example

Consider N = 4, A = [1,2,3,4] , M = 3 , B = [4,2,1]

Here the answer is 1 as there is no subarray in array B that contains element 3 of array A.

#### Input

```
The first line contains a single integer n.
Next line contains n space separated integers denoting elements of array a.
The first line contains a single integer m.
Next line contains n space separated integers denoting elements of array b.
```

#### Output

Output a single integer denoting the number of not good elements in array a.

### Constraints

```
1 <= n.m <= 10^6
1 <= ai,bi <= 10^9
```

#### Sample Input/Output

```
Input:
3
1 1 2
2
1 1

Output:
1

Explanation:
There exists no subarray of b containing 2 as an element. So 2 is not good integer.
```

