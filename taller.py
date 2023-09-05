#Moviento caballo
import random 
x=y=i=aleatorio=0
n=10
x=4
y=4
while(i<n):
    aleatorio=random.randrange(1,9)
    print(aleatorio)
    if(aleatorio==1):
        if(x+1<9 and y+2 <9):
            x=x+1
            y=y+2
            print("1..Posición del caballo: (",x,"",y,")")
    if(aleatorio==2):
        if(x+2<9 and y+1 <9):
            x=x+2
            y=y+1
            print("2..Posición del caballo: (",x,"",y,")")
    if(aleatorio==3):
        if(x+2<9 and y-1 >0):
            x=x+2
            y=y-1
            print("3..Posición del caballo: (",x,"",y,")")
    if(aleatorio==4):
        if(x+1<9 and y-2 >0):
            x=x+1
            y=y-2
            print("4..Posición del caballo: (",x,"",y,")")
    if(aleatorio==5):
        if(x-1<9 and y+2 >9):
            x=x-1
            y=y+2
            print("5..Posición del caballo: (",x,"",y,")")
    if(aleatorio==6):
        if(x-2<9 and y+1 >9):
            x=x-2
            y=y+1
            print("6..Posición del caballo: (",x,"",y,")")
    if(aleatorio==7):
        if(x-2<9 and y-1 >0):
            x=x-2
            y=y-1
            print("7..Posición del caballo: (",x,"",y,")")
    if(aleatorio==8):
        if(x-1<9 and y-2 >0):
            x=x-1
            y=y-2
            print("8..Posición del caballo: (",x,"",y,")")
    i+=1
