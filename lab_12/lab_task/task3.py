import re
str="Some analyst say a buffet-less berkhshire hathaway could be a candidate for being broken up into multiple companies."
x=re.findall("in to ",str) #it find two different value in one parameter
print(x)