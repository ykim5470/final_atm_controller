# ATM Controller Package 

## Overview 
This project aims to control a simple ATM operations and test modules for further integration.

The main operation process is as follows.
1. Build the program
```
$ pip install -r requirements.txt
$ python3 -m pip install --upgrade build
$ python3 -m build
```

2. Run the program
``` 
//implement main function 
$ python src
```

3. Run the module

### Case 0. ATM Initialize &  State update with default
```
"""
Initial state
Please insert card if you want to make a transaction : 
"""
```

### Case 1. Insert Card & State update with card inserted
Insert Card action is started when a user press "1" 
After 3 sec delay occurs for card reading process time 
Card state updated and request card PIN number
```
"""
Please insert card if you want to make a transaction : 1
Wait please
alex
Your are now having card state
Please Enter 4-digit PIN number :
"""
```

### Case 2. Pin Authenticate & State update with HasCard
Authenticate process operated
If valid pin number is entered, update state and proceed next 
If not valid pin number is entered, keep asking a valid pin number

( aka. Demo pin Number is "0000" for any registered user) 
```
"""
// Not valid
Please Enter 4-digit PIN number : 1111
Your are now having card state
Please Enter 4-digit PIN number :

// valid
Please Enter 4-digit PIN number : 0000
Please select one of the following accounts you have
1 : WESTPAC
2 : NAB
"""
```

### Case 3. Select Account & State update with AccountSelected
Show registered card account options and receive user select action 
Different accounts are independent instance from Bank
If wrong account selected, then keep asking a valid option 
If account is selected, then proceed next
```
"""
Please select one of the following accounts you have
1 : WESTPAC
2 : NAB
2
alex
NAB
Please select one of the following options
1. Balance
2. Deposit
3. Withdraw
4. Exit

"""
```

### Case 4. Transaction Balance check 
Show balance
```
"""
1
alex at NAB left $ 3000
Please select one of the following options
1. Balance
2. Deposit
3. Withdraw
4. Exit

"""
```

### Case 5. Transaction Deposit check
Insert Cash
After 3 sec delay for counting notes from cash bin 
Confirm amount inserted from user 
If amount is matched, Entered "1" from user 
Update ATM cash bin balance

```
"""
2
Please insert cash in the bin 
1002
Your notes inserted is : 1002
please enter 1 if the amount is correct
1
alex at NAB left $ 4002
"""
```

### Case 6. Transaction Withdraw check
Withdraw Cash
Check if cash is enough in the cash bin
Check if balance is enough in the bank 
If all meets, proceed

```
"""
// If balance is low
Your notes to withdraw are : 4003
Over withdraw!
alex at NAB left $ 4002
Please select one of the following options
1. Balance
2. Deposit
3. Withdraw
4. Exit


// If Valid
alex at NAB left $ 3802
Please select one of the following options
1. Balance
2. Deposit
3. Withdraw
4. Exit

"""
```


### Case 7. Exit
Exit State update default if exit occurs
Return card and back to default state at Case 1 

```
"""
4
You entered exit
Please take your card :)
Initial state
Please insert card if you want to make a transaction :
"""
```

## Test Code 
Unfortunately, it was not fully handled for testing all cases of modules in this project.
Mainly focused on how module work and states have been properly updated. 
```
$ python -m unittest discover .
```



