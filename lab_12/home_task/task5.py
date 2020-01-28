# This function modifies global variable 's' 
def f(): 
    global name
    print (name)
    name = "Imran riaz chohan"
    print (name)  
  
# Global Scope 
name = "usama chohan" 
f() 
print (name) 