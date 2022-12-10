# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
yes = True
while yes:
    name = input("Enter the name: ")
    letter = [n for n in name]
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    dict = {row.letter: row.code for(index, row) in data.iterrows()}
    # print(dict["a"])
    try:
        list = [dict[l.upper()] for l in letter]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(list)
        yes = False


