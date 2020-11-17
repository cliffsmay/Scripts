import sys

#account balance 
account_balance = float(500.25)
userchoice = input ("What would you like to do?\n")



#printbalance function = custom function to request account balance

def printbalance ():
   global account_balance

  

#deposit function = custom function to add funds to the account and update account balance

def deposit ():
  global account_balance
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  account_balance = account_balance + float(deposit_amount)
  print("Deposit was $" + str('%.2f' % float(deposit_amount)) + ", current balance is $" + str(account_balance))
  
#withdraw function = custom function for withdrawing funds from the account and updating account balance
#input parameters are used within the function to determine if the value requested is greater than account balance

def withdrawal ():
  global account_balance
  withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  if float(withdrawal_amount) > account_balance:
    print("$" + str('%.2f' % float(withdrawal_amount)) + " is greater than your account balance of $" + str(account_balance))
  else:
    account_balance = account_balance - float(withdrawal_amount)
    print("Withdrawal amount was $" + str('%.2f' % float(withdrawal_amount)) + ", current balance is $" + str(account_balance))
    
#the proper functions are called in the main portion of the code to return the correct output. 

if (userchoice == 'B'):
  print("Your current balance:\n")
  print(account_balance)
elif (userchoice == 'D'):
  deposit()
elif (userchoice == 'W'):
  withdrawal()
elif (userchoice == 'Q'):
  print('Thank you for banking with us.')
  