
import random
from tkinter import *
import time

class Airplane:

    
    def __init__(self, company_name, v, b):
        self.company_name = company_name
        self.v = v
        self.b = b



def pervyy_polet():
    color = ['red', 'orange', 'green', 'olive', 'blue', 'pink', 'magenta', 'purple', 'brown', 'silver', 'black']
    companies = ["S7", "British Airlines", "Delta", "Уральские Авиалинии", "Emirates", "Air Berlin", "Turkish Airlines", "Победа", "Nord Wind", "Аэрофлот"] 
    a = Tk()
    a.title("Airplanes                                                                 0.6.4")  
    c = Canvas(a, height = 700, width = 700)
    c.pack()
    c.create_oval(-1000,-1000,1000,1000, fill = 'yellowgreen')
    c.create_oval(-1000,-1000,720,720, fill = 'gold', outline = 'yellow')
    c.create_oval(-1000,-1000,590,590,fill = 'cyan',outline = 'cyan')
    c.create_oval(-1000,-1000,450,450,fill = 'deepskyblue',outline = 'deepskyblue')
    c.create_oval(-1000,-1000,350,350,fill = 'royalblue',outline = 'royalblue')
    c.create_oval(-1000,-1000,250,250,fill = 'navy',outline = 'navy')
    airplanes = []

    for f in range(0,10):
        rancolor = random.choice(color)
        ran_x = random.randint(0,700)
        ran_y = random.randint(0,700)
        spe = [1, 2, 3, 4, 5, 6]
        ranspeed = random.choice(spe)
        ransec_x = random.randint(0,700)
        ransec_y = random.randint(0,700)
        plane = (random_x, random_y, rancolor, ranspeed, ran_x, ran_y)
        airplanes.append(plane)
        # c.create_line(ran_x, ran_y, ransec_x, ransec_y, fill = rancolor, width=3, arrow=LAST, dash=(9,1),activefill=rancolor, arrowshape="9 18 9")
        c.create_oval(random_x - 5, random_y - 5, random_x + 5, random_y + 5, fill = rancolor, outline = rancolor)
        spe = [1, 2, 3, 4, 5, 6]
        ranspeed = random.choice(spe)
    time.sleep(ransleep)
    a.mainloop()


if __name__ == "__main__":
    pervyy_polet()

