
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)
 
with open("./Input/Letters/starting_letter.docx") as letter_file:
    letters = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/Letter_for_{stripped_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)    




