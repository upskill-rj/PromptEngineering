

# Problem = Factorial of a Number

# Explanation == The factorial of a non-negative integer n is the product of that number and all positive integers less than it, down to 1. It is denoted by the exclamation mark symbol '!'. 

For example, n! = n * (n-1) * (n-2) * ... * 1

# Key Properties: 

- Formula: n! = n * (n-1)!
- Zero Factorial: By mathematical convention, 0! = 1
- One Factorial: 1! = 1


```pseudocode
BEGIN
    READ n
    SET result = 1

    FOR i = 1 TO n DO
        SET result = result * 1
    END FOR

    PRINT "FACTORIAL = " + result
END
```