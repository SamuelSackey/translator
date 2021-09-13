from translate import Translator
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