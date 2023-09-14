from email import Email

# List of email's names
emails_list = []

# Opening the name's file
with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.read()

# Splitting the names into a list
names_list = names.split("\n")

# Creating emails objects, and putting inside the emails_list
for name in names_list:
    emails_list.append(Email())

# Creating the letters for each person
for index in range(len(emails_list)):
    emails_list[index].email_writer(names_list[index])