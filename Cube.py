import random 

count = 0

try:
    while True:
        a = int(random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
        count = count + 1
        print("Count = " + str(count))	
        print(str(a) + " X " + str(a) + " X " + str(a))
        answer = int(input())
        if(answer == (a*a*a)):
            print("SUCCESS!!")
        else:
            print("FAIL!! correct answer: " + str(a*a*a))

except:
    print("Irrelevant key has been pressed. Exiting program")
