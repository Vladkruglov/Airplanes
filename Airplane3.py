import random
from tkinter import *
import time

def fly():
    t = Tk()
    c = Canvas(t,height = 700,width = 700)
    c.pack()
    colors = ['blue', 'red', 'green', 'yellow', 'brown', 'black', 'silver', 'magenta', 'purple', 'cyan', 'orange', 'lightgreen']
    for i in range(0,20):
        rancolor = random.choice(colors)
        ran_x = random.randint(0,700)
        ran_y = random.randint(0,700)
        ransec_x = random.randint(0,700)
        ransec_y = random.randint(0,700)
        c.create_line(ran_x, ran_y, ransec_x, ransec_y, fill = rancolor)
        c.create_oval(ransec_x - 5, ransec_y - 5, ransec_x + 5, ransec_y + 5, fill = rancolor, outline = rancolor)
    timechoice = [2,3,4,5,6]
    tim = random.choice(timechoice)
    t.mainloop()
    
if __name__ == "__main__":
    fly()
