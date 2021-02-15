def get(grp):
    inf=[]
    if(grp=='A+'):
        lines=open('apos.txt',encoding="utf8").readlines()
        for line in lines:
            info=line.split(',')
            inf.append([info])
    elif(grp=='B+'):
        lines=open('bpos.txt',encoding="utf8").readlines()
        for line in lines:
            info=line.split(',')
            inf.append([info])
    elif(grp=='O+'):
        lines=open('opos.txt',encoding="utf8").readlines()
        for line in lines:
            info=line.split(',')
            inf.append([info])
    elif(grp=='O-'):
        lines=open('oneg.txt',encoding="utf8").readlines()
        for line in lines:
            info=line.split(',')
            inf.append([info])
    elif(grp=='AB+'):
        lines=open('abpos.txt',encoding="utf8").readlines()
        for line in lines:
            info=line.split(',')
            inf.append([info])
    return (inf)