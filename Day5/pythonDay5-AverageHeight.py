# Average Height Calculator with Loops
i = 0 
summ = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    i += 1
    summ += student_heights[n]
Average = round(sum / i)
# Another way is to use len() and sum() functions on the list. 
print(f"Average Height is {Average}.")