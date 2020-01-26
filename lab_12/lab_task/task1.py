import re  #import regular expression
txt="some analyst say a buffets-less Berkshire Hathaway could be a candidate for bieng broken up into multiple companies."
x=re.search("^some.companies$",txt) #its search the pattern
print(x)