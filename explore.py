import rules
import botplay_history
import brain
bot_history = botplay_history.history()

# piece info 
rules.player_piece = 'O'
rules.bot_piece = 'X' 

bot = brain.memory()

def bot_play(code):
    position = bot.react(code)
    bot_history.add(code,position)
    return code[:int(position)-1] + rules.bot_piece + code[int(position):]
def bot2_play(code):
    position = bot.react(code)
    bot_history.add(code,position)
    return code[:int(position)-1] + rules.player_piece + code[int(position):]
while input('Explore 1000 rounds? [Y/n] ').lower()=='y' :
    for i in range(1000):
        game_condition = '123456789'
        #inner game loop
        inner_game_round = 0
        while not rules.is_gameover(game_condition):
            if inner_game_round%2==0:
                game_condition = bot_play(game_condition)
            else :
                game_condition = bot2_play(game_condition)
        #brain learn
        round = 0
        for key in bot_history.list :
            if round%2==0:
                bot.learn(key,bot_history.list[key],rules.winner(game_condition))
            else :
                bot.learn_from_player(key,bot_history.list[key],rules.winner(game_condition))
        bot_history.clear()
        bot.compress_data()

bot.save_arr_tofile()


