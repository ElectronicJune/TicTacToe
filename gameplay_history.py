class history :
    list = dict()
    def add(code,piece,piece_position):
        list[code] = (piece,piece_position)
    def get_piece(code):
        if code not in list :
            return
        return list[code][0]
    def get_piece_postion(code):
        if code not in list :
            return
        return list[code][1]

