def is_gameover(code):
    for i in range(3):
        if code[i] == code[i+3] == code[i+6]:
            return True
    for i in range(3):
        if code[i*3] == code[i*3+1] == code[i*3+2]:
            return True
    if code[0] == code[4] == code[8] or code[2] == code[4] == code[6] :
        return True
    for i in code:
        if i.isdigit() and i!='0' :
            break
    else:
        return True
    return False
def winner(code):
    for i in range(3):
        if code[i] == code[i+3] == code[i+6]:
            return code[i]
    for i in range(3):
        if code[i*3] == code[i*3+1] == code[i*3+2]:
            return code[i*3]
    if code[0] == code[4] == code[8] or code[2] == code[4] == code[6] :
        return code[4]
    return '-1'
bot_piece = 'X' #default
player_piece = 'O' #default