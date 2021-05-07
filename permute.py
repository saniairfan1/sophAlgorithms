
def permute(lst):
    'finds all the permuations of a list lst'
    if len(lst)==0 or len(lst)==1:
        return [lst]
    elif len(lst)==2:
        f = lst[0]
        s = lst[1]
        return [[f,s],[s,f]]
    else:
        newLst = []
        for i in range(len(lst)):
            currElem = lst[i]
            rest = lst[:i] + lst[i+1:]                     # this basically gets the rest of the elem in the lst apart from curr
           
            
            lst2 = permute(rest)
            for j in lst2:
                newLst.append([currElem] + j)
        return newLst

def max_perm(n):
    'returns the max sum of differences in a permuted list 1-n'
    max = 0
    lst = []
    for i in range(1,n+1):
        lst.append(i)

    permutedList = permute(lst)
    for i in permutedList:
        if sum_diff(i)>max:
            max  = sum_diff(i)
    return max
 

def sum_diff(lst):
    'finds the sum of the abs value differences in a list'
    sum =0
    for i in range(len(lst)-1):
        sum += abs(lst[i]-lst[i+1])
    return sum

            

        
            
            
        
        
           
            
            


        
      
