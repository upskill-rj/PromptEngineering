
# Problem = Fibonacci Series

# Explanation : 
The Fibonacci sequence is an infinite series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.
The sequence progresses as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .....


```pseudocode
BEGIN
    READ n
    SET a = 0, b = 1

    PRINT a
    PRINT b

    FOR i = 3 TO n DO
        SET c = a + b
        PRINT c
        SET a = b
        SET b = c
    END FOR

END
```