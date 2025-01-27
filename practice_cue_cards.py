import os
import json
import time
import random

def introduce_game():
    print("Let's begin studying!")
    time.sleep(1)
    print("This is a timed activity... Go as fast as you can!")
    time.sleep(1)
    print("Ready?")
    time.sleep(1)
    print("GO!")

file_path = "./saved_spanish_cue_cards.json"

def is_file_empty():
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        return True


if not os.path.exists(file_path):
    print("Sorry there is no cue card file to study. Please create a cue card file to begin studying.")
else:
    file_is_empty = is_file_empty()
    if file_is_empty:
        print("Sorry there are no words saved in your cue cards. Please add cue cards to begin studying.")
    else:
        introduce_game()
        with open(file_path, "r") as f:
            inv_cue_cards = json.load(f)
            cue_cards = {v: k for k, v in inv_cue_cards.items()}
            initial_cue_cards_length = len(cue_cards)

        time_begin = time.time()
        guess_number = 0
        correct_answers = 0

        continue_translating = True
        while continue_translating:
            random_spanish_word = random.choice(list(cue_cards.keys()))
            # random_english_word = random.choice(list(cue_cards.values()))
            answer = input("Translate " + random_spanish_word + ": ")
            guess_number += 1
            answer = answer.capitalize()
            if answer == cue_cards[random_spanish_word]:
                print("Correct!")
                correct_answers += 1
                del cue_cards[random_spanish_word]
                if len(cue_cards) == 0:
                    continue_translating = False
    
            else:
                print("Incorrect. Moving on... ")

        time_end = time.time()
        duration = time_end - time_begin
        duration = round(duration, 2)
        score = (correct_answers/guess_number)*100
        score = round(score)
        score = " (" + str(score) + "%)"
        print("All done!")
        print("You completed " + str(initial_cue_cards_length) + " cue cards in " + str(duration) + " seconds.")
        print("You scored " + str(correct_answers) + "/" + str(guess_number) + " guesses" + score)



        

    
