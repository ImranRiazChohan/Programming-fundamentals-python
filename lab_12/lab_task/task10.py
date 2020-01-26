#NAMESPACE TASK

count =5 # global 
def some_method():
    global count #local global
    count=count+1
    print(count)
some_method()    