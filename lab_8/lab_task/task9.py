dict1={'name': 'jibran', 'age': '12', 'class': '7th', 'DOB': '16-jun-2000', 'Age': '13', 'School': 'PECHS SCHOOL', 'freind1': 'wasi', 'freind2': 'hassan', 'freind3': 'basit'}
print(dict1)
for key,val in dict1.items():
    print("{}:{}".format(key,val))
dict1.popitem()
print("afte pop from the dictionary:\n{}".format(dict1))    