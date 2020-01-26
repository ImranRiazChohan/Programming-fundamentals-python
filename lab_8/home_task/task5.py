parent_list_of_guest=['ali','imran','umar','tosif']
family_list_of_member=['usama','riaz','sofyan','ammir']
my_list_of_guest=['wahab','rafique','tosif iqbal','umair ahmed','ammir sohail']
def count_no_of_guest():
    guest=set(parent_list_of_guest+my_list_of_guest)
    totalguest=len(guest)
    family_member=set(family_list_of_member)
    family_and_guest=len(guest| family_member)
    print("total no of guest:{}".format(totalguest))
    print("family and guest are:{}".format(family_and_guest)) 

count_no_of_guest()