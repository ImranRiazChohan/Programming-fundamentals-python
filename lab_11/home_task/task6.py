class person:
    def __init__(self,first_name,last_name,gender,nic,address):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.nic=nic
        self.address=address

class student(person):
    def student_get_roll_no(self,roll_no):
        self.roll_no=roll_no
        return roll_no

    def student_get_semester(self,semester):
        self.semester=semester
        return semester  
    def student_info(self):
        return ("student_name:{}\ngender:{}\nnic:{}\naddress:{}\nroll_number:{}\nsemester:{}".format(self.first_name+self.last_name,self.gender,self.nic,self.address,self.roll_no,self.semester))

class teacher(person):
    def teacher_get_course(self,course_name):
        self.course_name=course_name
        return course_name
    def teacher_qualification(self,qualification):
        self.qualification=qualification
        return qualification 
    def teacher_info(self):
        return("name:{}\ngender:{}\nnic:{}\naddress:{}\ncourse_name:{}\nqualification:{}".format(self.first_name+self.last_name,self.gender,self.nic,self.address,self.course_name,self.qualification))
st1=student("usama","chohan","male","00000-00000000-0","abc street")
st1.student_get_roll_no('17b-043-cs')
st1.student_get_semester('4th')
print(st1.student_info())        

t1=teacher("sir usman ","arif","male",'4221-2313131-9',"gulshan")
t1.teacher_get_course("programming_fundamentals")
t1.teacher_qualification("master in AI")
print(t1.teacher_info())