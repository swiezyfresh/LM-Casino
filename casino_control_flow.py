import casino_game
import casino_player

player = casino_player.Player.add_player()
ruletka = casino_game.Game("Ruletka", 10, 100, 3)


game_request = True
while game_request == True:
    bet, pick = casino_player.Player.place_bet(player,ruletka.pool,ruletka.picks)
    ruletka.play_game(player, bet, pick)
    input_game_request = input("DO YOU WANT TO PLAY AGAIN? (Y/N)")
    if input_game_request == "N":
        game_request = False
