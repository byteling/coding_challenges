# https://edabit.com/challenge/yuPWwSbCGPm2KzSzx

prices = {
    "Strawberries" : "$1.50",
    "Banana" : "$0.50",
    "Mango" : "$2.50",
    "Blueberries" : "$1.00",
    "Raspberries" : "$1.00",
    "Apple" : "$1.75",
    "Pineapple" : "$3.50"
}

class Smoothie:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        print(self.ingredients)
        total = 0.00
        for fruit in self.ingredients:
            print(prices[fruit].replace("$",""))
            total += float(prices[fruit].replace("$",""))
        print('$%.2f'%total)

    def get_price(self):
        return self.get_cost() * 1.5

    def get_name(self):
        self.ingredients_sorted = sorted(self.ingredients)
        returnstring = []
        if (len(self.ingredients) > 1):
            for i in self.ingredients_sorted:
                returnstring.append(i.replace("ies", "y"))
            returnstring.append("Fusion")
        else:
            returnstring.append(self.ingredients[0])
            returnstring.append("Smoothie")
        print(" ".join(returnstring))
        return " ".join(returnstring)

class something:
    s1 = Smoothie(["Banana"])
    s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
    s2.get_cost()
    s2.ingredients
    s2.get_name()