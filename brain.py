import numpy as np
from numpy import random
import rules

class memory :
    game_code = np.loadtxt('game_code.csv',delimiter=',',dtype='S')
    game_choice = np.loadtxt('game_choice.csv',delimiter=',',dtype='S')
    game_choice_p = np.loadtxt('game_choice_prob.csv',delimiter=',')
    def possible_position(self,code):
        arr = [c for c in code if c in '123456789' ]
        return arr + ['0' for i in range(9-len(arr))]
    def add(self,code):
        if code not in self.game_code :
            self.game_code = np.concatenate((self.game_code,[code]))
            self.game_choice = np.vstack((self.game_choice,self.possible_position(code)))
            p = [2 for i in code if i in '123456789']
            p += [0 for i in range(9-len(p))]
            self.game_choice_p = np.vstack((self.game_choice_p,p))
    def react(self,code):
        self.add(code)
        index = np.where(self.game_code==code)[0][0]
        return random.choice(self.game_choice[index],p=[x/(self.game_choice_p[index].sum()) for x in self.game_choice_p[index]],size=1)[0]
    def learn(self,code,position,winner):
        index = np.where(self.game_code==code)[0][0]
        if winner == rules.bot_piece:
            self.game_choice_p[index][np.where(self.game_choice[index]==position)[0][0]] += 4
        elif winner == rules.player_piece :
            for i in range(9):
                if self.game_choice[index][i] != position :
                    if self.game_choice[index][i] != '0' :
                        self.game_choice_p[index][i] += 1
        else :
            self.game_choice_p[index][np.where(self.game_choice[index]==position)[0][0]] += 2
    def learn_from_player(self,code,position,winner):
        self.add(code)
        index = np.where(self.game_code==code)[0][0]
        if winner == rules.player_piece:
            self.game_choice_p[index][np.where(self.game_choice[index]==position)[0][0]] += 4
        elif winner == rules.bot_piece :
            for i in range(9):
                if self.game_choice[index][i] != position :
                    if self.game_choice[index][i] != '0' :
                        self.game_choice_p[index][i] += 1
        else :
            self.game_choice_p[index][np.where(self.game_choice[index]==position)[0][0]] += 2
    def save_arr_tofile(self):
        np.savetxt('game_code.csv',self.game_code , delimiter=',')
        np.savetxt('game_choice.csv',self.game_choice , delimiter=',')
        np.savetxt('game_choice_prob.csv',self.game_choice_p , delimiter=',')
