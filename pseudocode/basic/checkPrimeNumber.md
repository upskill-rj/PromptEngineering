
# Problem = Check Prime Number


```pseudocode
BEGIN

    READ n
    SET isPrime = TRUE

    IF n < 2 THEN
        SET isPrime = FALSE
    ELSE
        FOR i = 2 TO SQRT(n) DO
            IF n % i == 0 THEN
                SET isPrime = FALSE
            END IF
        END FOR
    END IF

    IF isPrime THEN
        PRINT "Prime"
    ELSE
        PRINT " Not Prime "
    END IF

END
```