'''This program can be thought of as a way to order food from a grocery shopping app. And grocery is just a small example. It can be used to order laptops from a computer store or anything else from any other store. This is just a very limited example to represent the basic idea and functionality of a program.'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
'''👇here a random list of items are defined with their quantities and the units they are sold in, these are essentially just samples and are limited, however it could be expanded upon with as many items as possible.'''
items=['bread', 'cereal', 'cheese', 'chicken', 'milk', 'sausage', 'yogurt']
itemqty = [5, 12, 8, 10, 9, 7, 6]  
itemunits=["packets","packets","packets","pounds","cartons","pounds","cups"]

'''the following function has been used to prompt the user with messages and take the appropriate input. This function is the heart of the program and runs all the basic operations'''
def user_prompt():

  '''Below we are just prompting the user to enter a item they would desire and taking that input to fetch it from the list of items available using the binary search function we were provided with.'''
  print("The following items are available:")
  for i in items:
    print(i)
  word=input("Please type the item you are looking for: ")
  itemfind=binary_search(items,word)

  '''Below we are trying to check whether the item entered is even there in our list and if it isn't we are prompting a valid message to the user'''
  if itemfind==-1:
    print("Sorry but this item is unavailable.")
  else:
    print("There are",itemqty[itemfind],itemunits[itemfind],"of",items[itemfind],"available.")

    '''Below we are trying to input the quantity the user wants of the particular item he mentioned, this only happens after checking whether the item mentioned by the user actually exists in the list'''
    quantity=int(input("How many do you want: "))

    '''If the user inputs a number that is higher than the amount available than a valid message is prompted to the user and the user can enter a number again'''
    while quantity>itemqty[itemfind]:
      print("Sorry but only",itemqty[itemfind],itemunits[itemfind],"is available")
      quantity=int(input("How many do you want: "))
    if quantity<=itemqty[itemfind]:
      print("Great! you will recieve your order soon. Thank you for working with the master coder grocery app.")

      '''After a valid quantity is entered a thank you message has been printed and the quantity is updated in the list.'''
      itemqty[itemfind]=itemqty[itemfind]-quantity
user_prompt()
