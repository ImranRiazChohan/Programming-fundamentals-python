#NAMESPACE TASK

uit_1=5 #global namespace
def some_func():
    cs2=4 #local namespace
    print(cs2)
    def some_inner_func():
        se=8 #nested loacal namespace
        print(se)
print(some_func())        