translation_dict = {
    "hello": "merhaba",
    "world": "dünya",
    "apple": "elma",
    "computer": "bilgisayar",
    "ussr": "sovyetler biriliği ",
    "book": "kitap"
}


word = input("Enter an English word: ").lower()

if word in translation_dict:
    print(f"The Turkish translation of '{word}' is: {translation_dict[word]}")
else:
    print("This word is not in the dictionary.")
