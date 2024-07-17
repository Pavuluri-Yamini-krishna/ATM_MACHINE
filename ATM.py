#For stopping program execution for few seconds
import time

print("Please insert Your CARD...")

#For card processing
time.sleep(4)

password = 2024

#Waiting for  atm pin from user
pin = int(input("Enter your ATM PIN:  "))

#User balance
balance = 5000

#Checking pin is Valid or Invalid
if pin == password:
    #Loop will run the user
    while True:

        #Showing choice of info to user

        print(""" 
			1. BALANCE INQUIRY
			2. CASH WITHDRAWAL
			3. CASH DEPOSIT
			4. EXIT
			"""
              )

        try:    
             #Option from user
            option = int(input("Please enter your option: "))
        except:
            print("Invalid option!")
        
        #for option 1        
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("Enter amount to withdraw:  "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"Your updated balance is {balance}")

            

        if option == 3:

            deposit_amount = int(input("Enter amount to deposit: "))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account.")



            print(f"Your new balance is {balance}")



        if option == 4:
             print("Thank you for using the ATM. Goodbye!")
             break

else:
    print("Incorrect pin. Please try again!")
