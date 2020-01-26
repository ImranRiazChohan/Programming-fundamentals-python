def hexASCII():
    dic={}
    for val in range(97,123):
        dic[chr(val)]=hex(val)
    print(dic)
hexASCII()        