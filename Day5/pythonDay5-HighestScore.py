# Highest Score Exercise 
# Don't use max() and min() functions on the list
max_score = 0
student_scores = input("Input a list of student scores. ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")