import random 

try:
    while True:
        first = int(input("Enter the starting number : "))
        last = int(input("Enter the ending number : "))

        for i in range(first,last):
            print(str(i) + " X " + str(i))
            answer = int(input())
            if(answer == (i*i)):
                print("SUCCESS!!")
            else:
                print("FAIL!! correct answer: " + str(i*i)) 
except:
    print("Irrelevent key has been pressed. Exiting Program")
    
    