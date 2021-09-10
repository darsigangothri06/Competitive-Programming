In New Delhi the DTC bus tickets have a number which follows the below properties:

```
1. The number consists N even digits
2. Only K decimal digits d1, d2, ... dk can be used to create tickets.
3. If 0 is among these digits then numbers may have leading zeros. 

For example, if N is 4 and only digit 0 and 4 can be used then
0000, 4004, 4440 are valid tickets 00 and 04 are not
```

A ticket is best **if the sum of first n/2 digits is equal to the sum of remaining digits which is n/2**

Your task is to calculate the number of different best tickets and as answer may be big so print modulo of 9989244353

```
Constraints:
N = 2 <= N <= 2*10 ^ 5
K = 1 <= K <= 10
di = 0 <= di <= 9
```

### Input

The first line contains two integers N and K where N is number of digit in ticket and K is number of different decimal digits can be used.

The second line contains a sequence of **pairwise distinct** integer d1, d2, ... dk

These are the digits that may be used in ticket numbers. The digits are given in arbitrary order.

### Output

Print the number of best ticket numbers, taken modulo 998244353

### Examples

```
Input:
4 2
1 8

Output:
6

Explanation:
There are 6 best ticket numbers
1111, 1818, 1818, 1881, 8118 and 8888
```

```
Input:
20 1
6

Output:
1

There is only one ticket number in this example, it consists of 20 digits 6.
This ticket number is best. So the answer is 1
```

#### Sample Input/Output

```
Input:
10 5
6 1 4 0 3

Output:
569725
```

