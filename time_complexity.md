## Simple for-loop
for x in range(n):  
    statement(s) that take constant time  
### Running Time Complexity = O(n)

## For-loop with Increments
for x in range(1, n, k):  
    statement(s) that take constant time  
### Runing Time Complexity = O(n)

## Simple Nested For-loop
for i in range(n):  
    for x in range(m):  
        Statement(s) that take(s) constant time  
### Running Time Complexity = O(nm)

## Nested For-loop with Dependant Variables
for i in range(n):  
    for x in range(i):  
        Statement(s) that take(s) constant time  
### Running Time Complexity = O(n^2)

## Nested For-loop with Index Modification
for i in range(n):  
    i *= 2  
    for x in range(i):  
        Statement(s) that take(s) constant time  
### Running Time Complexity = O(n^2)

## Loops with log(n) time complexity
while i < n:  
    i*=k  
    Statement(s) that take(s) constant time  
### Running Time Complexity = O(log k (n))