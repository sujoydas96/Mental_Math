import random 

count = 0
while True:
    a = int(random.choice([11,12,13,14,15,16,17,18,19]))
    count = count + 1
    print("Count = " + str(count))	
    print(str(a) + " X " + str(a))
    answer = int(input())
    if(answer == (a*a)):
        print("SUCCESS!!")
    else:
        print("FAIL!! correct answer: " + str(a*a))