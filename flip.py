def flip(lst):
    'gives commands on how to sort a pancake stack'
    if decreasing(lst) == 0:
        print("flip top  " + str(len(lst)) + " pancakes")
    elif increasing(lst) == 0:
        print('')
    else:
        currBiggestPancake = findMax(lst) +1          #which pancake num is this
        print("flip top " + str(currBiggestPancake) + " pancakes")
        
        #now we need to reverse the list from 0 to including 4
        newLst = lst[currBiggestPancake-1::-1]
        remLst = lst[currBiggestPancake::]

        for i in range(len(newLst)):
            if i +1 == len(newLst):
                for j in remLst:
                    newLst.append(j)
        #return newLst  -------- this is the flipped list that we now need to reverse.

        # now we need to slice the largest num out of list
        newLst = newLst[len(remLst):]
        print("flip top " + str(currBiggestPancake+1) + " pancakes")
        newLst.reverse()
        flip(newLst)
      
def increasing(lst):
    'returns 0 if the list is increasing'
    count = 0
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            count += 0
        else:
            count+=1
    return count

def decreasing(lst):
    'returns 0 if the list is decreasing'
    count = 0
    for i in range(0,len(lst)-1):
        if lst[i+1] < lst[i]:
            count +=0
        else:
            count+=1
    return count

def findMax(lst):
    'returns the index of the max num in the lst'
    max = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return lst.index(max)
   
