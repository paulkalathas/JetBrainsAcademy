class Coffee:
    def __init__(self, water, milk, coffee_beans, cost):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cost = cost


class CupOfCoffee:
    espresso = Coffee(250, 0, 16, 4)
    latte = Coffee(350, 75, 20, 7)
    cappaccino = Coffee(200, 100, 12, 6)


class Resources:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def prepare(self, coffee):
        # check resource availability.  If available, make coffee, if not, prompt message
        water = self.water - coffee.water
        milk = self.milk - coffee.milk
        coffee_beans = self.coffee_beans - coffee.coffee_beans
        disposable_cups = self.disposable_cups - 1

        if water < 0:
            print('Sorry, we do not have enough water')
        elif milk < 0:
            print('Sorry, we do not have enough milk')
        elif coffee_beans < 0:
            print('Sorry, we do not have enough coffee beans')
        elif disposable_cups < 0:
            print('Sorry, we do not have enough disposable cups')
        else:
            print()
            print("I have enough resources, making you a coffee!")
            self.water = water
            self.milk = milk
            self.coffee_beans = coffee_beans
            self.disposable_cups = disposable_cups

    def make(self):
        # Customer input to select coffee and then make coffee
        selection = input('What do you want to buy? 1 - Espresso, 2 - Latte, 3 - Cappaccino, back - to main menu: ')
        if selection == '1':
            self.prepare(CupOfCoffee.espresso)
            self.money += 4
        elif selection == '2':
            self.prepare(CupOfCoffee.latte)
            self.money += 7
        elif selection == '3':
            self.prepare(CupOfCoffee.cappaccino)
            self.money += 6
        elif selection == 'back':
            return CoffeeMachine.run_machine

    def fill(self):
        self.water += int(input('How many ml of Water do you want to add into the Coffee Machine?'))
        self.milk += int(input('How many ml of Milk do you want to add into the Coffee Machine?'))
        self.coffee_beans += int(input('How many g of Coffee Bean do you want to add into the Coffee Machine?'))
        self.disposable_cups += int(input('How many disposable cups do you want to add into the Coffee Machine?'))

    def take_money(self):
        """Gives all money to all who enter the command 'take' :)"""
        print(f'I gave you ${self.money}')
        self.money = 0

    def remaining(self):

        # Current amount of resources available in the Coffee Machine
        print('The Coffee Machine has.')
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")


class CoffeeMachine:
    def __init__(self):
        self.cup_of_coffee = CupOfCoffee()
        self.resources = Resources()
        self.affordable_cups = 0
        self.run_machine()

    def run_machine(self):
        """Basic program loop and processing user commands"""
        while True:
            print()
            action = input('Write action (buy, fill, take, remaining, exit):')
            print()
            if action == 'buy':
                self.resources.make()
                print()

            elif action == 'fill':
                self.resources.fill()
                print()

            elif action == 'take':
                self.resources.take_money()
                print()

            elif action == 'remaining':
                self.resources.remaining()
                print()
            elif action == 'exit':
                break


coffeemachine = CoffeeMachine()
