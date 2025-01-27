from googletrans import Translator
translator = Translator()
cue_cards_list = {}

def validate(question):
    while True:
        answer = input(question)
        if answer == "no" or answer == "No":
            return False
        elif answer == "yes" or answer == "Yes":
            return True
        else:
            print("Invalid response.")


continue_add = True
while continue_add:
    word = input("Enter an English word to translate in Spanish: ")
    word = word.capitalize()
    spanish_word = translator.translate(word, src = "en", dest ="es").text
    spanish_word = spanish_word.capitalize()
    print("In Spanish, " + word + " is " + spanish_word)
    cue_cards_list[word] = spanish_word

    continue_add = validate("Do you want to add more? (yes/no): ")
    if continue_add:
        print("Okay! Let's translate more words... ")
    
print("Here are the words we've added to your cue cards: ")
for i, words in enumerate(cue_cards_list):
    print(str(i + 1) + ": " + str(words) + ": " + cue_cards_list[words])

import os
import json

save_file = validate("Do you want to save this to your cue cards file? ")
if save_file:
    file = "saved_spanish_cue_cards.json"
    if os.path.exists(file):
        same_file = validate("Do you want to add to your existing cue cards file? (yes/no): ")
        if same_file:
            with open(file, "r") as f:
                file_size = os.path.getsize(file)
                if file_size == 0:
                    json.dump(cue_cards_list, f, ensure_ascii=False, indent=4)
                else:
                    existing_words = json.load(f)
                existing_words.update(cue_cards_list)
            with open(file, "w") as f:
                json.dump(existing_words, f, ensure_ascii=False, indent=4)
            print("The words have been added to you cue cards!")
        else:
            with open(file, "w") as f:
                json.dump(cue_cards_list, f, ensure_ascii=False, indent=4)
            print("Okay, we created a fresh cue card file with those words")
    else:
        with open(file, "w") as f:
            json.dump(cue_cards_list, f, ensure_ascii=False, indent=4)
        print("Okay, we created a fresh cue card file with those words")
else:
    print("Okay, we will not save those to your cue cards.")
