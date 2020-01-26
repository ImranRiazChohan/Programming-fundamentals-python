love_crickte={"usama","wasi","hassan","ahsan","basit",'talha',"malik","shoaib","haris","farhan","wahab"}
love_hockey={"usama","haris","ahmed","wahab","umair","khalid","mansoor","imran","ibad","ali",'furqan',"khuzaima"}
#for universal set
print("universal set: ",love_crickte|love_hockey)
#for who love both 
print("who love both: ",love_crickte&love_hockey)
#for who love hockey
print("who love hockey: ",love_hockey-love_crickte)
#for who love cricket
print("who love cricket: ",love_crickte-love_hockey)