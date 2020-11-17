import sys
'''
Section 1: Collect customer input
'''
# user is prompted to input the rental code B, D, or W 
# which is then assigned to the variable rentalCode

rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

# if, elif conditional statement 
#based on the user input the appropriate string is assigned to the variable
#the user is prompted to enter the number of days or 
#weeks the car was rented and the value is assigned to the variable rentalPeriod

if rentalCode == "W":
  rentalPeriod = input("Number of Weeks Rented:\n")
elif rentalCode == "B":
  rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == "D":
  rentalPeriod = input("Number of Days Rented:\n")

#cost assigned for each rental code

budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00	

# if, elif conditional statement 
#identifies the calculations for each rental code and
#assigns the numeric value to the variable baseCharge
#based on the input of the user

if rentalCode == "B":
  baseCharge = float(rentalPeriod) * float(budgetCharge)
elif rentalCode == "D":
  baseCharge = float(rentalPeriod) * float(dailyCharge)
elif rentalCode == "W":
  baseCharge = float(rentalPeriod) * float(weeklyCharge)

#user is prompted to enter the starting and ending odometer reading
#the numeric values are assigned to the variables odoStart and odoEnd 

odoStart = input("Starting odometer reading:\n")
odoEnd = input("Ending odometer reading:\n")

'''
Section 2: Calculate the costs from the customer input
'''

#the number of miles driven is calculated
#the numeric value is then stored as the variable totalMiles

totalMiles = int(odoEnd) - int(odoStart)

#if conditional statement based on rental code B
#the arithmetic operator * is used to calculate the mile charge
#the value is stored as the variable mileCharge
if rentalCode == "B":
  mileCharge = float(totalMiles) * 0.25

#if, elif, else conditional statement based on rental code D
#the arithmetic operators * and / are used to calculate the mile charge
#the value is stored as the variable mileCharge
#average day miles = less than or equal to 100 = no charge 
#average day miles = more than 100 
#100 is subtracted from average day miles = extra miles
#.25 cents per extra mile is calculated an assigned to the variable mileCharge
#comparision operator <= is used to distinguish less than or equal to 100 miles
  
elif rentalCode == "D":
  averageDayMiles = float(totalMiles)/float(rentalPeriod)
  if float(averageDayMiles) <= 100:
      extraMiles = 0
  else:
      extraMiles = float(averageDayMiles) - 100;
  mileCharge = (.25 * float(extraMiles)) * float(rentalPeriod)

##if, elif, else conditional statement based on rental code W
#the arithmetic operators * and / are used to calculate the mile charge
#the value is stored as the variable mileCharge
#average weekly miles is less than or equal to 900 = no charge 
#average weekly miles exceeds 900 = $100 per week additional charge
#comparision operator <= is used to distinguish less than or equal to 900 miles
 
elif rentalCode == "W":
  averageWeekMiles = float(totalMiles)/ float(rentalPeriod)  
  if averageWeekMiles <= 900:
    mileCharge = 0
  else:
    mileCharge = 100 * float(rentalPeriod)
    
'''
Section 3: Display the results to the customer
'''

#the amount due is calculated by adding the base charge + the mile charge 
#the numeric value is assigned to the variable amtdue 

amtDue = float(baseCharge) + float(mileCharge)

#strings are assigned to variables and 
#the print function is used to print a summary of the charges

print("Rental Summary")
print("Rental Code:       " + str(rentalCode))
print("Rental Period:         " + str(rentalPeriod)) 
print("Starting Odometer: " + str(odoStart)) 
print("Ending Odometer:   " + str(odoEnd)) 
print("Miles Driven:      " + str(totalMiles))
print("Amount Due:        " + "$" + str(amtDue) + '0')