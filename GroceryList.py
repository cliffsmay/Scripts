

#empty dictionary is created for grocery_item
grocery_item = {}
#empty list is created for grocery_history
grocery_history = []

#variable used to check if while loop condition is met
stop = 'c'

#while loop is used to iterate through the loop
while stop == 'c':

    item_name = input("Item name:\n")
    quantity = int(input("Quantity purchased:\n"))
    cost = float(input("Price per item:\n"))

#dictionary entry is created
#key-value pairs are added 
    grocery_item['name']= item_name
    grocery_item['number']= int(quantity)
    grocery_item['price']= float(cost)

    
#the append function is used to modify values in the list
#data is added to the list
    grocery_history.append(grocery_item.copy())

#user is prompted asking if they have finished entering grocery items

    choice = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

#if user enters (q)uit the loop is exited
    if choice == 'q':
        break


#variable is defined to hold grand total
grand_total = float(0.00)
  
# an index-based (range) for loop is used to iterate through the loop
for i in range (0, len(grocery_history)):
  
#values in the list are accessed / values are accessed using keys
  item_total = grocery_history[i]['number'] * grocery_history [i]['price']
  
#values in the list are accessed / values are accessed using keys  
  print(str(grocery_history[i]['number']) + ' ' + str(grocery_history[i]['name']) + ' @ $' + str('%.2f' % grocery_history[i]['price']) + ' ea $' + str('%.2f' % item_total))

#the item_total is added to the grand_total
  grand_total = grand_total + item_total
    
#item_total is set to 0
item_total = 0
#grand total is printed
print(str('Grand total: $%.2f' % grand_total))