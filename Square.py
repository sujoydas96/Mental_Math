import random 

try:
    while True:
        for i in range(21,30):
            print(str(i) + " X " + str(i))
            answer = int(input())
            if(answer == (i*i)):
                print("SUCCESS!!")
            else:
                print("FAIL!! correct answer: " + str(i*i)) 
except:
    print("Irrelevent key has been pressed. Exiting Program")
    
    