mlist = list(1, 2, 3, 4)
for h in mlist:
    mlist[h]=mlist[h]*2
mlist = [1, 2, 3, 4]
mylist=[mlist[i]*2 for i in range(len(mlist))]    