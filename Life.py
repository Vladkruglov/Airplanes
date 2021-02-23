import time
import doctest

COORD_MAX = 1000000



initial = [(3,4), (3,3), (3,2)]

def is_alive(y, x, generation):
    
    try:
        more_than_max(y, x, generation)
        generation.index((y, x))
        return True
    except ValueError:
        return False
    return False

def calc_neighbours(y, x, generation):
    """
    >>> calc_neighbours(3, 3, [(3,4), (3,3), (3,2)])
    2
    """
    alive_neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i==0 and j==0:
                continue
            if is_alive(y+i, x+j, generation):     
                alive_neighbours +=1
    return alive_neighbours
        

def is_born(y, x, generation):
    
    neighbours = calc_neighbours(y, x, generation)
    if neighbours == 3:
        return True

def find_new_life(y,x, generation):
    """
    >>> find_new_life(3, 3, [(3,4), (3,3), (3,2)])
    [(2, 3), (4, 3)]
    """
    newborn_cells = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_born(y+i, x+j, generation):
                newborn_cells.append((y+i, x+j))
    
    return newborn_cells

def start(generation):
    calc_generation(generation)
    

def more_than_max(y, x, generation):
    """
    >>> more_than_max(-1, 1000001,[(3, 2), (3, 3), (3, 4)])
    (999999, 1)
    """
    
        
    if x < 0 or y < 0 or x > COORD_MAX or y > COORD_MAX:
        if x < 0:
            x = COORD_MAX + x 
        if y < 0:
            y = COORD_MAX + y 
        if x > COORD_MAX:
            x = x - COORD_MAX
        if y > COORD_MAX:
            y = y - COORD_MAX
    return y, x

def calc_generation(generation):
    """
    >>> calc_generation([(3, 2), (3, 3), (3, 4)])
    [(2, 3), (3, 3), (4, 3)]
    """
    new_generation = []
    for (y, x) in generation:
        non = calc_neighbours(y,x,generation)
        if non >= 2 and non <= 3:
            more_than_max(y, x, generation)
            new_generation.append((y,x))
            new_generation.append(find_new_life(y, x, generation))
        
    new_generation = check(new_generation)
    return new_generation

def check(spisok):
    """
    >>> check([(3, 2), (3, 2)])
    False
    >>> check([(3, 2), (3, 3)])
    [(3, 2), (3, 3)]
    """
    if  len(set(map(tuple, spisok))) != len(spisok):
        return False
    else:
        return spisok
    

def main():
    generatios = []
    state = initial
    generatios.append(tuple(state))
    while len(state) > 0 and state != calc_generation(state) and check(generatios) == generatios:
        state = calc_generation(state)
        time.sleep(0.5)
        print("Alive: {}".format(len(state)))
        print(state)
        generatios.append(tuple(state))
        

if __name__ == "__main__":
    doctest.testmod()
    main()