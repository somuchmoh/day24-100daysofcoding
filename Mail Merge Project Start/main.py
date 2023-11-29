# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter = open("./Input/Letters/starting_letter.txt")
line = letter.readlines()
names = open("./Input/Names/invited_names.txt")
name = names.readlines()
updated_names = []
for a_name in name:
    new_name = a_name.strip("\n")
    updated_names.append(new_name)

name_list = []
for i in range(0, len(updated_names)):
    new_line = line[0].replace('Dear [name],\n', f'Dear {updated_names[i]},\n')
    name_list.append(new_line)

for each_name in range(0, len(name_list)):
    with open(f"./Output/ReadyToSend/letter_for_{name_list[each_name]}", mode='a') as new_letter:
        new_letter.write(name_list[each_name])
        for i in range(1, len(line)):
            new_letter.write(line[i])























