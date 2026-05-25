

# Problem == Reverse String


```pseudocode
BEGIN
    READ str
    SET reversed = ""

    FOR i = LENGTH(str) DOWN TO 1 DO
        SET reversed = reversed + str[i]
    END FOR

    PRINT reversed
END
```