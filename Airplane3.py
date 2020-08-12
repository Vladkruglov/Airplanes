import random
from tkinter import *
import time

def fly():
    t = Tk()
    t.title("Airplanes                                                                 0.1.release3")  
    can = Canvas(t,height = 700,width = 700)
    can.pack()
    can.create_rectangle(0,0,700,700,fill = 'yellowgreen')
    colors = ['blue', 'red', 'forestgreen', 'yellow', 'brown', 'black', 'silver', 'magenta', 'purple', 'cyan', 'orange', 'lightgreen']
    ww = 1
    r = 5
    a = 5
    e = 10
    w = 10
    we = 1
    while ww < 70:
        r = r + 10
        a = a + 10
        e = e + 10
        w = w + 10
        ww = ww + 1
        can.create_oval(r,a,e,w,fill = 'forestgreen', outline = 'darkgreen')
    e = 685
    w = 5
    r = 690
    a = 10

    while we < 70:
        r = r - 10
        a = a + 10
        e = e - 10
        w = w + 10
        we = we + 1
        can.create_oval(e,w,r,a,fill = 'forestgreen', outline = 'darkgreen')




    can.create_oval(200, 299, 143, 267, fill = 'white', outline = 'white')
    can.create_oval(600, 569, 843, 467, fill = 'white', outline = 'white')
    can.create_oval(100, 39, 125, 213, fill = 'white', outline = 'white')
    can.create_oval(567, 65, 653, 23, fill = 'white', outline = 'white')
    can.create_oval(300, 508, 400, 400, fill = 'white', outline = 'white')
    can.create_oval(100, 208, 500, 400, fill = 'white', outline = 'white')
    lehf = list() 
    rd = list() 
    for i in range(0,10):
        rancolor = random.choice(colors)
        ran_x = random.randint(0,700)
        ran_y = random.randint(0,700)
        ransec_x = random.randint(0,700)
        ransec_y = random.randint(0,700)
        can.create_line(ran_x, ran_y, ransec_x, ransec_y, fill = rancolor, width=3, arrow=LAST, dash=(9,1),activefill=rancolor, arrowshape="9 18 9")
        fjr = (ransec_x, ransec_y)
        lehf.append(fjr)
        rd.append(rancolor)

    timechoice = [2,3,4,5,6]
    tim = random.choice(timechoice)
    time.sleep(tim)
    t.mainloop()
if __name__ == "__main__":
    fly()
