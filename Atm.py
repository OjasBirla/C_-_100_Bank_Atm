class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def balanceInquiry(self):
        print("You Have ______ Rs in you account")

    def changePin(self):
        new_pin = input("Enter the new Pin ")
        print("Your Pin number has been changed")

card_number = input("Eneter your Card Number ") 
pin_number = input("Eneter your Pin Number ") 

card = Atm(card_number, pin_number)

card.balanceInquiry()
card.changePin()