def palindrom():

    if word == word[::-1].lower():
        print("True")
    else:
        print("False")

while True:
    word = input().lower()
    palindrom()

