
import random
from tkinter import *
import time

color = ['red', 'orange', 'green', 'olive', 'blue', 'pink', 'magenta', 'purple', 'brown', 'silver', 'black']
companies = ["S7", "British Airlines", "Delta", "Уральские Авиалинии", "Emirates", "Air Berlin", "Turkish Airlines", "Победа", "Nord Wind", "Аэрофлот"]

class Airplane(object):

    
    def __init__(self, x, y, company, speed, color, bearing):
        self.company = company
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.bearing = bearing

    def __init__(self, max_height = 700, max_width = 700, max_speed = 1000, max_bearing = 360):
        self.x = random.randint(0, max_height)
        self.y = random.randint(0, max_width)
        self.speed = random.randint(0, max_speed)
        self.color = random.choice(color)
        self.company = random.choice(companies)
        self.bearing = random.randint(0, max_bearing)

    def __str__(self):
        return "Самолёт компании {}, в координатах {}, {}, со скоростью {}, имеет цвет {}.".format(self.company, self.x, self.y, self.speed, self.color)

    def draw(self, c):
        c.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill = self.color) 




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
    airplanes  = []

    t = Tk()
    t.title("Airplanes                                                                 0.6.4")  
    canvas = Canvas(t,height = 700,width = 700)
    canvas.pack()
    canvas.create_oval(-1000,-1000,1000,1000, fill = 'yellowgreen')
    r = 0
    z = 70
    while r < 10:
        r = r + 1
        canvas.create_line(z, 0, z, 700)
        z = z + 70
    r = 0
    z = 70
    while r < 10:
        r = r + 1
        canvas.create_line(0, z, 700, z)
        z = z + 70
    canvas.create_line(0, 70, 700, 70)
    canvas.create_line(0, 140, 700, 140)
    canvas.create_line(0, 210, 700, 210)
    canvas.create_line(0, 280, 700, 280)
    canvas.create_line(0, 350, 700, 350)
    canvas.create_line(0, 420, 700, 420)
    canvas.create_line(0, 490, 700, 490)
    canvas.create_line(0, 560, 700, 560)
    canvas.create_line(0, 630, 700, 630)

    for i in range(0, 20):
        airplane = Airplane()
        airplanes.append(airplane)
    
    for airplane in airplanes:
        airplane.draw(canvas)
    t.mainloop()


# i will do experiment!!!
