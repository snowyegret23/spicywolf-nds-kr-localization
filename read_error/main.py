import re

with open("fontconfig.txt", "r", encoding="utf-8") as f:
    data = [i.strip() for i in f.readlines()]
    table_dict = {
        line[1]: line[0]
        for i in data
        if (line := i.split("=", maxsplit=1)) and len(line) == 2
    }


# print(table_dict)
while True:
    user_input = input("입력: ")
    user_input = user_input.replace("[ERROR] String ", "")
    user_input = re.sub(r" is too long \(\d+/\d+\)\.", "", user_input)
    print("출력: ", end="")
    for i in user_input:
        if i in table_dict:
            print(table_dict[i], end="")
        if i in [" ", ".", ",", "!", "?"]:
            print(i, end="")
        elif i == "|":
            print(" ", end="")
    print("\n")
