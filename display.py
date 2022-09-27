def print_tictactoe(code):
    grid = '''  {}  |  {}  |  {}  
-----+-----+-----
  {}  |  {}  |  {}  
-----+-----+-----
  {}  |  {}  |  {}  '''
    print(grid.format(code[0],code[1],code[2],code[3],code[4],code[5],code[6],code[7],code[8]),end='')

def print_title():
  print('+---------------------------+')
  print('| TIC TAC TOE GAME with bot |')
  print('+---------------------------+\n')
