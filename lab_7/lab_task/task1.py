def numWords(filename):
    file=open(filename,'r')
    content=file.read()
    file.close()

    word_list=content.split()
    print(word_list)
    return print(len(word_list))

numWords("text_file.txt")