import datetime
time=datetime.datetime.now()
prod=[{'id': 1, 'Item': 'tea', 'Quantity': 2, 'Price_per_unit': 5, 'Total': 10}, {'id': 2, 'Item': 'coffee', 'Quantity': 4, 'Price_per_unit': 10, 'Total': 40}]
prod1=prod
temp=[]
temp1=[]
order=[]
order1=order


def AdminModule():
    print("*********************")
    print("1.Add Product in Stock (ProductName, UnitPrice)")
    print("2.Update Product price in Stock")
    print("3.Remove Product from Stock")
    print("4.View All Products in Stock")
    print("5.Logout Admin")
    print("*********************")
    

def adminDisplayMenu():
    print("Id\tItem\tQuantity\tPrice_per_unit\tTotal")
    print("***************************************************")
    for d in prod:
        print(f'{d["id"]}\t{d["Item"]}\t{d["Quantity"]}\t\t{d["Price_per_unit"]}\t{d["Total"]}')
        
                       
def addItem():
    n=int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id=int(input("Enter id : "))
        new_Item=input("Enter Item : ")
        new_Quantity=int(input("Enter Quantity : "))
        new_Price_per_unit=int(input("Enter Price_per_unit : "))
        new_Total=int(new_Quantity*new_Price_per_unit)
        d=[{"id":new_id,"Item":new_Item,"Quantity":new_Quantity,"Price_per_unit":new_Price_per_unit,"Total":new_Total}]
        prod.extend(d)
        adminDisplayMenu()
        
def removeItem():    
    prodId=int(input("Enter the id need to be deleted : "))
    found=False
    for d in prod1:
        found=d["id"]==prodId
        if found !=True:
            temp.append(d)
            continue
        if found==True:
            d["Quantity"]-=1
    print("Deleting item....")
    if len(temp)==d:
        print(f"{prodId} not found")
    else:
        print(f"{prodId}'s one available is removed from the list")
    adminDisplayMenu()
def goods():
    Total=0
    print("\n")
    for d in prod:
        print(f'{d["Item"]} = {d["Quantity"]}')
        Total+=(d["Quantity"])
    print("\nTotal available goods is : ",Total)
def GrandTotal():
    total=0
    for o in order:
        total+=(o["Quantity"]*o["Price_per_unit"])
    print("\nGrand Total is : ",total)

def PrintInvoice():
    name=input("enter customer name: ")
    print("***************************************************")
    print("\n*****ONLINE RETAIL SHOPPING - INVOICE*****\n")
    print("***************************************************")
    print("Customer: ",name,"\t\tDate: ",time.strftime("%d""/%b""/""%g") )
    print("Id\tItem\tQuantity\tPrice_per_unit\tTotal")
    print("***************************************************")
    for o in order:
        print(f'{o["id"]}\t{o["Item"]}\t{o["Quantity"]}\t\t{o["Price_per_unit"]}\t{o["Total"]}')
    GrandTotal()
    print("\n***************************************************\n")
    
def logoutA():
    loginA()    

def adminChoice():
    choice=int(input("Please enter admin choice : "))
    if choice==2:
        adminDisplayMenu()
        print("\n***************************************************\n")
        AdminModule()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==1:
        adminDisplayMenu()
        print("\n***************************************************\n")
        addItem()
        print("\n***************************************************\n")
        AdminModule()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==3:
        adminDisplayMenu()
        print("\n***************************************************\n")
        removeItem()
        print("\n***************************************************\n")
        AdminModule()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==4:
        adminDisplayMenu()
        goods()
        print("\n***************************************************\n")
        AdminModule()
        print("\n***************************************************\n")
        adminChoice()
    elif choice==5:
        loginU()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n***************************************************\n")
        AdminModule()
        print("\n***************************************************\n")
        adminChoice()

def ConsumerModule():
                print("Id\tItem\tQuantity\tPrice_per_unit")
                print("***************************************************")
                for d in prod:
                    print(f'{d["id"]}\t{d["Item"]}\t{d["Quantity"]}\t\t{d["Price_per_unit"]}')
def user_id():
    ConsumerModule()
    new_id=int(input("\nEnter the id : "))
    
