import random
import casino_player
class Game:
    def __init__(self, name, min_bet, max_bet, picks_quantity):
        self.name = name
        self.pool = [min_bet, max_bet]
        self.picks = self.add_picks(picks_quantity)

    def __repr__(self) -> str:
        info = "Name: {}\nPool: {}$-{}$, Picks: {}".format(self.name,self.pool[0],self.pool[1],self.picks)
        return info
    
    def add_picks(self,quantity):
        picks = []
        print("NOW ADD PICK OPTIONS:")
        for index in range(quantity):
            new_pick = input("PICK {}:".format(index))
            picks.append(new_pick)
        return picks

    def play_game(self, player, bet, pick):
        correct_pick = self.picks[random.randint(0,len(self.picks)-1)]
        prize = 0
        if pick == correct_pick:
            print(correct_pick + " WINS!!!")
            prize = bet * 2
            print("YOU WIN " + str(prize) + "$!!!\n")
            casino_player.Player.change_balance(player, prize)
            casino_player.Player.change_record(player, "W")
            print(player)
        else:
            print("YOU'VE LOST!!!\n")
            casino_player.Player.change_record(player, "L")
            print(player)
