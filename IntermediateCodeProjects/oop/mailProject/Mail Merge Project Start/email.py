# Constants
PLACEHOLDER = "[name]"


# Email class
class Email:

    def __init__(self):
        with open("./Input/Letters/starting_letter.txt", mode="r") as file:
            self.mensagem = file.read()

    # Function that writes the letter
    def email_writer(self, name):
        self.mensagem = self.mensagem.replace(PLACEHOLDER, name)
        with open(f"./Input/Letters/letter_for_{name}.txt", mode="w") as file:
            file.write(self.mensagem)

    # Gets
    def get_mensagem(self):
        return self.mensagem