def placeOrder():
    #n=int(input("Enter the no.of.items need to be added : "))
    for d in prod:
        new_id=int(input("Enter id : "))
        new_Item=input("Enter Item : ")
        new_Quantity=int(input("Enter Quantity : "))
        new_Price_per_unit=int(f'{d["Price_per_unit"]}')
        new_Total=int(new_Quantity*new_Price_per_unit)
        o=[{"id":new_id,"Item":new_Item,"Quantity":new_Quantity,"Price_per_unit":new_Price_per_unit,"Total":new_Total}]
        order1.extend(o)
    #ConsumerModule()
    #new_id=int(input("\nEnter the id : "))
    #for d in prod:
        if d["id"]==new_id:
            print("\nId\tItem\tQuantity\tPrice_per_unit")
            print("***************************************************")
            print(f'{d["id"]}\t{d["Item"]}\t\t{d["Price_per_unit"]}')
            #order=['{d["id"]}\t{d["Item"]}\t{d["Quantity"]}\t{d["Price_per_unit"]}\t{d["Total"]}']
            conform=input("\nDo you want to place an order on the above shown product : Y/N ")
            if conform=='Y' or conform=='y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["Item"],d["Quantity"]))
                d["Quantity"]-=1
                break
            elif conform=='N' or conform=='n' :
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform=input("\nDo you want to place an order on the above shown product : Y/N ")
                break
                    
        #elif d["id"]!=new_id:
          #  print("\nYou have entered invalid id. Please enter valid id\n")
        #user_id()            
    print("\nAvailable products : \n")    
    ConsumerModule()
    
def cancelOrder():
    found=False
    temp1=[]
    order_id=input("Enter the order id : ")
    for o in order1:
        found=o["id"]==order_id
        if found!=True:
            temp1.append(o)
            continue
        if found==True:
            order1["Quantity"]-=1
    print("Deleting item....")
    if len(temp1)==o:
        print(f'{order_id} is not found')
    else:
        print(f'{order_id} is removed from the placed order')

def userLogin():
    print("*********************\n")
    print("1.View All Products in Stock")
    print("2.Add to shopping basket")
    print("3.View all product of basket")
    print("4.Search product in Stock")
    print("5.Remove product from basket")
    print("6.Print invoice")
    print("7.Logout")
    print("\n*********************")
    
def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        ConsumerModule()#Basket(ProductName , Quantity)
        print("\n***************************************************\n")
        userLogin()
        print("\n***************************************************\n")
        userChoice()
    elif choice==2:
        placeOrder()
        print("\n***************************************************\n")
        userLogin()
        print("\n***************************************************\n")
        userChoice()
    elif choice==3:
        print("Id\tItem\tQuantity\tPrice_per_unit\tTotal")
        print("***************************************************")
        for o in order:
            print(f'{o["id"]}\t{o["Item"]}\t{o["Quantity"]}\t\t{o["Price_per_unit"]}\t{o["Total"]}')
        print("***************************************************")
        userChoice()
    elif choice==5:
        cancelOrder()
        print("\n***************************************************\n")
        userLogin()
        print("\n***************************************************\n")
        userChoice()
    elif choice==6:
         PrintInvoice()
         #GrandTotal()
         print("\n***************************************************\n")
         userLogin()
         print("\n***************************************************\n")
         userChoice()
    elif choice==7:
         #loginU()
         print("Thank You")
         loginU()
    else:
         print("Invalid Choice. Please enter valid choice")            

def loginA():
   password=input("Enter Admin password (pswd-admin) : ")
   if password=="admin":
       AdminModule()
       adminChoice()    
   else:
       print("Invalid password. Please enter valid password")
       loginA()

def loginU():
    ans=input("wanna shop?(y/Y)  ")
    if ans=='y' or ans=='Y' :
         password=input("Enter user password (pswd-user) : ")
         if(password=="user"):
              userLogin()
              userChoice()
         else:
              print("Invalid password. Please enter valid password")
              loginU()
    
def main():
     loginA()
     #loginU()
main()
print("Online Retail Shopping Program Successfully executed!")
print("Developer: Akshansh Pal")
