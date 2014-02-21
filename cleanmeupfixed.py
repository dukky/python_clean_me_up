
import random

class RandomNumberGame(object):

    """
    Constructor for RandomNumberGame class
    """
    def __init__(self, games_to_play, name, max_num):
        self.games_to_play = games_to_play
        self.name = name
        self.max_num = max_num
        self.possible_numbers = []
        for i in range(games_to_play):
            self.possible_numbers.append(random.randint(0, self.max_num))

    """
    Play a game
    """
    def play(self):
        while(len(self.possible_numbers) > 0):
            current_number = self.possible_numbers.pop()
            self.play_round(current_number)
        print("bye bye")


    """
    Play a round
    """
    def play_round(self, current_number):
        print("starting a new round")
        guessed = False
        while not guessed:
            guess = int(raw_input(self.name + ", guess what the number might be :: "))
            if guess == current_number:
                guessed = True

            message = {
                0  : "That's right, the number is " + str(guess),
                1  : "No, that number is too big",
                -1 : "No, that number is too small",
            }[self.validate_guess(guess, current_number)]
            print(message)

    """
    Validate the guess
    """
    def validate_guess(self, guess, current_number):
        if guess == current_number:
            return 0
        elif guess > current_number:
            return 1
        elif guess < current_number:
            return -1

if __name__ == '__main__':
    name = raw_input("What is your name? :: ")
    randomnumbergame = RandomNumberGame(3, name, 1000)
    randomnumbergame.play()
