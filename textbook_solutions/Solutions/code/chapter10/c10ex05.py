# c10ex05.py.py
#    Program to compute GPA

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + gradePoint * credits
        self.hours = self.hours + credits

    def gpa(self):
        return self.qpoints/self.hours

def main():
    print("This program computes a student's GPA")
    student = Student("No Name", 0, 0)

    infoStr = input("Enter course info (gradepoints, credits): ")
    while infoStr != "":
        data = infoStr.split(",")
        gp, credits = float(data[0]), float(data[1])
        student.addGrade(gp, credits)
        infoStr = input("Enter course info (gradepoints, credits): ")

    print("\nSummary of courses entered:")
    print("hours:", student.getHours())
    print("GPA:", student.gpa())

if __name__ == '__main__':
    main()

