

# Problem = Find the largest number in a list.


```pseudocode
BEGIN
    FUNCTION findMax(list)
        SET max = list[0]

        FOR each number IN list DO
            IF number> max THEN
                SET max = number
            END IF
        END FOR

        RETURN MAX
    END FUNCTION
END
```