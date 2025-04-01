import random
MAX_NUM = 50
MIN_NUM = 1
MAX_ATT = 10
def intro()-> None:
    print("Welcome to the number guessing game!\nYou will have 10 attempts to guess the number correctly")
    print("Ready??")
    for count in range(1,4): 
        print(count)
    print("GO!")

def play() -> None:
    num = random.randint(MIN_NUM, MAX_NUM)
    guess = []
    attempt = 0
    intro()

    while attempt!= MAX_ATT:
        try:
            g = int(input("Enter your guess\n>_ "))
        except ValueError:
            print("Try an int")

        if g == num:
            print("You guessed the number in ", attempt+1," attempts")
            return
        elif g in guess:
            print("Already guessed this number!\n")
        elif g>num:
            print(f"The num is less than {g}")
            attempt+=1
            print(MAX_ATT-attempt," attempts left\n")
        elif g< num:
            print(f"The num is more than {g}")
            attempt+=1
            print(MAX_ATT-attempt," attempts left\n")

        guess.append(g)
    print(f"GAME OVER\nThe correct num was {num}")
    return

if __name__ == "__main__":
    play()
