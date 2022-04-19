def solution():
    words = input().strip().split()
    isnopair = True
    lastword = ""

    for word in words:
        if word.isalpha() and lastword.isalpha():
            print(lastword + " " + word)
            isnopair = False
        lastword = word
    if isnopair:
        print("Мало слов!")

solution()
