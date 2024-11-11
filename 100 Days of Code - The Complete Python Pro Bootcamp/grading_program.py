# creating dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


# Create an empty dictionary called student_grades.
student_grades = {}

# loop to add the grades to student_grades dictionary
for names in student_scores:
    score = student_scores[names]
    if score >= 91:
        score = "Outstanding"
    elif score >= 81:
        score  = "Exceeds Expectations"
    elif score >= 71:
        score = "Acceptable"
    elif score <= 70:
        score = "Fail"
        
    student_grades[names] = score


print(student_grades)
