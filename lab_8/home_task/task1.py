family={"father":"riazuddin","mother":"naeema","brother":"umar"}
maternal_grandparent={"paternal_grand father":"abdul hakeem","paternal_grand mother":"zaitoon"}
paternal_grandparent={"maternal_grand_father":"abdul aziz","maternal_grand_mother":"raisa"}
uncle_aunt_maternal={"paternal_uncles":["salahuddin",'saleemuddin','ghani','hafiz moin'],"paternal_aunties":['huma','rani',"gulshan"]}
uncle_aunt_paternal={"maternal_uncles":['siddique','nasir'],'maternal_aunties':['noshin','bilo','najo']}

family.update(maternal_grandparent)
family.update(paternal_grandparent)
family.update(uncle_aunt_maternal)
family.update(uncle_aunt_paternal)

for key,val in family.items():
    print("{}:{}".format(key,val))