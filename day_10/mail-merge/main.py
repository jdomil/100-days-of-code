with open("./input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

with open("./input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

for name in names_list:
    formatted_name = name.strip()
    final_letter = starting_letter.replace("[name]", formatted_name)
    with open(f"./output/ReadyToSend/letter_for_{formatted_name}.txt", mode="a") as final_file:
        final_file.write(final_letter)
