# Practice with basic file manipulation

invite_name = ""
START_LETTER_PATH = "./Input/Letters/starting_letter.docx"
NAMES_PATH = "./Input/Names/invited_names.txt"
send_letter_path = f"./Output/ReadyToSend/letter_for_{invite_name}.docx"
new_letter = ""

new_name_list = []


#Save names to a list
with open(NAMES_PATH) as file:
    names = file.readlines()

#Save letter to a list
with open(START_LETTER_PATH) as file:
    letter = file.readlines()

#Create a new list with no new lines after each name
for name in names:
    new_name_list.append(name.strip())

#Turn the original letter from a list into a string variable
for each in letter:
    new_letter += each

#Create the final letters for each person
for each in new_name_list:
    invite_name = each
    final_letter = new_letter.replace("[name]", invite_name)
    with open(f"./Output/ReadyToSend/letter_for_{invite_name}.docx", mode="w") as file:
         file.write(final_letter)