
import customer
c=0
id=100
print("starting the store")
adm=input("make admin user\n")
security_code=input("enter new security code\n")
customer.rentalsore.admin.admin_code=security_code
while(True):
    print("WHO ARE YOU\ntype customer for customer \ntype admin for admin \ntype exit to exit")
    str=input()
    if str=="customer":
        
        name1=input("enter your username that has not been taken by anyone else\n")
        for i in customer.rentalsore.admin.enti:
            if i.name==name1:
                print("username already exist")
                pas1=input("enter password")
                if pas1==i.password:
                    obj=i
                else:
                    print("wrong password")
                c=1
                break
        if c==0:
            contact=input("enter your contact\n")
            password=input("enter your password")
            obj=customer.entity(name1,contact,id,password)
            id+=1
            customer.rentalsore.admin.enti.append(obj)
        
        while True:
            print("""pick a choice
1. See available bikes on the shop and list of price
2. Rent bikes basis of price list
3. return bike
4. see profile
5. go backto login menu\n""")
            number=int(input("enter your choce from above\n"))
            if number==1:
                print(customer.rentalsore.admin.no_of_bike_nprice())
            elif number==2:
                num=int(input("number of bikes that you want to rent\n"))
                str2=input("for how long as mentioned on the list\n")
                print(obj.rent_bike(num,str2))
            elif number==3:
                num=int(input(f"number of bikes that you want to return from {obj.quanti}\n"))
                print(obj.return_bike(num))
            elif number==4:
                print(obj.show_entity())
            elif number==5:
                break
            else:
                print("wrong choice choose again\n")
                continue
    elif str=="admin":
        sec_code=input("enter the security code for admin access\n")
        if customer.rentalsore.admin.admin_code!=sec_code:
            print("wrong security code")
        else:         
            while True:
                print("""pick a choice
1. display the rented bikes 
2. list of entitis/customers
3. Display available inventory
4. increase number of bikes that can be rented or add stock
5. go backto last menu""")
                number=int(input("enter your choce from above\n"))
                if number==1:
                    print("list of bikes rented by customers\n",customer.rentalsore.admin.dict_rent)
                elif number==2:
                    lst=[]
                    for x in customer.rentalsore.admin.enti:
                        lst.append(x.show_entity())
                    print("all entity curently in the system\n",tuple(lst))
                elif number==3:
                    print(customer.rentalsore.admin.display_invent())
                elif number==4:
                    num=int(input("Enter the number of bikes/stocks you want to add\n"))
                    print(customer.rentalsore.admin.add_no_of_bikes(num))
                elif number==5:
                    break
                else:
                    print("wrong choice choose again\n")
                    continue
            
    elif str=="exit":
        break
    else:
        print(f"there is no entity named {str}\n")