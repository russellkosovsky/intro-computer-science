#program to create a class called Student and a main program that will test it


class Student:
    """ This class has the following instance variables.
            name: a string holding the student's last name,
            id: a unique integer identifying the student
            courseList: a list of strings, each string representing
                a course the student is enrolled in """


    ##define constructor that takes 3 arguments: studName, studID, studCourseList
    """ Constructor - takes name, id, and courseList - 
    default for courseList is the empty list """
    # add body for constructor
    def __init__(self, studName, studID, studCourseList = []):
        self.name = studName
        self.id = studID
        self.courseList = studCourseList


    def setCourseList(self, newList):
        """changes courseList to the new list of courses"""
        ##add body of the method
        self.courseList = newList


    def addCourse(self, name):
        """adds a course to the list"""
        ##add body of the method
        self.courseList.append(name)


    def printInfo(self):
        """prints out student information"""
        ##add body of the method
        print("Student Name:",self.name)
        print("Student ID:",self.id)
        print("Student Courses:",self.courseList)


    def changeName(self, newName):
        """changes name to the newName"""
        ##add body of the method
        self.name = newName


#main function
def main():

    #create a student
    stu1 = Student('Jones',12345,['COM110', 'HIS112','DAN100'])
    stu1.addCourse('HIS101')
    stu1.printInfo()
    
    #create another student
    stu2 = Student('Gonzalez',65432)
    stu2.printInfo()
    stu2.setCourseList(['MAT112','BIO207','PSY122'])
    stu2.printInfo()
    stu2.changeName("Martinez")
    stu2.printInfo()


if __name__ =='__main__':
    main()

''' what is this?
You could import the class to another program
    (from StudentClass0 import *)

But we do not what the class tester (main) to run when imported into another program
because of this conditional, main will be called only when this program is run directly 
and not when its imported into another program

if class is imported to another program, __name__ would == the name of the module (in this case, StudentClass0)
'''
