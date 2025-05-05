# c11ex03.py
#    A program to sort student information into GPA order.

from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students


def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), 
              file=outfile)
    outfile.close()
                      

def main():
    print("This program sorts student grade information")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)

    sortBy = input("Enter field to sort on (gpa, name, or credits): ")
    order = input("Ascending or Descending order? ")
    
    choice = sortBy[0].lower()
    if choice == 'n':
        print("Sorting by name.")
        data.sort(key=Student.getName)
    elif choice == 'c':
        print("Sorting by credits hours")
        data.sort(key=Student.getHours)
    else:
        print("Sorting by GPA.")
        data.sort(key=Student.gpa)

    ochoice = order[0].lower()
    if ochoice == 'd':
        print("Descending order")
        data.reverse()
    else:
        print("Ascending order")
    
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
