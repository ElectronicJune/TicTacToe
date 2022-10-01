import numpy as np
from numpy import float64, random
import rules

class memory :
    game_code = np.loadtxt('game_code.csv',delimiter=',',dtype='S')
    game_choice_p = np.loadtxt('game_choice_prob.csv',delimiter=',',dtype='i')
    def to_pb_code(self,code):
        code = code.replace(rules.bot_piece,'b').replace(rules.player_piece,'p')
        return code
    def add(self,code):
        if code not in self.game_code :
            self.game_code = np.concatenate((self.game_code,[code]))
            p = [int(i in '123456789')*2 for i in code]
            self.game_choice_p = np.vstack((self.game_choice_p,p))
    def react(self,code):
        code = self.to_pb_code(code)
        self.add(code)
        index = np.where(self.game_code==code)[0][0]
        return random.choice([c for c in self.game_code[index]],p=[x/(self.game_choice_p[index].sum()) for x in self.game_choice_p[index]],size=1)[0]
    def learn(self,code,position,winner):
        code = self.to_pb_code(code)
        index = np.where(self.game_code==code)[0][0]
        if winner == rules.bot_piece:
            self.game_choice_p[index][int(position)-1] += 4
        elif winner == rules.player_piece :
            for i in range(9):
                if i+1 != int(position) :
                    if self.game_choice_p[index][i] != 0 :
                        self.game_choice_p[index][i] += 1
        else :
            self.game_choice_p[index][int(position)-1] += 2
    def learn_from_player(self,code,position,winner):
        code = self.to_pb_code(code)
        self.add(code)
        index = np.where(self.game_code==code)[0][0]
        if winner == rules.player_piece:
            self.game_choice_p[index][int(position)-1] += 4
        elif winner == rules.bot_piece :
            for i in range(9):
                if i+1 != int(position) :
                    if self.game_choice_p[index][i] != 0 :
                        self.game_choice_p[index][i] += 1
        else :
            self.game_choice_p[index][int(position)-1] += 2
    def compress_data(self):
        for i in range(len(self.game_choice_p)) :
            gcd = np.gcd.reduce(self.game_choice_p[i])
            self.game_choice_p[i] = np.divide(self.game_choice_p[i],np.array([gcd for j in range(9)]))

    def save_arr_tofile(self):
        np.savetxt('game_code.csv',self.game_code , delimiter=',',fmt='%s')
        np.savetxt('game_choice_prob.csv',self.game_choice_p , delimiter=',')
