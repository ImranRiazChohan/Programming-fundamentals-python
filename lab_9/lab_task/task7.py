my_top_student={"hassan ",'ali','saboor','umair','kamran'}
print("my top scoring student in programming are:",my_top_student)
print("oh I guess i miss one student let me add his name too")
print('prevously i have added:'+str(len(my_top_student))+"student in my list")
my_top_student.add("ali khan")
my_top_student.add('fazal')
print("thanks i have remember him")
print('Now my top student are:',my_top_student)
print("Now after adding i have:"+str(len(my_top_student))+"student of my list")
print("oh  i guess i have added one student name with similar name let me remove his name.")
my_top_student.remove("ali khan")
print("Now my top student name after removing extra name are:",my_top_student)
print("now after removing i have : "+str(len(my_top_student))+"students in my list")
my_top_student.discard('fazal')
print("now after removing i have :"+str(len(my_top_student))+" student in my list")
print(my_top_student)