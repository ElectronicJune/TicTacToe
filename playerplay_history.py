class history :
    list = dict()
    def add(self,code,piece_position):
        self.list[code] = piece_position
    
    def get_piece_postion(self,code):
        if code not in self.list :
            return
        return self.list[code]

    def clear(self):
        self.list = dict()