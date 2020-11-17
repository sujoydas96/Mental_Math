import random 

while True:
    for i in range(11,20):
        print(str(i) + " X " + str(i))
        answer = int(input())
        if(answer == (i*i)):
            print("SUCCESS!!")
        else:
            print("FAIL!! correct answer: " + str(i*i)) 
    
    