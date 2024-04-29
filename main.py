import mysql.connector
import re

for i in range(1):
    myPassword = "mySQL4me-preston"

# adds account to sql database
def add_account():
    # get names
    firstName = input("What is your First Name? ")
    lastName = input("What is your Last Name? ")

    # get pin
    pin = input("What would you like your 4 digit PIN to be? ")
    while (re.match("\\d{4}", pin) == None):
        pin = input("Please put a valid 4 digit PIN: ")

    # create new account in database
    testQuery = ('INSERT INTO bank_accounts (First_name, Last_name, Balance, PIN) VALUES ("'+firstName+'", "'+lastName+'", 0.0, '+str(pin)+')')
    cursor.execute(testQuery)
    connection.commit()

    # gets account id
    testQuery = ("SELECT @@IDENTITY AS identity")
    cursor.execute(testQuery)

    for item in cursor:
        id = item[0]

    print("Account added. Your account ID is: " + str(id))

# deletes account from sql database
def delete_account():
    # get account id from user
    accountID = input("What is the Account ID of the account you are trying to delete? ")

    # find account pin
    testQuery = ("SELECT PIN FROM bank_accounts WHERE ID =" + accountID)
    cursor.execute(testQuery)

    for p in cursor:
        accPin = p[0]

    # verifies pin 
    pin = input("What is the 4 digit PIN (Type 0 to exit)? ")
    while (pin != accPin):
        if (pin == "0"): return
        pin = input("Incorrect PIN. Try Again (Type 0 to exit): ")

    # deletes account
    testQuery = ("DELETE FROM bank_accounts WHERE ID = " + accountID)
    cursor.execute(testQuery)
    connection.commit()

    print("Account deleted.")

# views account in sql database
def view_account():
    # get id of requested account
    accountID = input("What is the Account ID of the account you are trying to view? ")

    # find account pin
    testQuery = ("SELECT PIN FROM bank_accounts WHERE ID =" + accountID)
    cursor.execute(testQuery)

    for p in cursor:
        accPin = p[0]

    # verifies pin
    pin = input("What is the 4 digit PIN (Type 0 to exit)? ")
    while (pin != str(accPin)):
        if (pin == "0"): return
        pin = input("Incorrect PIN. Try Again (Type 0 to exit): ")

    # finds accound balance
    testQuery = ("SELECT balance FROM bank_accounts WHERE ID = " + accountID)
    cursor.execute(testQuery)

    for balance in cursor:
        print("Your Account has "+ str(balance[0]) + "$")

# deposites money in account
def deposit_money():
    # get accound id
    accountID = input("What is the Account ID of the account you are trying to deposit to? ")

    # get amount of money to be deposited
    deposit = float(input("How much money would you like to deposit? "))
    while (deposit <= 0):
        print("You cannot deposit that amount of money")

    # gets previous account balance
    testQuery = ("SELECT balance FROM bank_accounts WHERE ID = " + accountID)
    cursor.execute(testQuery)

    for p in cursor:
        balance = p[0]

    # updates sql database on new account balance
    testQuery = ("UPDATE bank_accounts SET balance = " + str(float(balance)+deposit) + " WHERE ID = " + accountID)
    cursor.execute(testQuery)
    connection.commit()

    for balance in cursor:
        print("Account " + accountID + " has been deposited "+ str(deposit) + "$")

# withdraws money from account
def withdraw_money():
    # gets account id
    accountID = input("What is the Account ID of the account you are trying to withdraw from? ")

    # finds account pin
    testQuery = ("SELECT PIN FROM bank_accounts WHERE ID =" + accountID)
    cursor.execute(testQuery)

    for p in cursor:
        accPin = p[0]

    # verifies pin
    pin = input("What is the 4 digit PIN (Type 0 to exit)? ")
    while (pin != str(accPin)):
        if (pin == "0"): return
        pin = input("Incorrect PIN. Try Again (Type 0 to exit): ")

    # finds and displays old balance
    testQuery = ("SELECT balance FROM bank_accounts WHERE ID = " + accountID)
    cursor.execute(testQuery)

    for p in cursor:
        balance = p[0]

    # gets amount of money being withdrew
    withdraw = float(input("How much money would you like to withdraw (You have "+str(balance)+"$)? "))
    while (withdraw <= 0 or withdraw > balance):
        print("You cannot deposit that amount of money")

    # updates account
    testQuery = ("UPDATE bank_accounts SET balance = " + str(float(balance)-withdraw) + " WHERE ID = " + accountID)
    cursor.execute(testQuery)
    connection.commit()

    print("Account " + accountID + " has withdrew "+ str(withdraw) + "$")



print("Welcome to the bank!")
connection = mysql.connector.connect(user = 'root', database = 'lesson_3', password = myPassword)
cursor = connection.cursor()

while True:
    # prints bank actions
    print()
    print("Here are your options:")
    print("Add Account (1)")
    print("Delete Account (2)")
    print("View Account (3)")
    print("Deposit Money (4)")
    print("Withdraw Money (5)")
    print("Exit (0)")

    # gets user action
    userInput = input("-> ")
    print()

    # runs according action
    if (userInput == "1"):
        add_account()
    elif (userInput == "2"):
        delete_account()
    elif (userInput == "3"):
        view_account()
    elif (userInput == "4"):
        deposit_money()
    elif (userInput == "5"):
        withdraw_money()
    elif (userInput == "6"):
        testQuery = ("SELECT * FROM bank_accounts")
        cursor.execute(testQuery)
        for element in cursor:
            print(element)
    
    if (userInput == "0"): break


cursor.close()
connection.close()