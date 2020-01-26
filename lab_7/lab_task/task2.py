def numline(filename):
    file=open(filename,'r')
    linelist=file.readlines()
    file.close()
    print(linelist)
    return print(len(linelist))

numline("text_file.txt")