def abc(filename):
    file=open(filename,'r') #existing file
    other=open("censored.txt",'w') #new file
    for s in file: 
        splt=s.split()
        for words in splt:
            if len(words)==4:
                line=s.replace(words,"****")
        other.write(line)
    file.close()
    other.close()
abc("text_file.txt")
