import random
class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.won = 0
        self.lost = 0
    def __repr__(self) -> str:
        info = "Name: {}\nBalance: {}, Record: {} won - {} lost".format(self.name,self.balance,self.won,self.lost)
        return info

test_player = Player("Chuj", 20)
print(test_player)