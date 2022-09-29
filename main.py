import display 
import rules
import botplay_history
import brain
history = botplay_history.history()
#print title 
display.print_title()

# piece info 
rules.player_piece = input('Choose a piece [O/X]: ').strip()
rules.bot_piece = 'X' if rules.player_piece!='X' else 'O'

#start outer game loop 
run_game = True
game_round = 0

bot = brain.memory()
#functions
def bot_play(code):
    position = bot.react(code)
    history.add(code,position)
    return code[:int(position)-1] + rules.bot_piece + code[int(position):]
def player_play(code):
    while True :
        position = input('Piece position: ').strip()
        if len(position)==1 and position.isdigit() and (position in code):
            break
    return code[:int(position)-1] + rules.player_piece + code[int(position):]
while run_game :
    game_round += 1
    print('ROUND',game_round)
    game_condition = '123456789'
    #inner game loop
    inner_game_round = 1
    while True:
        if inner_game_round% 2 == (0 if game_round%2==0 else 1) :
            game_condition = bot_play(game_condition)
        else:
            display.print_tictactoe(game_condition)
            game_condition = player_play(game_condition)
        if rules.is_gameover(game_condition):
            display.print_tictactoe(game_condition)
            if rules.winner(game_condition)==rules.player_piece:
                print('YOU WIN')
            elif rules.winner(game_condition)==rules.bot_piece:
                print('YOU LOSE')
            else :
                print('DRAW')
            break
        inner_game_round += 1
    #brain learn
    history.clear()
    run_game = False if input('Play again? [Y/n]: ').lower()=='n' else True


