Bob loves chess so one day he asked his brother a simple problem of chess in which his brother need to calculate the number of ways to place N rooks on N x N chessboard such that below conditions should met

```
1. All the empty cell of chessboard should under the attack
2. Exactly K pair of rooks should attack each other
```

### Note

```
1. Two ways to place the  rooks are considered different if there exists atleast one cell which is empty in one of the ways
but contains a rook in another way

2. An empty cell of chessboard is under attack is there is at leat one rook in the same row or atleast one rook in the same column. 
Two rooks attack each other if they share the same row or column, and there are
no other rooks between them
```

The answer might be large, so print it modulo 998244353

#### Input

The only line of input contains two integers N and K

#### Output

Print the number of ways to place the rooks, taken modulo 998244353

### Examples

```
Input:
3 2
Output:
6

Input:
3 3
Output:
0

Input:
4 0
Output:
24
```

#### Sample Input/Output

```
Input:
3 2
Output:
6
```

