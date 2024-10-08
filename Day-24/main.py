file = open("./Input/Names/invited_names.txt", mode="r")
file2 = open("./Input/Letters/starting_letter.txt",
             mode="r")
text = file2.read()

for x in file:
    x = x.strip()
    new_text = text.replace("[name]", x)
    file_name = "letter_for_"+x
    with open(f"./Output/ReadyToSend/{file_name}.txt", mode="w") as f:
        f.write(new_text)
