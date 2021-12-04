deposit = 0
balance = 0
withdrawl = 0
print('hello')
def Bal(amt):
    print("Your account balance is INR: {}".format(balance))
def Deposit():
    deposit = int(input("Enter the amount to deposit: "))
    global balance
    balance += deposit
    print("Your account is cerdited with INR: {}".format(deposit))
    Bal(balance)
def Withdraw():
    withdraw = float(input("Enter the amount to withdraw: "))
    global balance
    if withdraw > balance:
        print("No sufficient amount in your account")
    else:
        print("Your account debited with INR: {}".format(withdraw))
        balance -= withdraw
        Bal(balance)
while True:
    print('-'*100)
    print("A T M O p e r a t i o n s ")
    print('-'*100)
    print("""1. Deposit
2. Withdraw
3. Balance Enquiry
4. Exit""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Deposit()
    elif choice == 2:
        Withdraw()
    elif choice == 3:
        Bal(balance)
    else:
        print("Thankyou")
        break
