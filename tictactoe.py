from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect 4 - Camilla")

ROWS, COLS = 6, 7
board = [["" for _ in range(COLS)] for _ in range(ROWS)]
buttons = {}
clicked = True  # X starts

# ---------- Helper functions ----------
def index_from_button(b):
    """Find row, col of a clicked button"""
    for (r, c), btn in buttons.items():
        if btn == b:
            return r, c
    return None, None

def get_column(col):
    """Return the lowest empty row in this column, or None if full"""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "":
            return row
    return None

def check_winner(r, c, player):
    """Check 4 in a row from (r, c)"""
    def count_dir(dr, dc):
        rr, cc, cnt = r, c, 0
        while 0 <= rr < ROWS and 0 <= cc < COLS and board[rr][cc] == player:
            cnt += 1
            rr += dr
            cc += dc
        return cnt

    for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
        total = count_dir(dr, dc) + count_dir(-dr, -dc) - 1
        if total >= 4:
            return True
    return False

# ---------- Game logic ----------
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
    btn.config(text=player, bg="red" if player == "X" else "blue")

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
        btn.config(text=" ", bg="SystemButtonFace", state=NORMAL)

# ---------- Build Buttons ----------
count = 1
for r in range(ROWS):
    for c in range(COLS):
        btn = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                     bg="SystemButtonFace", command=lambda b=None: None)
        btn.config(command=lambda b=btn: b_click(b))
        btn.grid(row=r, column=c)
        buttons[(r, c)] = btn
        globals()[f"b{count}"] = btn  # keep your b1..b42 naming
        count += 1

# ---------- Menu ----------
my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

root.mainloop()
