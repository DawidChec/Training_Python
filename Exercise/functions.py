
def find_average_marks(mark):
    average = sum(marks) / len(marks)
    return average

def calculate_the_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >=50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 10, 80, 100]

average_marks = find_average_marks(marks)
print("Your average degree is", average_marks)

grade = calculate_the_grade(average_marks)
print("Your grade is:", grade)