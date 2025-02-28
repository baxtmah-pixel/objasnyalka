meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "КРИПОВЫЙ": "страшный",
            "АГРИТЬСЯ": "злиться"
            }
while True:
    command = int(input("выбери команду:", "1. добаить слово","2. удалить слово", "3. непонятное слово"))
    if command == 3:
        word = input("введите непонятное вам слово").upper()
        if word in meme_dict.keys():
        
            print("значение:", meme_dict[word])
        else:
            print("вы ошиблись")
    elif command == 1:
        print(meme_dict)
        slovo = input("введите слово").upper()
        ojasnenie = input("введите значение слова")
        meme_dict[slovo] = ojasnenie
        print(meme_dict)
    elif command == 2:
        print(meme_dict)
        delete = input("введите слово которое хотите удалить").upper()
        del meme_dict[delete]
        print(meme_dict)
    else:
        print("вы ошиблись числом")
