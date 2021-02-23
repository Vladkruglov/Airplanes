def find(a, b):
    for i in range(min(a,b), 0, -1):
        print("checked: {}".format(i))
        if a % i == 0 and b % i == 0:
            return i
            

    
    





if __name__ == "__main__":
    g = int(input())
    f = int(input())
    print(find(g, f))