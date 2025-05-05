# c07ex2.py
#    quiz grader using decision

def main():
    print("Quiz Grader\n")
    score = float(input("Enter the score (0-5): "))
    if score < 2:
        grade = "F"
    elif score < 3:
        grade = "D"
    elif score < 4:
        grade = "C"
    elif score < 5:
        grade = "B"
    else:
        grade = "A"
    print("Grade is", grade)

if __name__ == '__main__':
    main()

    
