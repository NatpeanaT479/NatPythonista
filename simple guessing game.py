import random 
num = random.randint(1,10)
attempt = 0
while attempt < 4:
    guess = int(input("Guess the number"))
    if guess == num:
        print("correct!")
        break
    if guess != num:
        print("try again!")
        attempt +=1   
print("Game ends")
