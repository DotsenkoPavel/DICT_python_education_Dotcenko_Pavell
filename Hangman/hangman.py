import random
print("HANGMAN")
print("The game will be available soon.")
words = ['python', 'javascript', 'html', 'java']
english_letters = list("qwertyuiopasdfghjklzxcvbnm")
answer_prog = random.choice(words)  # python
word_list = list(answer_prog) # [p,y,t,h,o,n]
user_word_list_null = "-" * len(answer_prog)    # ------
user_list = list(user_word_list_null)    # [-,-,-,-,-,-]
user_used = []
start = 'play'
count = 0


def res():
    global start, user_list, word_list
    if user_list != word_list:
        print("You lost!")
    else:
        print("You guessed the word!")
        print("You survived!")
    start = str(input('Type "play" to play the game, "exit" to quit:'))


def double():
    global word_list, answer_user, user_list
    if word_list.count(answer_user) >= 2:
        index = word_list.index(answer_user)
        user_list[index] = answer_user
        word_list[index] = '-'