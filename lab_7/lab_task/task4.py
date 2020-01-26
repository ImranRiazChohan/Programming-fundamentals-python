def myGrep(filename,string_target):
    file=open(filename,'r')
    content=file.read()
    file.close()
    if string_target=='Line': #print every line in a single line
        for line in content:
            print(line,end="")    
    elif string_target=="char":
        for line in content:
            print(line,end=',')
    else:
        print("asdas")        
               
myGrep("text_file.txt","Line")

