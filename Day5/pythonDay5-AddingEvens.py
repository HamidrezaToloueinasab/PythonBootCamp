# Adding Even numbers from 1 to 100 inclusively 
sum_even = 0
for number in range(0, 101, 2):
    sum_even += number
print(sum_even)

# another way: 
# total = 0
# for number in range(1,101):
#    if number % 2 == 0:
#      total += number
# print(total)