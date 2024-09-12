def linsearch(A,key):
    for i in range(0,len(A)):
        if A[i] == key:
            return i
    return None

if __name__ == "__main__":
    print(linsearch([3,6,1,-2,8], -2))