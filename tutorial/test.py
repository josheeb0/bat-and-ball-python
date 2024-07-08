import random
random_number = random.randint(1,10)

# print ("cheats :)")
# print (random_number)

users_number = 0
counter = 0

while random_number != users_number:
    print ("")
    users_number = int(input("Guess the number!: "))
    if random_number != users_number:
        counter += 1
        print("")
        print(f"Guess counter: {counter} - you are incorrect try again")
    else:
        counter += 1
        print("")
        print(f"Guess counter: {counter} - you are correct well done")
