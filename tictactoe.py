from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect 4 - Camilla")

ROWS, COLS = 6, 7
board = [["" for _ in range(COLS)] for _ in range(ROWS)]
buttons = {}
clicked = True  # X starts

def index_from_button(b):
    for (r, c), btn in buttons.items():
        if btn == b:
            return r, c
    return None, None

def get_column(col):
   
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "":
            return row
    return None

def find_winner(player):
   
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != player:
                continue

            # horizontal
            if c + 3 < COLS and all(board[r][c + i] == player for i in range(4)):
                return [(r, c + i) for i in range(4)]

            # vertical
            if r + 3 < ROWS and all(board[r + i][c] == player for i in range(4)):
                return [(r + i, c) for i in range(4)]

            # diagonal down-right
            if r + 3 < ROWS and c + 3 < COLS and all(board[r + i][c + i] == player for i in range(4)):
                return [(r + i, c + i) for i in range(4)]

            # diagonal down-left
            if r + 3 < ROWS and c - 3 >= 0 and all(board[r + i][c - i] == player for i in range(4)):
                return [(r + i, c - i) for i in range(4)]

    return None

def check_winner(r, c, player):
    win_coords = find_winner(player)
    if win_coords:
        # highlight winning discs
        for (rr, cc) in win_coords:
            buttons[(rr, cc)].config(bg="yellow", activebackground="yellow")
        return True
    return False

def b_click(b):
    global clicked
    _, col = index_from_button(b)

    row = get_column(col)
    if row is None:
        messagebox.showerror("Connect 4", "Column is full!")
        return

    player = "X" if clicked else "O"
    board[row][col] = player
    btn = buttons[(row, col)]
    color = "red" if player == "X" else "blue"

    # ensure color stays across platforms
    btn.config(text=player, bg=color, activebackground=color)

    if check_winner(row, col, player):
        messagebox.showinfo("Connect 4", f"Player {player} wins!")
        disable_all_buttons()
        return

    clicked = not clicked

def disable_all_buttons():
    for btn in buttons.values():
        btn.config(state=DISABLED)

def reset():
    global board, clicked
    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    clicked = True
    for btn in buttons.values():
        btn.config(text=" ", bg="SystemButtonFace", activebackground="SystemButtonFace", state=NORMAL)

# Build Buttons
count = 1
for r in range(ROWS):
    for c in range(COLS):
        btn = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda b=None: None)
        btn.config(command=lambda b=btn: b_click(b))
        btn.grid(row=r, column=c)
        buttons[(r, c)] = btn
        globals()[f"b{count}"] = btn  # b1-b42 naming
        count += 1

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

root.mainloop()
