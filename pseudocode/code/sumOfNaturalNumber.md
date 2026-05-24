

# Problem == Sum of First N Natural Numbers


BEGIN
    READ n
    SET sum = 0
    FOR i = 1 TO n DO
        SET sum = sum + i
    END FOR
    PRINT "Sum = " + sum
END