import random
import turtle
import time

class Airplane:

    
    def __init__(self, company_name, v, b):
        self.company_name = company_name
        self.v = v
        self.b = b

class Fly(Airplane):
    def __init__(self, company_name, v, b, rer):
        self.company_name = company_name
        self.v = v
        self.b = b
        self.rer = rer

    def vse_tri_poleta():
        random_y = random.randint(-250, 250)
        random_x = random.randint(-250, 250)
        color = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'pink', 'magenta', 'purple', 'brown', 'silver']
        rancolor = random.choice(color)
        indcolor = color.index(rancolor)
        color.pop(indcolor)
        a = turtle.Pen()
        b = turtle.Pen()
        c = turtle.Pen()
        d = turtle.Pen()
        e = turtle.Pen()
        f = turtle.Pen()
        g = turtle.Pen()
        h = turtle.Pen()
        i = turtle.Pen()
        j = turtle.Pen()
        companies = ["S7", "British Airlines", "Delta", "Уральские Авиалинии", "Emirates", "Air Berlin", "Turkish Airlines", "Победа", "Nord Wind", "Аэрофлот"] 
        fly = [a, b, c, d, e, f, g, h, i, j]
        rer = random.choice(fly)
        rer.color(rancolor)
        rer.speed(0)
        rer.up()
        rer.goto(random_x, random_y)
        rer.down()
        ie = [1, 2, 3, 4]
        spe = [1, 2, 3, 4]
        ransleep = random.choice(ie)
        ranspeed = random.choice(spe)
        polet_y = random.randint(-250, 250)
        polet_x = random.randint(-250, 250)
        rer.speed(ranspeed)
        rer.goto(polet_x, polet_y)
        time.sleep(ransleep)
        second_y = random.randint(-250, 250)
        second_x = random.randint(-250, 250)
        ransleep = random.choice(ie)
        ranspeed = random.choice(spe)
        rer.speed(ranspeed)
        rer.goto(second_x, second_y)
        time.sleep(ransleep)
        third_y = random.randint(-250, 250)
        third_x = random.randint(-250, 250)
        ransleep = random.choice(ie)
        ranspeed = random.choice(spe)
        rer.speed(ranspeed)
        rer.goto(third_x, third_y)
        time.sleep(ransleep)
        rer.goto(random_x, random_y)
        
for i in range(0,10):
    Fly.vse_tri_poleta() 

time.sleep(10)