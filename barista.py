class Barista(object):
    def make_coffee(self, withmilk=False):
        if(withmilk):
            return "Here is your coffee with milk"
        else:
            return "Here is your regular coffee"

    def make_tea(self, withsugar=False):
        if(withsugar):
            return "Your sweet tea is ready"
        else:
            return "Your tea is ready"

    def get_payment(self, cash=True):
        if(cash):
            return "Thank you for the tip!"
        else:
            return "Let me get the POS terminal"

    def present_menu(self, regular=False):
        if(regular):
            return "Would you like the usual?"
        else:
            return "Would you like coffee or tea?"
