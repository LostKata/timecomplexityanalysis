def binsearch(A,key):
    m = len(A)-1 ; i = 0 ; j = m
    while True:
        m = (j-i)//2+i # returns integer
        if A[m] == key:
            return m
        if i == j-1:
            if A[j] == key:
                return j
            else:
                break
        elif A[m] < key: # Search upper half
            i = m
            j = j
        elif A[m] > key: # Search lower half
            i = 0
            j = m
if __name__ == "__main__":
    i = binsearch([-2,2,3,5,7,8,9], 8);print(i)
    i = binsearch([-2,2,3,5,7,8,9], 1);print(i)
    i = binsearch([-2,2,3,5,7,8,9], 9);print(i)