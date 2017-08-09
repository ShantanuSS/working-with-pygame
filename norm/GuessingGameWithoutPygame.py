from random import randint
x=randint(1,9)
guess=-1;
print("guess the no. below 10")
while guess!=x:
    guess=int(input("Guess"))
    if guess !=x:
        print("wrong guess")
    else:
        print("guessed correctly")
        
