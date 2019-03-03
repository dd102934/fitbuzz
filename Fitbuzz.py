a = 0
while a < 100:
    a += 1
    if a % 15 == 0:
        print(a,"Fitbuzz")
    elif a % 3 == 0:
        print(a,"Fit")
    elif a % 5 == 0:
        print(a,"buzz")
print("finish")
