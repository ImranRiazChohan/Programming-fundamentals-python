def numchars(filename):
    file=open(filename,'r')
    content=file.read()
    file.close()
    return print(len(content))

numchars("text_file.txt")