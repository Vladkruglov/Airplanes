
import random
from tkinter import *
import time

color = ['red', 'orange', 'green', 'olive', 'blue', 'pink', 'magenta', 'purple', 'brown', 'silver', 'black']
companies = ["S7", "British Airlines", "Delta", "Уральские Авиалинии", "Emirates", "Air Berlin", "Turkish Airlines", "Победа", "Nord Wind", "Аэрофлот"]

class Airplane(object):

    
    def __init__(self, x, y, company, speed, color):
        self.company = company
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color

    def __init__(self, max_height = 700, max_width = 700, max_speed = 1000):
        self.x = random.randint(0, max_height)
        self.y = random.randint(0, max_width)
        self.speed = random.randint(0, max_speed)
        self.color = random.choice(color)
        self.company = random.choice(companies)

    def __str__(self):
        return "Самолёт компании {}, в координатах {}, {}, со скоростью {}, имеет цвет {}.".format(self.company, self.x, self.y, self.speed, self.color)
    
    def save():
        airplanes = []
        for t in range(0,20):
            airplanes.append(Airplane())

    def draw(a, c):
        a.title("Airplanes                                                                 0.6.4")  
        c.pack()
        c.create_oval(-1000,-1000,1000,1000, fill = 'yellowgreen')
        c.create_oval(-1000,-1000,720,720, fill = 'gold', outline = 'yellow')
        c.create_oval(-1000,-1000,590,590,fill = 'cyan',outline = 'cyan')
        c.create_oval(-1000,-1000,450,450,fill = 'deepskyblue',outline = 'deepskyblue')
        c.create_oval(-1000,-1000,350,350,fill = 'royalblue',outline = 'royalblue')
        c.create_oval(-1000,-1000,250,250,fill = 'navy',outline = 'navy')
        for i in range(0, 20):
            c.create_oval(x - 5, y - 5, x + 5, y + 5)   


def pervyy_polet():
    
    
    jokelist = []
    for f in range(0,20):
        
        ran_x = random.randint(0,700)
        ran_y = random.randint(0,700)
        spe = [1, 2, 3, 4, 5, 6]
        ranspeed = random.choice(spe)
        ransec_x = random.randint(0,700)
        ransec_y = random.randint(0,700)
        plane = (ran_x, ran_y, rancolor, ranspeed, ransec_x, ransec_y)
        
    for f in range(0,20):
        joke = (ran_x, ran_y)
        jokelist.append(joke)

    for f in range(0,20):
        wow = random.choice(jokelist)
        # c.create_line(ran_x, ran_y, ransec_x, ransec_y, fill = rancolor, width=3, arrow=LAST, dash=(9,1),activefill=rancolor, arrowshape="9 18 9")
        c.create_oval(wow - 5, wow + 5, fill = rancolor, outline = rancolor)
    a.mainloop()
if __name__ == "__main__":
    Airplane.draw(Tk(), Canvas(Tk(), height = 700, width = 700))


# i will do experiment...
