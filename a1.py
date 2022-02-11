def jumperasman(n):
    ind=0
    mxjump=0
    for i in range(len(n)):
        if i> mxjump:
            break
        mxjump=max(int(n[i])+i,mxjump)
    if mxjump>=len(n)-1:
        return 1
    return 0
print(jumperasman(str(input()).split()))