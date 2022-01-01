f = open("englishwords.txt","r")
word_list = []
for line in f:
    stripword = line.strip()
    word_list.append(stripword)

#print(len(word_list))   

# Now we have converted the words txt into a list with 6900 words
import random
import string
char_list = (string.ascii_uppercase)
char_list = set(char_list)



def getavalidword():
    result_word = random.choice(word_list)

    while " " in result_word or "-" in result_word:
        result_word =  random.choice(word_list)
    return result_word

# now we get a word without " " or "-"

def hangman():
    used_letter = set()
    my_word = getavalidword()
    my_word = my_word.upper()
    my_word_letter = set(my_word)

    while len(my_word_letter) > 0:
        print('The letters you have guessed: ' + " ".join(used_letter))
        current_word = [letter if letter in used_letter else "-" for letter in my_word]
        print('The word is ' + ' '.join(current_word))
        guess_letter = input('Guess a letter (Quit the game[QT]):\n').upper()
        # if the guess is correct
        hidden_letter = my_word_letter - used_letter
        if guess_letter in hidden_letter:
            used_letter.add(guess_letter)
            my_word_letter.remove(guess_letter)
            print(f'Your guess is correct {guess_letter} is in the word')
        # if the guess is the letter you have guessed
        elif guess_letter in used_letter:
            print(f'You have guessed letter {guess_letter}, try a different one')
        # if the guess is new and not in the word
        elif guess_letter in char_list:
            used_letter.add(guess_letter)
            print(f'Please try again, {guess_letter} is not in the word')
        else:
            print('Invalid input, please input a letter')
        
    current_word = ''.join([letter if letter in used_letter else "-" for letter in my_word])    
    print(f'Congratulations! You have guessed the correct word {current_word} !')    






















hangman()    