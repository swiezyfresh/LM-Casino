import random
import casino_game
class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.won = 0
        self.lost = 0
    
    def __repr__(self) -> str:
        info = "Name: {}\nBalance: {}, Record: {} won - {} lost".format(self.name,self.balance,self.won,self.lost)
        return info
    
    def add_player():
        input_correct = False
        while input_correct == False:
            print("Please state your ### name and initial $$$ balance: \n")
            new_player_name = input("### Name: ")
            new_player_balance = input("$$$ Balance: ")
            try:
                new_player = Player(new_player_name, float(new_player_balance))
                input_correct = True
            except ValueError:
                print("Name must be a String, initial balance must be an Int!")
        return new_player
    
    def change_balance(self, amount):
        self.balance += amount
    
    def change_record(self, result):
        if result.upper() == "W":
            self.won += 1
        if result.upper() == "L":
            self.lost += 1
    
    def place_bet(self, pool, options):
        input_correct = False
        while input_correct == False:
            print("\n")
            print("MINIMUM BET: {} | MAXIMUM BET: {}".format(pool[0], pool[1]))
            print("\nPLACE YOUR BET BELOW: ")
            input_bet = input("Bet amount ($): ")
            print("\nGAME PICK OPTIONS: " + str(options))
            print("PLACE YOUR PICK BELOW: ")
            input_pick = input("Pick choice (#): ")
            try:
                print("YOUR BET: {} | YOUR PICK: {}".format(input_bet,input_pick))
                bet = int(input_bet)
                pick = str(input_pick)
                if self.balance - bet >= 0 and pick in options:
                    self.change_balance(-bet)
                    input_correct = True
                else:
                    print("WRONG PICK, CHOOSE FROM OPTIONS")
                    print("NOT ENOUGH MONEY ON YOUR ACCOUNT, PLACE LOWER BET!")
            except ValueError:
                print("INPUT CORRECT VALUES! BET MUST BE AN INTEGER, PICK MUST BE STRING!")
            print("\n")
        print("\n")
        return float(bet), str(pick)

#test_player1 = Player.add_player()
