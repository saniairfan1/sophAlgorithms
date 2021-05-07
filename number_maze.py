def number_maze(L):
    'returns true or false if there is a path from the first elem in a graph to the last'
    bag = []
    first = (0,0)
    bag.append(first)
    visited=[]
    
    while len(bag) > 0:
        cell = bag.pop()
        if cell not in visited:
            x = cell[0]
            y = cell[1]
            n = L[x][y]
            if n == 0:
                return True
            visited.append(cell)
        
            if y + n < len(L[0]):
                bag.append((x,y+n))
            if y - n >= 0:
                bag.append((x,y-n))
            if x + n < len(L):
                bag.append((x+n,y))
            if x - n >= 0:
                bag.append((x-n,y))
    return False
