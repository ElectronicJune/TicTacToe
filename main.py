import display 
import rules
import gameplay_history
import brain
#print title 
display.print_title()

# piece info 
rules.player_piece = input('Choose a piece [O/X]: ').strip()
rules.bot_piece = 'X' if rules.player_piece!='X' else 'O'

#start outer game loop 
run_game = True
game_round = 0

while run_game :
    game_round += 1
    print('ROUND',game_round)
    game_condition = '123456789'
    
    if game_round%2 == 0 :
        # code 
        pass
    #inner game loop
    for i in range(9):
        display.print_tictactoe(game_condition)
        #code
        pass

    run_game = False if input('Play again? [Y/n]: ').lower()=='n' else True


