import pandas
data = pandas.read_csv("nato_alphabet2.csv")
# convert csv file to dict in python use dictionary comprehension
# {keyword:value for namekeyword in data}
convert_dict = {row.letter:row.code for (index, row) in data.iterrows()}
def generator():
    user_word_typing = input("Enter a word: ").upper()
    try:
        # list comprehension [keyword for key in object]
        output = [convert_dict[letter] for letter in user_word_typing]
    except KeyError:
        print("Just a name or word. Dont use number or any type different!")
        generator()
    else:
        print(output)
generator()