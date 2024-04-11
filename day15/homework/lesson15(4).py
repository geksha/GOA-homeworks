#mexute davaleba

def my_replace(word,char1,char2):
    replaced_word = ''

    for i in word:
        if i == char1:
            replaced_word = replaced_word + char2
        else:
            replaced_word = replaced_word + i
            
    print(replaced_word)

my_replace("Gega Devdariani", "i", "d")