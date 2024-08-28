import random

def hangman():
    words = ['array', 'backend', 'class', 'database', 'virus']  
    word = random.choice(words)  
    guessed_letters = [] 
    tries = 6 

    while tries > 0:  
        print("\n")
        for letter in word:  
            if letter in guessed_letters:
                print(letter, end=" ")  
            else:
                print("_", end=" ") 

        if set(word) == set(guessed_letters):
            print("\n\nGewonnen!")
            break

        guess = input("\n\nRate einen Buchstaben: ").lower()  

        if guess.isalpha() and len(guess) == 1: 
            if guess in guessed_letters:
                print("Du hast diesen Buchstaben bereits geraten.")
            elif guess in word:
                guessed_letters.append(guess) 
            else:
                tries -= 1  
                print("Falsch geraten! Du hast noch", tries, "Versuche.")
        else:
            print("Ungültige Eingabe. Bitte rate einen einzelnen Buchstaben.")

    else:
        print("\n\nDu hast verloren! Das Wort war:", word)

hangman()
