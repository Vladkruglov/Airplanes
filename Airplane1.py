""" Эта программа создаёт класс самолёта, кладёт самолёты в список, и потом по списку рисует полёт самолётов """
import random
from tkinter import *
import time 
import math

color = ['red', 'orange', 'green', 'olive', 'blue', 'pink', 'magenta', 'purple', 'brown', 'silver', 'black']
companies = ["S7", "British Airlines", "Delta", "Уральские Авиалинии", "Emirates", "Air Berlin", "Turkish Airlines", "Победа", "Nord Wind", "Аэрофлот"]

class Airplane(object):

    
    def __init__(self, x, y, company, speed, color, bearing, kmeters, x_fly, y_fly):
        # функция которая  имеет все переменные
        self.company = company
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.bearing = bearing
        self.x_fly = x_fly
        self.y_fly = y_fly

    def __init__(self, max_height = 700, max_width = 700, max_speed = 350, max_bearing = 360, max_kmeters = 400, min_kmeters = 50):
        # функция выдаёт значение переменных
        self.x = random.randint(0, max_height)
        self.y = random.randint(0, max_width)
        self.speed = random.randint(50, max_speed)
        self.color = random.choice(color)
        self.company = random.choice(companies)
        self.bearing = random.randint(0, max_bearing)
        self.x_fly = self.speed * math.cos(self.bearing) + self.x
        self.y_fly = self.speed * math.sin(self.bearing) + self.y

    def __str__(self):
        # берёт специальную строку
        return "Самолёт компании {}, в координатах {}, {}, летит в {}, {}, со скоростью {}, имеет цвет {}.".format(self.company, self.x, self.y, self.x_fly, self.y_fly, self.speed, self.color)

    def draw(self, c):
        c.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill = self.color) 
        c.create_line(self.x, self.y, self.x_fly, self.y_fly, fill = self.color, width=3, arrow=LAST, dash=(9,1),activefill=self.color, arrowshape="9 18 9")
        
    def change(self):
        """ Функция изменяет скорость и направление 
        Направление может иметь значение от 0 до 360
        Скорость может быть от 50 до 350"""
        self.bearing = random.randint(-15, 15) - 90
        self.speed = self.speed + random.randint(-40, 40) 
        if self.bearing > 360:
            self.bearing = self.bearing - 360 
        elif self.bearing < 0:
            self.bearing = self.bearing + 360
        if self.speed > 350:
            a = self.speed - 350
            self.speed = 350 - a
        elif self.speed < 50:
            a = 50 - self.speed 
            self.speed = self.speed + a

        print(self.bearing)
    
    def calc(self):
        self.x_fly = self.speed * math.cos(self.bearing) + self.x
        self.y_fly = self.speed * math.sin(self.bearing) + self.y

    def move(self):
        self.x = self.x_fly
        self.y = self.y_fly
        

if __name__ == "__main__":
    airplanes  = []

    t = Tk()
    t.title("Airplanes                                                                 0.10.5")  
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

    for i in range(0, 1):
        airplane = Airplane()
        airplanes.append(airplane)

    b = airplanes.index(airplane)


    while len(airplanes) > 0: 
        for airplane in airplanes:
            airplane.draw(canvas)
            airplane.move()
            airplane.calc()
            airplane.change()
            if airplane.x > 700 or airplane.x < 0 or airplane.y > 700 or airplane.y < 0:
                airplanes.remove(airplane)

    
    t.mainloop()



