from math import floor
from random import randrange

def find_max(lst):
    'finds the max in a lambda list using alg similar to binary search'
    # here i will call a function that does a search
    return max(lst,0,len(lst))


def max(lst,i, j):
    'searches for max ig'
    if i==j:
        return -1
    if i+1 == j:       #since that means theres only one element left to the right
        return lst[i]
    if j ==2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
        
    
    mid = (i+j)//2  #index of median

    if lst[mid]  > lst[mid-1] and lst[mid]> lst[mid+1]:
        return lst[mid]
    if lst[mid] > lst[mid+1]:
        #search left of middle
        return max(lst,i,mid)
    else:
        #search right of middle 
        return max(lst,mid+1,j)
    
def rnd_L(n):
    'create random Lambda list of n distinct elements'

    lst = [randrange(1,floor(n**1.5)) for _ in range (n+1)]
    max_ind = randrange(n+1)
    for i in range(max_ind):
        lst[i] += lst[i-1]
    for i in range(max_ind, n+1):
        lst[i] = lst[i-1] - lst[i]
    lst = [lst[i] + abs(lst[n]) for i in range(n)]
    return lst


def flip(lst):
    #calll another func
    print('')






def flip2(lst,n):
    if n == 0:                           #n is the len of the list
        return 

    currMax = max(lst,0,i)              #finds the max in the lst
    indMax = lst.index(currMax)         #finds the index of the maximum

    if indMax != n-1:                    # if the index of the max is not the same as the last elem, then well reverse
        lst = lst[n-1::-1]
        lst.append(currMax)

        
        
        
    
    
    
 
    
    



    
    


    
    
    
    
    
    
