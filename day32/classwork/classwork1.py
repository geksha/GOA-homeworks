
def get_count(sentence):
    count = 0
    for i in ["a", "e", "i", "o", "u"]:
        count += sentence.count(i)
    return count