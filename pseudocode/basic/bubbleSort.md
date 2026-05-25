

# Problem = Bubble Sort


```pseudocode
BEGIN

    READ list
    SET n = LENGTH(list)

    FOR i = 1 TO n-1 DO
        FOR j = 1 TO n-i DO
            IF list[j] > list[j+1] THEN
                SWAP list[j] AND list[j+1]
            END IF
        END FOR
    END FOR

    PRINT list

END
```