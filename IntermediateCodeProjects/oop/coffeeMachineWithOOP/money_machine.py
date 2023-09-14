class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_receive = 0

    def report(self):
        """Prints the current profit."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coin(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coin.")
        for coin in self.COIN_VALUE:
            self.money_receive += int(input(f"How many {coin}?: ")) * self.COIN_VALUE[coin]
        return self.money_receive

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coin()
        if self.money_receive >= cost:
            change = round(self.money_receive - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_receive = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_receive = 0
            return False