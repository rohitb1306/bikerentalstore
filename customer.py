
import rentalsore
class entity:
    
    def __init__(self,name,contact,id,password):
        self.name=name
        self.contact=contact
        self.id=id
        self.password=password
        self.quanti=0
        self.balance=0.0
        

    #function for renting bikes  

    def rent_bike(self,number_bike,str1):
        if number_bike>2 and number_bike<=5 and (self.quanti+number_bike)<=5:
            disc=30/100
            rentalsore.admin.dis_customer[self.name]=disc
            if rentalsore.admin.no_of_bikes<number_bike:
                return f"Not enough bikes for rent\n{rentalsore.admin.no_of_bikes} bikes left"
            else:
                self.quanti+=number_bike
                rentalsore.admin.no_of_bikes-=number_bike
                if self.name in rentalsore.admin.dict_rent:
                    rentalsore.admin.dict_rent[self.name]=((rentalsore.admin.dict_rent[self.name][0]+self.quanti),(rentalsore.admin.dict_rent[self.name][1]+((int(rentalsore.admin.price[str1].split("$")[0])*number_bike)-((int(rentalsore.admin.price[str1].split("$")[0])*number_bike)*disc))),str1)
                else:
                    rentalsore.admin.dict_rent[self.name]=(self.quanti,(int(rentalsore.admin.price[str1].split("$")[0])*number_bike)-((int(rentalsore.admin.price[str1].split("$")[0])*number_bike)*disc),str1)
                self.balance+=rentalsore.admin.dict_rent[self.name][1]
                return "bikes rented"
        elif self.quanti+number_bike>5:
            return "we dont allow more that 5 bikes to a single customer" 
        else:
            
            if rentalsore.admin.no_of_bikes<number_bike:
                return f"only {rentalsore.admin.no_of_bikes} bikes left"
            else:
                self.quanti+=number_bike
                rentalsore.admin.no_of_bikes-=number_bike
                if self.name in rentalsore.admin.dict_rent:
                    rentalsore.admin.dict_rent[self.name]=((rentalsore.admin.dict_rent[self.name][0]+self.quanti),(rentalsore.admin.dict_rent[self.name][1]+(int(rentalsore.admin.price[str1].split("$")[0])*number_bike)),str1)
                else:
                    rentalsore.admin.dict_rent[self.name]=(self.quanti,(int(rentalsore.admin.price[str1].split("$")[0])*number_bike),str1)
                self.balance+=rentalsore.admin.dict_rent[self.name][1]
                return "bikes rented"


    def return_bike(self,number_bike):
        
        rentalsore.admin.no_of_bikes+=number_bike
        print("this is your bill\n")
        print(self.pay_bill(number_bike))
        if self.quanti==number_bike:
            self.quanti-=number_bike
            rentalsore.admin.dict_rent.pop(self.name)
            str2="all bikes returned"
        else:
            self.quanti-=number_bike
            a=rentalsore.admin.dict_rent[self.name][0]-number_bike
            rentalsore.admin.dict_rent[self.name]=(a,rentalsore.admin.dict_rent[self.name][1],rentalsore.admin.dict_rent[self.name][2])
            str2=f"returned {number_bike} left to return {self.quanti}"
        return str2        
   

    #function for showing entity

    def show_entity(self):
        return ({"Name":self.name,"contact":self.contact,"your id":self.id,"number of bikes rented":self.quanti,"ttal balance remaining":self.balance})
    
    #function for the payment 

    def pay_bill(self,number_bike):
        dis=rentalsore.admin.dis_customer[self.name]
        st=rentalsore.admin.dict_rent[self.name][-1]
        str2=f"""BILLING SYSTEM FOR BIKE RENTALS
quantity of bikes rented\tprice\ttime\n
{self.quanti}\t\t\t\t{rentalsore.admin.price[rentalsore.admin.dict_rent[self.name][2]]}\t{rentalsore.admin.dict_rent[self.name][2]}\n*********************************************\n
Bikes being returned\t\t{number_bike}\t{(number_bike*int(rentalsore.admin.price[st].split("$")[0])-((number_bike*int(rentalsore.admin.price[st].split("$")[0]))*dis))}
*********************************************
total amount for all the bikes rented is={self.balance}
*********************************************
Your remaining rented bikes ={self.quanti-number_bike}
Your remaining balance is={self.balance-(number_bike*int(rentalsore.admin.price[st].split("$")[0])-((number_bike*int(rentalsore.admin.price[st].split("$")[0]))*dis))}
\n\n"""
        
        self.balance-=(number_bike*int(rentalsore.admin.price[st].split("$")[0])-((number_bike*int(rentalsore.admin.price[st].split("$")[0]))*dis))
        return str2


  