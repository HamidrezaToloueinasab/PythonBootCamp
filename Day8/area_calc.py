# area calculator 
# 1 can covers 5 m^2 of wall
import math
def paint_calc(height,width,cover):
    n = height * width / cover
    m = math.ceil(n)
    print(f"You will need {m} cans of paint.")
test_h = int(input("height of the wall?"))
test_w = int(input("width of the wall?"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
