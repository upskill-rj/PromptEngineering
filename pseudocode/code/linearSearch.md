

# Problem == Linear Search


BEGIN
    READ list, target
    SET found = FALSE

    FOR each item IN list DO
        IF item == target THEN
            SET found = TRUE
            PRINT "FOUND !!"
        END IF
    END FOR

    IF found == FALSE THEN
        PRINT "Not Found"
    END IF
END
