"""
Leila Lopez Marks
10/22/2020
Battleship
"""

def board():
    for i in range(8):
        print(vertical[0])
        if i < 2:
            print(horizontal[0])


print("Welcome to Battleship!")
num_of_players = input("Choose the number of players. Valid inputs are: 0,1, or 2")
print("You have chosen ", num_of_players, "players")

red_or_blue = input("Chose red or blue: ").upper() # Input for red or blue
if red_or_blue == 'red':
    print(f"Player 1 is red and player 2 is blue")
else:
    print("Player 1 is blue and player 2 is red")

board()

def player_1_turn():
  player1_row = input("player 1 pick your row")
  player1_col = input("player 1 pick your col")

  int_player1_row = int(player1_row)
  int_player1_col = int(player1_col)
  print("Player 1 picked", int_player1_row, int_player1_col)


myArr = ["0"]*8
print(myArr)

myArr[4] = "X"
print(myArr)
board = [
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
    [" ", "", " "," "," "," ", " ", " "],
]
print(f'''
    0 1 2
   0 {board[0][0]}|{board[0][1]}|{board[0][2]} 
    -------------
   1 | |
    ---------------
   2 | |
''')
board = [
[
    ["~", "~", "~","~","~","~", "~", "~"],
    ["~", "~", "~","~", "~","~", "~","~"],
    ["~", "~", "~", "~", "~", "~", "~", ],
    ["~", "~", "~", "~", "~", "~", "~", ],
    ["~", "~", "~", "~", "~", "~", "~", ],
    ["~", "~", "~", "~", "~", "~", "~", ],
    ["~", "~", "~", "~", "~", "~", "~", ],
    ["~", "~", "~", "~", "~", "~", "~", ],
]

def winCondition():
    if board[0][0] == board[0][1] and board [0][0] == board [0][2]:
    print(board[0][0], "is the winner cols")

    elif board[0][0] == [1][0] and board[0][0] == board[2][0]:
    print(board[0][0], "is the winner row")
    else:
       print("keep playing")
winCondition()


def drawBoard():
    print(f'''
        0 1 2 3 4 5 6 7  
       _______
    0 | {board[0][0]}|{board[0][1]}|{board[0][2]} |
      | -+-+- | 
    1 | {board[1][0]}|{board[1][1]}|{board[1][2]} |
      | -+-+- |                                    
    2 | {board[2][0]}|{board[2][1]}|{board[2][2]} | 
      | -+-+- |
    3 | {board[3][0]}|{board[3][1]}|{board[3][2]} |
      | -+-+- | 
    4 | {board[4][0]}|{board[4][1]}|{board[4][2]} |
      | -+-+- | 
    5 | {board[5][0]}|{board[5][1]}|{board[5][2]} |
      | -+-+- | 
    6 | {board[6][0]}|{board[6][1]}|{board[6][2]} |
      | -+-+- | 
    7 | {board[7][0]}|{board[7][1]}|{board[7][2]} |
      | -+-+- | 
       -------
    ''')

def game_play():
    player_1_turn()
    drawBoard()
    winCondition()