import re
txt="Some analyst say a buffet-less berkhshire hathaway could be a candidate for being broken up into multiple companies."
x=re.sub("\s","*",txt,4)
print(x)