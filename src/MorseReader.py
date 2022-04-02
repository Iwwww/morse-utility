from AudioGenerator import generate
import re
from time import sleep

isRunningFlag = False

def isRunning():
    global isRunningFlag
    return isRunningFlag

def playMorse(morse,
         small_duration=100, middle_duration=300,
         small_pause=50, middle_pause=250, big_pause=500,
         tone=500,
         level=0,
         print_log=False, print_pauses=False):

    def get_key(dict, value):
        for key, v in dict.items():
            if v == value:
                return key

    global isRunningFlag
    isRunningFlag = True

    small_pause = small_pause / 1000
    middle_pause = middle_pause / 1000
    big_pause = big_pause / 1000

    # Log
    if print_log == True:
        print("small pause = {}".format(small_pause))
        print("middle pause = {}".format(middle_pause))
        print("big pause = {}".format(big_pause))
        print("\n")

    # Log
    if print_log == True:
        print('All morse: [{}]'.format(morse) )

    # Log
    if print_log == True:
        print("Run status =", isRunning())



    words = re.split(r"/", morse) # Split words
    # Log
    if print_log == True:
        print("Words:", words)
    for word in words:

        # Log
        if print_log == True:
            print("word:", word)
        letters = re.split(r" ", word) # Split letters

        for letter in letters:

            # Log
            if print_log == True:
                print("letter:", letter)
            for sing in str(letter): # Split sings

                # Log
                if print_log == True:
                    print("sing:", sing)

                # Play sound
                if sing == '.':
                    generate(tone, small_duration, level=level)
                elif sing == '-':
                    generate(tone, middle_duration, level=level)

                sleep(small_pause)
            sleep(middle_pause)
        sleep(big_pause)

        # Log
        if print_log == True:
            print("\n")

    isRunningFlag = False

    # Log
    if print_log == True:
        print("Run status =", isRunning())

if __name__ == "__main__":
    morse = "... ------/... "
    playMorse(morse, print_log=True, level=0)