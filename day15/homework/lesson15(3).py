def is_palindrom(word):
    reversed_word = ''

    for i in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[i]

    print(reversed_word == word) 

is_palindrom("luka")   