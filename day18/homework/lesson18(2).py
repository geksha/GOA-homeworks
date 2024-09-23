def descending_order(num):
    num = str(num)
    num = list(num)
    num = sorted(num)
    num = reversed(num)
    num = "".join(num)
    return int(num)

print(descending_order(42145))