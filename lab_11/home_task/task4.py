class Toyota:
    def __init__(self,color,price,model):
        self.color=color
        self.price=price
        self.model=model

class Fortuner(Toyota):
    def fortuner_info(self):
        type="Saloon"
        manufacturing_year='2017'
        return ("\n\nMODEL:{0}\nCOLOR:{1}\nPRICE:{2}\nMANUFACTURING_YEAR:{3}\nTYPE:{4}".format(self.model,self.color
        ,self.price,manufacturing_year,type))

class COROLLA(Toyota):
    def corolla_info(self):
        type="SPORTS"
        manufacturing_year='2014'
        return ("\n\nMODEL:{0}\nCOLOR:{1}\nPRICE:{2}\nMANUFACTURING_YEAR:{3}\nTYPE:{4}".format(self.model,self.color
        ,self.price,manufacturing_year,type))

class PRIUS(Toyota):
    def prius_info(self):
        type="LUXURY"
        manufacturing_year='2018'
        return ("\n\nMODEL:{0}\nCOLOR:{1}\nPRICE:{2}\nMANUFACTURING_YEAR:{3}\nTYPE:{4}".format(self.model,self.color
        ,self.price,manufacturing_year,type))

c1=COROLLA("red",1200000,"gli")
print(c1.corolla_info())


p1=PRIUS("mate_grey",2500000,"p5")
print(p1.prius_info())

f1=Fortuner("red",5000000,'f1')
print(f1.fortuner_info())