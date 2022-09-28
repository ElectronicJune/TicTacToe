class history :
    list = dict()
    def add(self,code,piece,piece_position):
        self.list[code] = (piece,piece_position)
    def get_piece(self,code):
        if code not in self.list :
            return
        return self.list[code][0]
    def get_piece_postion(self,code):
        if code not in self.list :
            return
        return self.list[code][1]


