import re
str="Some analyst say a buffet-less berkhshire hathaway could be a candidate for being broken up into multiple companies."
x=re.findall("ou",str) #its find the str value pattern
print(x)