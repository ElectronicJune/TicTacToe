def is_gameover(code):
    for i in range(3):
        if code[i] == code[i+3] == code[i+6]:
            return True
    for i in range(3):
        if code[i*3] == code[i*3+1] == code[i*3+2]:
            return True
    if code[0] == code[4] == code[8] or code[2] == code[4] == code[6] :
        return True
    return False

def winner(code):
    for i in range(3):
        if code[i] == code[i+3] == code[i+6]:
            return code[i]
    for i in range(3):
        if code[i*3] == code[i*3+1] == code[i*3+2]:
            return code[i]
    if code[0] == code[4] == code[8] or code[2] == code[4] == code[6] :
        return code[4]
    return '-1'

