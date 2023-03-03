import random
import time
def str_pas():
    for i in range(len(str_of_pas)):
        j = random.randint(1, len(str_of_pas))
        str_of_pas.append(str_of_pas[j-1])
        str_of_pas.remove(str_of_pas[j-1])
def change_all():
    for i in range(len(all_characters)):
        j = random.randint(1, len(all_characters))
        all_characters.append(all_characters[j-1])
        all_characters.remove(all_characters[j-1])
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "=", "+", "-", "_", "\\", "|", "~",
                     "`", "[", "]", "{", "}", ";", ":", "'", '"', "<", ">", "?", ".", ",", "/"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
all_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                  "!", "@", "#", "$", "%", "^", "&", "*", "=", "+", "-", "_", "\\", "|", "~", "`", "[", "]", "{", "}", ";", ":", "'", '"', "<", ">", "?", ".", ",", "/",
                  1, 2, 3, 4, 5, 6, 7, 8, 9,
                  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count = 0
print("wellcome to password suggestion version 1.0.0\nin this program you inter your password and this program check your password for some object for example especial charcter and etc.\nand next suggest a new password")
time.sleep(5)
out = input("What do you want?\ncreat password(c) or suggest pasword(s)?\ntype c or s: ")
if out == "s":
    pas = input("Enter your own password: ")
    str_of_pas = [i for i in pas]
    print("--------------------log--------------------")
    capital_of_pas = [i for i in pas if i in capital_letters]
    if len(capital_of_pas) == 0:
        print("in your password hasn't any capital letters")
        co = random.randint(1, len(capital_letters))
        str_of_pas.append(capital_letters[co-1])
        count += 1
        str_pas()
    else:
        print("has capital letters")
    small_of_pas = [i for i in pas if i in small_letters]
    if len(small_of_pas) == 0:
        print("in your password hasn't any small letters")
        co = random.randint(1, len(small_letters))
        str_of_pas.append(small_letters[co-1])
        count += 1
        str_pas()
    special_of_pas = [i for i in pas if i in special_characters]
    if len(special_of_pas) == 0:
        print("in your password hasn't any special character")
        co = random.randint(1, len(special_characters))
        str_of_pas.append(special_characters[co-1])
        count += 1
        str_pas()
    else:
        print("has special characters")
    numbers_of_pas = [i for i in pas if i in numbers]
    if len(numbers_of_pas) == 0:
        print("in your password hasn't any number")
        co = random.randint(1, len(numbers))
        str_of_pas.append(numbers[co-1])
        count += 1
        str_pas()
    else:
        print("has number")
    if len(str_of_pas) < 5:
        if len(capital_of_pas) or len(special_of_pas) or len(numbers_of_pas) or len(small_of_pas) == 0:
            print("in your password number of characters are lower than 8")
            change_all()
            time.sleep(3)
            n = int(input("How many characters you like should the password be?"))
            n = n - len(str_of_pas)
            for i in range(n):
                j = random.randint(1, len(all_characters))
                str_of_pas.append(all_characters[j])
            str_pas()
    else:
        print("has a minimum number of characters")
    print("-------------------------------------------")
    if count >= 0:
        print("--------------------suggest--------------------")
        str_pas()
        print("my suggestion for set new password is :")
        time.sleep(5)
        for i in range(len(str_of_pas)):
            print(str_of_pas[i], end="")
    print("\n----------------------------------------------")
else:
    change_all()
    creat_pas = []
    n = int(input("How many characters you like should the password be? "))
    for i in range(n):
        j = random.randint(1, len(all_characters))
        creat_pas.append(all_characters[j])
    print("wait...")
    time.sleep(5)
    print("your password is:")
    for i in range(len(creat_pas)):
        print(creat_pas[i], end="")
