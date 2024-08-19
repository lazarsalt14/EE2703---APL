def list_rotate(l, N):
    acutal_rotate=N%len(l)
    temp=list(l)
    for i in range(len(l)):
        l[((i-acutal_rotate)%(len(l)))]=temp[i]
    return l        