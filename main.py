file = open("My_File.txt")
contents = file.read()
print(contents)
file.close()

# Another way to open a file without close function.
with open("My_File.txt") as f:
    content = f.read()
    print(content)

# Writing to a file
with open("My_File.txt", mode='a') as f:
    f.write("\nI am learning Python.")

# Writing to a new file
with open("New_File.txt", mode='w') as f:
    f.write("Hey there, this is a new file.")

# Using absolute path to open a file
with open("/Users/mohanamkavi/PycharmProjects/Txt Files/My_Text.txt") as text:
    content_text = text.read()
    print(content_text)

# Using relative path to open a file
with open("../../PycharmProjects/Txt Files/My_Text.txt") as new_text:
    content_new_text = new_text.read()
    print(content_new_text)
