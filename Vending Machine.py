#Vending Machine


#The following vending machine lets the user choose the item they want to buy out of the given 2 categories.
#User will enter their  money and will be refunded the remaining amount when they're done using the vending machine.
#After buying an item user may another item if desired.
#The machine follows a stock system. Items will run out of stock at a point and the user will be notified.


#Creating a VendingMachine function
def VendingMachine():

    #Display time
    import time
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("\n" + local_time.rstrip() + "\n")

    #Display text
    print("\n\t\t     Welcome to the Vending Machine!\n\n-------------------------------------------------------------------------")
    
    #Creating categories

    #Creating different dictionary for each drink in the drinks category:
    a={
            "item_id":"01",
            "item_name":"Pepsi ",
            "item_price":3.00,
            "stock":2
        }
    b={
            "item_id":"02",
            "item_name":"Sprite",
            "item_price":3.00,
            "stock":3
        }
    c={
            "item_id":"03",
            "item_name":"Fanta ",
            "item_price":3.00,
            "stock":4
        }
    d={
            "item_id":"04",
            "item_name":"Coffee",
            "item_price":2.00,
            "stock":7
        }
    e={
            "item_id":"05",
            "item_name":"Tea   ",
            "item_price":2.00,
            "stock":7
        }
    f={
            "item_id":"06",
            "item_name":"Juice ",
            "item_price":1.50,
            "stock":1
        }
    g={
            "item_id":"07",
            "item_name":"Water ",
            "item_price":1.00,
            "stock":8
        }
    h={
            "item_id":"08",
            "item_name":"Milk  ",
            "item_price":2.00,
            "stock":9
        }
   
    #Creating different dictionaries for each snack in the snacks category:
    i={
            "item_id":"09",
            "item_name":"Chips    ",
            "item_price":2.50,
            "stock":6
        }
    j={
            "item_id":"10",
            "item_name":"Cookie   ",
            "item_price":2.00,
            "stock":5
        }
    k={
            "item_id":"11",
            "item_name":"Chocolate",
            "item_price":4.00,
            "stock":5
        }
    l={
            "item_id":"12",
            "item_name":"Apple Pie",
            "item_price":4.50,
            "stock":4
        }
    m={
            "item_id":"13",
            "item_name":"Nachos   ",
            "item_price":2.50,
            "stock":9
        }
    n={
            "item_id":"14",
            "item_name":"Nut Bar  ",
            "item_price":1.50,
            "stock":3
        }
    o={
            "item_id":"15",
            "item_name":"Croissant",
            "item_price":2.50,
            "stock":5
        }
    p={
            "item_id":"16",
            "item_name":"Sandwich ",
            "item_price":3.50,
            "stock":7
        }
    q={
            "item_id":"17",
            "item_name":"Popcorn  ",
            "item_price":2.00,
            "stock":4
        }
    r={
            "item_id":"18",
            "item_name":"Cupcake  ",
            "item_price":4.00,
            "stock":5
        }
    s={
            "item_id":"19",
            "item_name":"Brownie  ",
            "item_price":4.00,
            "stock":2
        }
    t={
            "item_id":"20",
            "item_name":"Gum      ",
            "item_price":1.00,
            "stock":8
        }

    #Creating a list which contains all The items 
       
    AvailableDrinks = [a,b,c,d,e,f,g,h]
    AvailableSnacks = [i,j,k,l,m,n,o,p,q,r,s,t]
 

    #Cash in Machine:
    cash = 0.00

    #Creating a function to show the drinks menu
    def display(AvailableDrinks):
        print("\nThe items available are: \n\n---------------------------------Drinks----------------------------------")
        
        for i in AvailableDrinks:
            print(f"Item Id : {i['item_id']} --- Item Name : {i['item_name']} --- Item Price : {i['item_price']} --- Stock : {i['stock']}")
    
    display(AvailableDrinks)

    
    #Creating another function to show the snacks menu
    def display (AvailableSnacks):
        print("\n\n---------------------------------Snacks-----------------------------------")
        
        for i in AvailableSnacks:
            print(f"Item Id : {i['item_id']} --- Item Name : {i['item_name']} --- Item Price : {i['item_price']} --- Stock : {i['stock']}")

        print("\n-------------------------------------------------------------------------")
    display(AvailableSnacks)



    #using a while loop to start the main purchasing process
    while True:
        SelectedItem = input("Enter the ID of the item you wish to buy: ")
        for i in AvailableDrinks:
            if SelectedItem == i.get("item_id"): #User will buy the item by entering item id
                SelectedItem = i
                if i.get("stock") == 0: #Creating a stock system for the drinks
                    #User will be notified when the stock runs out
                    print("\nSorry item is out of stock.")
                    print(f"Item Id : {i['item_id']} --- Item Name : {i['item_name']} --- Item Price : {i['item_price']} --- Stock : {i['stock']}")
                    print("-------------------------------------------------------------------------")
                    break
                    
                else:
                    item_price = SelectedItem.get("item_price")
                    while cash < item_price: #Tell the required amount of cash to the user
                        cash = float(input("Please insert AED " + str(item_price - cash) + ":~ "))
                    else:
                        print ("You have purchased " + SelectedItem.get("item_name") + "\n-------------------------------------------------------------------------")
                        SelectedItem["stock"] -= 1
                        cash -= item_price
                        print("Your remaining balance is :~ " + "AED " + str(cash)) #Tell the user their remaining balance in the machine
                        question = input("Would you like to buy anything else? \nyes/no :~ ") #Asking if user wants to buy anything else
                        print("-------------------------------------------------------------------------")
                        if question == "no": #Code for when the user types no
                            if cash != 0: #Returning the remaining cash after user is done
                                print("AED " + str(cash) + " have been returned." + "\n-------------------------------------------------------------------------" )
                                cash = 0
                                print ("Thank you for using this vending  machine. Have a great day!\n--------------------------------------------------------------------------")
                                break
                            else:
                                print ("Thank you for using this vending  machine. Have a great day!\n-------------------------------------------------------------------------")
                                break
                        else: #Continues the process if user types yes
                            continue
            
        
            
                         
    
    #Same code is used twice. Once for drinks and then for snacks as there are two lists being used instead of one
    #Taking user input to buy snacks while calculating cash   
        for i in AvailableSnacks:
            if SelectedItem == i.get("item_id"): #User will buy the item by entering item id
                SelectedItem = i
                if i.get("stock") == 0: #Creating a stock system for the snacks
                    #User will be notified when the stock runs out                              
                    print("\nSorry item is out of stock.")
                    print(f"Item Id : {i['item_id']} --- Item Name : {i['item_name']} --- Item Price : {i['item_price']} --- Stock : {i['stock']}")
                    print("-------------------------------------------------------------------------")
                    break
                else:    
                    item_price = SelectedItem.get("item_price")
                    while cash < item_price: #Code to tell the user how much money he has to pay
                        cash = float(input("Please insert AED " + str(item_price - cash) + ":~ "))
                    else:
                        print ("You have purchased " + SelectedItem.get("item_name") + "\n-------------------------------------------------------------------------")
                        SelectedItem["stock"] -= 1 
                        cash -= item_price
                        print("Your remaining balance is :~ " + "AED " + str(cash)) #Tell the user their remaining balance in machine
                        question = input("Would you like to buy anything else? \nyes/no :~ ") #Ask if they want to buy anything else
                        print("-------------------------------------------------------------------------")
                        if question == "yes":
                            continue
                            
                        elif question=="no": #Code for when the user types no
                            if cash != 0: #Returning the remaining cash after user is done
                                print("AED " + str(cash) + " have been returned." + "\n-------------------------------------------------------------------------" )
                                cash = 0
                                print ("Thank you for using this vending  machine. Have a great day!\n-------------------------------------------------------------------------")
                                break
                        break
                     
                    


                        
    
            
    
VendingMachine()