def add_nums():
    total, temp, b = 0,0,0
    f = open("input.txt", "r")
    for w in f:
        n = []
        for x,l in enumerate(w):
            if l.isnumeric():
                n.append(l)
            for i,j in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if w[x:].startswith(j):
                    n.append(i)
        total += int(f"{n[0]}{n[-1]}")
    return total
            
 
if __name__ == "__main__":
    print(add_nums())
 
 
 
 
