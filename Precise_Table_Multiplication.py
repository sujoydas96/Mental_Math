import random 

count = 0
a = int(input("Enter the multiplication table for practice: "))

while True:
    b = int(random.choice([2,3,4,5,6,7,8,9]))
    count = count + 1
    print("Count = "+str(count))	
    print(str(a) + " X " + str(b))
    answer = int(input())
    if(answer == (a*b)):
        print("SUCCESS!!")
    else:
        print("FAIL!! correct answer: " + str(a*b))
