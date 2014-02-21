"""
CleanMeUp - an exercise in reading bad code and writing good code.

Refactor this code so it's readable, testable (bonus points for writing tests),
and has sensibly named functions with clear purpose.

The overall behaviour of the program should be the same - you are *only* to
change the implementation, not the behaviour.

Submit your solution in a Pull Request.

"""
import random
name = raw_input("What is your name? :: ")
print("Ok, hello there " + name)
possible_numbers = []
for i in range(3):
    possible_numbers.append(random.randint(0, 1000))
while len(possible_numbers) > 0:
    secret_number = possible_numbers.pop()
    number_guessed_yet = False
    tries = 0
    print("starting a new round")
    while not number_guessed_yet:
        guess = raw_input(name + ", guess what the number might be :: ")
        guess = int(guess)
        if guess > secret_number:
            print("No, that number is too big")
        elif guess < secret_number:
            print("No, that number is too small")
        elif guess == secret_number:
            print("That's right, the number is " + str(guess))
            number_guessed_yet = True
print("bye bye")
