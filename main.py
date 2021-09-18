from translate import Translator

print("Type the language to translate to. \nAvailable languages include: \n japanese \n chinese ")

while True:
    set_language = input("Language:  ")

    if set_language == "japanese":
        translator= Translator(to_lang="ja")

        try:
            with open("input_file.txt", mode="r") as in_file:
                text = in_file.read()
                translation = translator.translate(text)
                print(translation)

                with open("output_file.txt", mode="wb") as out_file:
                    out_file.write(translation.encode())

        except FileNotFoundError as err:
            print("File does not exist in directory")
        break

    elif set_language== "chinese":
        translator= Translator(to_lang="zh")

        try:
            with open("input_file.txt", mode="r") as in_file:
                text = in_file.read()
                translation = translator.translate(text)
                print(translation)

                with open("output_file.txt", mode="wb") as out_file:
                    out_file.write(translation.encode())

        except FileNotFoundError as err:
            print("File does not exist in directory")
        break

    else:
        print("Error: Language is not available or does not exist")
        continue

