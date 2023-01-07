rows = [["_", "_", "_"], #row1
        ["_", "_", "_"], #row2
        ["_", "_", "_"], #row3
]

player1_symbol = "X"
player2_symbol = "O"

def get_display():
    return f"""
  0 1 2 x
0 {rows[0][0]} {rows[0][1]} {rows[0][2]}
1 {rows[1][0]} {rows[1][1]} {rows[1][2]}
2 {rows[2][0]} {rows[2][1]} {rows[2][2]}
y
"""

def get_vertical_rows():
    vertical_rows = [[rows[0][0], rows[1][0], rows[2][0]],
                     [rows[0][1], rows[1][1], rows[2][1]],
                     [rows[0][2], rows[1][2], rows[2][2]]
    ]
    return vertical_rows

def get_diagonal_rows(): 
    diagonal_rows = [[rows[0][0], rows[1][1], rows[2][2]],
                     [rows[2][0], rows[1][1], rows[0][2]],
    ]
    return diagonal_rows

def get_turn(player, symbol):
    print(f"It's {player}'s turn ({symbol}).")
    x = int(input("Enter the position x: "))
    y = int(input("Enter the position y: "))
    rows[y][x] = symbol
    vertical_rows = get_vertical_rows()
    diagonal_rows = get_diagonal_rows()
    get_control([rows, vertical_rows, diagonal_rows], player)
    return get_display()

def get_control(control_list, player_name):
    for control in control_list:
        for row in control:
            if row[0] == row[1] and row[1] == row[2] and row[0] != "_":
                print(get_display())
                print(f"WINNER! {player_name} won the game! Congratulations.")
                exit()

print("Welcome! This is the 'Tic Tac Toe Game'.\nPlease enter the player's names.")
player1 = input("Enter the player 1 name: ")
player2 = input("Enter the player 2 name: ")
print(get_display())
for turn in range(4):
    print(get_turn(player1, player1_symbol))
    print(get_turn(player2, player2_symbol))
print(get_turn(player1, player1_symbol))
print("DRAW! There is no winner.")