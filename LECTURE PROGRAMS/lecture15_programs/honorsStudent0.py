"""program to create a class called Student and a main program that will test it"""

        
class Student:
    """This class has the following instance variables.
            name: a string holding the student's last name,
            id: a unique integer identifying the student
            courseList: a list of strings, each string representing
                a course the student is enrolled in"""

    def __init__(self, studName, studID, studCourseList = []):
        """Constructor - takes name, id, and courseList -
            default for courseList is the empty list"""
        self.name = studName
        self.id = studID
        self.courseList = studCourseList

    def setCourseList(self, newList):
        """changes courseList to the new list of courses"""
        self.courseList = newList

    def addCourse(self, name):
        """adds a course to the list"""
        self.courseList.append(name)
        
    def printInfo(self):
        """prints out student information"""
        print('------------------------------------')
        print ("Courses for " + self.name + " (ID# " + str(self.id) + "): ")
        print('------------------------------------')
        if self.courseList!=[]:
            for course in self.courseList:
                print(course)
        else:
            print("No courses for " + self.name)

        print()

    def changeName(self, newName):
        """changes name to the newName"""
        self.name = newName



class HonorsStudent(Student):
    """create a subclass of Student called HonorsStudent"""

    def __init__(self, name, id, majorName, titleName, classlist = []):
        """method to construct an nonors student"""
        ## here write constructor body
        Student.__init__(self, name, id, classlist)
        self.major = majorName
        self.title = titleName


    def printInfo(self):
        """method to print out info for an honors student"""
        ##print out student information
        Student.printInfo(self)
        print(self.major)
        print(self.title)
        

def main():

    #create a student
    stu1 = Student('Jones',89765,['COM110', 'HIS112','DAN100'])
    stu1.addCourse('HIS101')
    stu1.printInfo()

    #create another student
    stu2 = Student('Gonzalez',65432)
    stu2.printInfo()
    stu2.setCourseList(['MAT112','BIO207','PSY122'])
    stu2.printInfo()

    #create honors student
    stu3 = HonorsStudent('Smith', 56473, 'Computer Science:', 'Graphics', ['COM209', 'ART300'])
    stu3.printInfo()
       

if __name__ =='__main__':
    main()
                  
