# c11ex09.py
#   gpasort using decorated list


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
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)

    # build decorated list
    decorated = []
    for s in data:
        decorated.append((s.gpa(),s))

    # sort
    decorated.sort()

    # extract raw list
    data = []
    for (gpa,s) in decorated:
        data.append(s)
        
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

# Note: use of Python list comprehensions makes this technique easier:
def main2():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)

    # use list comprehension to build decorated list
    decorated = [(s.gpa(),s) for s in data]
    decorated.sort()

    # use list comprehension again to rebuild student list
    data = [s for (gpa,s) in decorated]
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
    
