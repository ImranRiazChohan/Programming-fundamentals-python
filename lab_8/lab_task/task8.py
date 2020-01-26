dict1={'name':"jibran","age":"12","class":"7th","DOB":"16-jun-2000"}
dict1["Age"]="13"
dict1["School"]="PECHS SCHOOL"
print("Age:{}".format(dict1["Age"]))
print("School:{}".format(dict1["School"]))

dict1["freind1"]="wasi"
dict1["freind2"]="hassan"
dict1["freind3"]="basit"

print("friend1:{}".format(dict1["freind1"]))
print("friend2:{}".format(dict1["freind2"]))
print("friend3:{}".format(dict1["freind3"]))

del dict1['name']
print(dict1)