
# Test with file in python3

# If was used "with" doesn't need close the file!
with open("file.txt", "w") as file:
    file.write("Hello World!!!!")
    
# If wasn't used "with", so it does necessary to close the file! 
file = open("new_text.txt", "w")
file.write("Hello World!!!!!!!!")
file.close()