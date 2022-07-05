
class admin:
    admin_code=""
    dis_customer={}
    no_of_bikes=10 #initially number of bikes we have
    dict_rent={}
    enti=[]
    price={"hour":"5$","day":"20$","week":"60$"}
    
    
    #for showing available number of bikes that can be rented amd price list for rent 

    @classmethod
    def no_of_bike_nprice(cls):
        return f"number of bikes available\t: {cls.no_of_bikes}\nprice={cls.price}\noffer= Group Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price"

    #for increasing the number of bikes available

    @classmethod
    def add_no_of_bikes(cls,numbe):
        cls.no_of_bikes+=numbe
    
    @classmethod
    def display_invent(cls):
        return f"nuber of bikes remaining are {cls.no_of_bikes}"
    