family_contact={"Abou":"0321-2091450","ammi":"0331-2357677","my_number":"0318-00145706","bhai":"0332-3818671","wahab":"0321-2345321",'rafique':"0333-2345644","tosif bhai":"0347-1243412","asif bhai":"0331-6454343","arif bhai":"0345-7889632"}

def delete_member(member):
    family_contact.pop(member)
    return print(family_contact)
delete_member("rafique")        