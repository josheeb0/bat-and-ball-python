import time 

num= int(input("Which Plus Table? "))

for i in range (1,11):
    answer=num+i
    guess=input("guess the number you dummy: ")
    if int(guess) == answer:
        print("well done you did it ;) owo")
    else:
        print("stupid dont ever try this again you useless dipstick |:<")
    print(1,"x",i,"=",answer)
    time.sleep(2)
