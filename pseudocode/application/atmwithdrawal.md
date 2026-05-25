

# Problem = ATM Withdrawal


```pseudocode
BEGIN
    READ balance, amount

    IF amount > balance THEN
        PRINT "Insufficient Funds"
    ELSE IF amount <=0 THEN
        PRINT "Invalid Amount"
    ELSE
        SET balance = balance - amount
        PRINT " Dispensing " + amount
        PRINT " Remaining Balance = " + balance
    END IF

END
```