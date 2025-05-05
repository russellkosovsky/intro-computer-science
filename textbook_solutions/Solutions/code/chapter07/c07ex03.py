# c07ex03.0y
#   Exam grader using decisions

def main():
    print("Exam Grader\n")
    score = float(input("Enter the score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("The grade is", grade)

if __name__ == '__main__':
    main()
