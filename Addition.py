import random 

count = 0
try:
    while True:
        a = int(random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
        b = int(random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))
        #a = int(random.choice([2,3,4,5,6,7,8,9]))
        #b = int(random.choice([2,3,4,5,6,7,8,9]))
        count = count + 1
        print("Count = "+str(count))	
        print(str(a) + " + " + str(b))
        answer = int(input())
        if(answer == (a+b)):
            print("SUCCESS!!")
        else:
            print("FAIL!! correct answer: " + str(a+b))


except:
    print("An irrelevant key has been pressed. Exiting program")
