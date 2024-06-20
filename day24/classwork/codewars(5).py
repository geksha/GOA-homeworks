def fake_bin(x):
    result = ""
    num = x
    for char in num:
        if int(char) >= 5:
            result = result + "1"
        if int(char) < 5:
            result = result + "0"
    return result