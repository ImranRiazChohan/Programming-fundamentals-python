class House:
    def __init__(self,house_no,location,size,rooms,price):
        self.house_no=house_no
        self.loc=location
        self.size=size
        self.rooms=rooms
        self.price=price

class Banglows(House):
    def banglowss_condtion(self,floors):
        self.floor=floors
    def banglows_info(self):
        return ("HOUSE TYPE BANGLOWS\nbanglows_no:{}\nlocation:{}\nsize:{}Yards\nrooms:{},no_of_floor:{}\nprice:{}".format(self.house_no,self.loc,self.size,self.rooms,self.floor,self.price))           

class Appartment(House):
    def Appartment_condtion(self,floor):
        self.floor=floor
    def Appartment_info(self):
        return ("HOUSE TYPE APPARTMENT \nflat_no:{}\nlocation:{}\nsize:{}Yards\nrooms:{},floor:{}th floor\nprice:{}".format(self.house_no,self.loc,self.size,self.rooms,self.floor,self.price))    
class FarmHouse(House):
    def FarmHouse_condition(self,name,no_of_pool,no_of_bath):
        self.pool=no_of_pool
        self.name=name
        self.no_of_bath=no_of_bath
    def FarmHouse_info(self):
            return ("HOUSE TYPE FARMHOUSE\nName:{}\nfarm_no:{}\nlocation:{}\nsize:{}Yards\nrooms:{},no_of_pool:{}\nprice:{}\nno_of_bath:{}".format(self.name,self.house_no,self.loc,self.size,self.rooms,self.pool,self.price,self.no_of_bath)) 

b1=Banglows("b/327","DHA",240,6,'2.5 crore')
b1.banglowss_condtion(2)
print(b1.banglows_info()) 

f1=Appartment("c23","gulistan-e-johar",120,4,"20 lakh")
f1.Appartment_condtion(5)
print(f1.Appartment_info())

frm1=FarmHouse("i/30","gulshan-e-maymar",2000,4,"20 crore")
frm1.FarmHouse_condition("Ideal_farm",2,4)
print(frm1.FarmHouse_info())