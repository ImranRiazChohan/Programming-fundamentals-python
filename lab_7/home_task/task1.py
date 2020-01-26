def Status(filename):
    file=open(filename)
    content=file.read( )
    file.close()
    split_file=content.split()
    count = 0
    for line in open(filename).readlines(  ):
       count += 1
    print("Number of line:",count) #no of line 
    print("character:",len(content)) #count character
    print("words:",len(split_file)) #count words    
Status("text_file.txt")
