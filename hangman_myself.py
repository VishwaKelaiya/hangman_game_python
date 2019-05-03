import time
import random

wordlist = 'WORDLIST.txt'


def get_word():
    with open(wordlist, 'r') as f:
        list_for_words = [char for char in f]

    random.shuffle(list_for_words)

    return list_for_words[0].rstrip('\n').strip()


def no_of_attempts():
    n_a = input('Enter no of incorrect attempts: [1-10] \n')

    try:
        n_a = int(n_a)
        if 1 <= n_a <= 10:
            return n_a
        else:
            print(f'{n_a} is not between 1 to 10  Please enter number between 1 to 10\n')
    except ValueError:
        print(f'{n_a} is not integer please enter integer\n')
    except:
        print('Some error occured!!\n')


if __name__ == '__main__':
    print('Starting Hangman Game......\n')
    time.sleep(1)

    attempts = no_of_attempts()
    print('Getting random word for you to guess\n')
    word = get_word()
    word.lower()
    word.rstrip('\n')
    l_w = ['-']*len(word)
    l_misses = set()
    l_correct = set()

    while(attempts > 0):

        print('Word: '+ ''.join(l_w))
        if ''.join(l_w) == word:
            print(f"You have got the word!!! It's {word}")
            break

        guess = input('Guess a letter:\n')
        guess.lower()


        if guess not in l_misses and guess not in l_correct:
            if guess in word:
                print(f'{guess} is in the word!')
                l_correct.add(guess)
                for i in range(len(word)):
                    if guess == word[i:i+len(guess)]:
                        l_w[i:i+len(guess)] = guess

            else:
                print(f'{guess} is not in the word!')
                attempts -= 1
                l_misses.add(guess)
                print(f'You have {attempts} left\n')
        else:
            print(f'You have already guessed this letter {guess}\n')

    if attempts == 0:
        print(f'You have finished all your attempts!! The word was {word}. Try again')




