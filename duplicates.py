def duplicates(lst):
    'prints the duplicates in a list by using a dict to keep count'
    dups = []
    d = {}
    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            if d[i] == 1:
                dups.append(i)
            d[i] +=1
    print(d)
