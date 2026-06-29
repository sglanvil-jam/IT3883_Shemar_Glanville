import time
from tkinter import *
from tkinter import messagebox  
from random import randint


class ButtonWrapper:
    def __init__(self, id="", row=-1, col=-1, c=""):
        self.ID = id
        self.ROW = row
        self.COL = col
        self.COLOR = c
        self.BUTTON_OBJ = None


""" Check if two labels have been clicked and if they are a match """
def check_match():
    global buttons
    clicked = []
    for b in buttons.values():
        if b.BUTTON_OBJ['relief'] == "sunken":
            clicked.append(b)
            
    if len(clicked) >= 2:
        # Check matching backgrounds
        if clicked[0].BUTTON_OBJ['bg'] == clicked[1].BUTTON_OBJ['bg']:
            # It's a match! Permanent black face up
            clicked[0].BUTTON_OBJ.configure(bg='black', relief='flat')
            clicked[1].BUTTON_OBJ.configure(bg='black', relief='flat')
        else:
            # Not a match. Turn back face down (lightgrey)
            clicked[0].BUTTON_OBJ.configure(bg='lightgrey', relief='raised')
            clicked[1].BUTTON_OBJ.configure(bg='lightgrey', relief='raised')


""" If a label is clicked, draw the hidden color """
def button_pushed(event, pushed_id):
    global buttons
    # Prevent interacting with already matched items or items currently turned face up
    if buttons[pushed_id].BUTTON_OBJ['bg'] == 'black' or buttons[pushed_id].BUTTON_OBJ['relief'] == 'sunken':
        return
        
    buttons[pushed_id].BUTTON_OBJ.configure(bg=buttons[pushed_id].COLOR, relief="sunken")
    buttons[pushed_id].BUTTON_OBJ.after(1500, check_match)


def close_options(top):
   top.destroy()


""" Save the new Row and Col values to the global game variables """
def save_options(r, c):
    global rows, cols
    if (r * c) % 2 != 0:
        messagebox.showerror("Invalid Dimensions", "Total number of tiles (Rows x Columns) must be an even number!")
        return
    
    rows = r
    cols = c
    reset_game()


""" Draw and handle the options menu """
def options():
    top = Toplevel(root)
    top.geometry("250x250")

    row_val = StringVar(value=str(rows))
    col_val = StringVar(value=str(cols))

    row = Entry(top, width=25, textvariable=row_val)
    row.pack(pady=5)

    col = Entry(top, width=25, textvariable=col_val)
    col.pack(pady=5)

    save = Button(top, text="Save", command=lambda: save_options(int(row_val.get()), int(col_val.get())))
    close = Button(top, text="Close", command=lambda: close_options(top))
    save.pack(pady=5, side=TOP)
    close.pack(pady=5, side=TOP)


""" Resets the game. Will clear, reshuffle and redraw the board """
def reset_game():
    global buttons
    for b in buttons.values():
        if b.BUTTON_OBJ:
            b.BUTTON_OBJ.destroy()

    buttons = {}  

    for i in range(rows):
        for j in range(cols):
            id = (i * cols) + j  
            b = ButtonWrapper(id=str(id), row=i, col=j)  
            
            # Using Tkinter Label with width/height and layout borders to act as a responsive Mac tile
            b.BUTTON_OBJ = Label(root, text="     ", bg="lightgrey", relief="raised", 
                                 borderwidth=4, width=8, height=4)
            
            # Bind the Mac left click event (<Button-1>) directly to our callback function
            b.BUTTON_OBJ.bind("<Button-1>", lambda event, bid=b.ID: button_pushed(event, bid))
            buttons[b.ID] = b  

    ids = list(range(rows * cols))  
    while len(ids) > 0:  
        a = ids[randint(0, len(ids) - 1)]  
        ids.remove(a)  
        b = ids[randint(0, len(ids) - 1)]  
        ids.remove(b)  
        color = colors[randint(0, len(colors) - 1)]  
        buttons[str(a)].COLOR = color  
        buttons[str(b)].COLOR = color

    for b in buttons.values():
        b.BUTTON_OBJ.configure(bg='lightgrey', relief='raised')

    for b in buttons.values():
        b.BUTTON_OBJ.grid(row=b.ROW, column=b.COL, padx=2, pady=2)


# Main Method
rows = 5
cols = 6

buttons = {}
root = Tk()
root.title("Tile Matching Game")
menubar = Menu(root)  

colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New Game', command=reset_game)
file.add_command(label='Options', command=options)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

reset_game()

root.grid_rowconfigure(0, minsize=40)
root.config(menu=menubar)
root.mainloop()
