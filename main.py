import random as rn

print("Guess the random word!")

attempts = int(input("How many attempts do you want?"))

words = ["bulka", "telefon", "bereza", "sliva"]
session_word = rn.choice(words)
session_list = [i for i in session_word]
session_guess = ['*' for i in range(len(session_word))]

counter = 0

while True:
    letter = input("Please enter your letter or word: ")
    if letter in session_list and letter != session_word:
        ind = session_list.index(letter)
        session_guess[ind] = letter
        session_list[ind] = "*"
        print(f"Nice shot, here what we have: {session_guess}, keep going!")
        counter += 1
        if ''.join(session_guess) == session_word:
            print(f"That's it, your word is {session_word} !")
            break
    elif letter == session_word:
        print(f"That's it, your word is {session_word} !")
        break
    elif attempts == 0:
        print("Not this time, homie:(")
    else:
        print(f"I do apoligize, there is no '{letter}' in here.")
        attempts -= 1
        continue
