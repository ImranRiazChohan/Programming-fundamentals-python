
def distribution(filename):
    file=open(filename,'r')
    for f in file:
        splt=f.split()
        for word in splt:
            print(word)
                
    file.close()     
distribution('grades.txt')        