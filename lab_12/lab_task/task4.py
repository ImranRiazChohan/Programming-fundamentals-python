import re
txt="Some analyst say a buffet-less berkhshire hathaway could be a candidate for being broken up into multiple companies."
x=re.search("\s",txt)
print("the first white space character is located in the position!",x.start())