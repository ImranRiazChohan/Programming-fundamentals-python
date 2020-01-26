import re
file=open("Text_RE.txt","r")
file_text=file.read( )
#split word
spl=re.split('\s',file_text)
print(spl)
#calculate number of vowels
small=re.findall("[a,e,i,o,u]",file_text)
capital=re.findall("[A,I,O,U,E]",file_text)
print("small_vowels: ",len(small))
print("capital_vowel: ",len(capital))
print("total number of vowels: ",(len(capital)+len(small)))
#find similar words

#replace small character  with capital
replace=re.sub("[a-z]\w+","[A-z]\w+",file_text)
print(replace)
#count total words after spliting
print("total words:",len(spl))