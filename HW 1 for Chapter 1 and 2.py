def calculate_grade(sub1, sub2, sub3, sub4, sub5):
    total_marks = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total_marks / 500 * 100
    
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'F'

# Example usage
marks = []
for i in range(1, 6):
    marks.append(int(input(f"Enter marks obtained in subject {i}: ")))

grade = calculate_grade(*marks)
print(f"Grade: {grade}")
