class Plant:
    def __init__ (self,plant_name,plant_location,plant_type,plant_import_type,plant_price):
        self.name=plant_name
        self.location=plant_location
        self.type=plant_type
        self.imported=plant_import_type
        self.price=plant_price

class Fruit(Plant):
    def info (self):
        if self.type == "sweet":
            print("its a sweet fruit")
            return ("Name:{}\nLocation:{}\nType:{}\nPrice:{}\nImport From:{}".format(self.name,self.location,self.type,self.price,self.imported))
        elif self.type == 'poisonous' :
            print("its a poisonous fruit")
            return ("Name:{}\nLocation:{}\nType:{}\nPrice:{}\nImport From:{}".format(self.name,self.location,self.type,self.price,self.imported))
        elif self.type == "sour":
            print("its a sour fruit")
            return ("Name:{}\nLocation:{}\nType:{}\nPrice:{}\nImport From:{}".format(self.name,self.location,self.type,self.price,self.imported))    

f1=Fruit('mango','mirpur khas','poisonous','local','250 rupees/kg')
print(f1.info())        
print()
f2=Fruit("orange","sukkur","sour","local","120 dozen")
print(f2.info())