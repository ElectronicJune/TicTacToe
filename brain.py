import numpy as np
from numpy import random

class memory :
    game_code = np.array(['123456789'])
    game_choice = np.array(['1','2','3','4','5','6','7','8','9'],ndmin=2)
    game_choice_p = np.array([1/9 for i in range(9)],ndmin=2)
    def possible_position(self,code):
        arr = [c for c in code if c in '123456789' ]
        return arr + ['0' for i in range(9-len(arr))]
    def add(self,code):
        if code not in self.game_code :
            self.game_code = np.concatenate((self.game_code,[code]))
            self.game_choice = np.vstack((self.game_choice,self.possible_position(code)))
            p = [1 for i in code if i in '123456789']
            p = [i/len(p) for i in p]
            p += [0 for i in range(9-len(p))]
            self.game_choice_p = np.vstack((self.game_choice_p,p))
    def react(self,code):
        self.add(code)
        index = np.where(self.game_code==code)[0][0]
        return random.choice(self.game_choice[index],p=self.game_choice_p[index],size=1)[0]