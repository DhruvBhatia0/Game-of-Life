import pdb

def submatrix(x,y):
    global l
    lx,ux=x-1,x+1
    ly,uy=y-1,y+1
    if lx==-1:
        lx=0
    if ux==N:
        ux=N-1
    if ly<0:
        ly=0
    if uy==N:
        uy=N-1
    nl=[]
    for i in range(ly,uy+1):
        t=l[i][lx:(ux+1)]
        nl.append(t)
        
    
    return nl
def dead(x,y):
    global l
    count=-1
    nl=submatrix(x,y)
    for i in nl:
        for j in i:
            if j=='#':
                count+=1
    if count>3:
        l[y][x]='.'
def dead2(x,y):
    global l
    count=-1
    nl=submatrix(x,y)
    for i in nl:
        for j in i:
            if j=='#':
                count+=1
    if count<2:
        l[y][x]='.'
def reprod(x,y):
    global l
    count=0
    nl=submatrix(x,y)
    for i in nl:
        for j in i:
            if j=='#':
                count+=1
    if count==3:
        l[y][x]='#'
    
    
    
    
    
m=int(input())
N=int(input())
l=[]

for i in range(N):
    l.append(input().split(' '))
pdb.set_trace()
for i in range(m+1):
    for j in range(N):
        for k in range(N):
            if l[j][k]=='.':
                reprod(k,j)
            else:
                dead(k,j)
                dead2(k,j)
for d in range(N):
        print(l[d])   

    

        


    
