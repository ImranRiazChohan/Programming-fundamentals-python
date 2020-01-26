def duplicate(filename):
    file=open(filename,"r")
    # content=file.read()
    word=set()
    for f in file:
        splt=f.split()
        for words in splt:
            if words in word:
                return print(True)
            word.add(words)
    else:
        return print(False)           
 
    file.close()   


duplicate('duplicate_file.txt')