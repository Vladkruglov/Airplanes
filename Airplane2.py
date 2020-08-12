import random
from tkinter import *
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

    def polet():
        t = Tk()
        c = Canvas(t,height = 700,width = 700)
        c.pack()
        c.create_rectangle(0,0,700,700,fill = 'khaki2')
        yhy = [1,2,3,4,5]
        color = ['red', 'orange', 'green', 'olive', 'cyan', 'blue', 'pink', 'magenta', 'purple', 'brown', 'silver', 'black']
        companies = ["S7", "British Airlines", "Delta", "Уральские Авиалинии", "Emirates", "Air Berlin", "Turkish Airlines","Победа", "Nord Wind", "Аэрофлот"]
        t.title("Airplanes                                                                 0.4.0")  
        c.create_oval(200, 299, 143, 267, fill = 'khaki3', outline = 'khaki3')
        c.create_oval(600, 569, 843, 467, fill = 'khaki3', outline = 'khaki3')
        c.create_oval(100, 39, 125, 213, fill = 'khaki3', outline = 'khaki3')
        c.create_oval(567, 65, 653, 23, fill = 'khaki3', outline = 'khaki3')
        c.create_oval(300, 508, 400, 400, fill = 'khaki3', outline = 'khaki3')
        c.create_oval(100, 208, 500, 400, fill = 'khaki3', outline = 'khaki3')
        for i in range(0,10):
            random_y = random.randint(0,700)
            random_x = random.randint(0,700)
            rancolor = random.choice(color)
            ran_x = random.randint(0,700)
            ran_y = random.randint(0,700)
            c.create_line(random_x, random_y, ran_x, ran_y,  fill = rancolor, width=3, arrow=LAST, dash=(9,1), activefill=rancolor, arrowshape="9 18 9")


        
        
        t.mainloop()
if __name__ == "__main__":
    Fly.polet() 

