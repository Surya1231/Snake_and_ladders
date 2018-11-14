from graphics import *
from random import *
import time

d1,d2=1200,620
win2=GraphWin("Dimentions",250,250)
win2.setCoords(0,0,10,10)
r1=Rectangle(Point(0,10),Point(10,0))
r1.setFill('cyan')
r1.draw(win2)
m1=Text(Point(5,8),'Select Dimentions')
m1.setSize(20)
m1.draw(win2)
ee1=Entry(Point(3,6),6)
ee2=Entry(Point(6,6),6)
ee1.setText(1200)
ee2.setText(620)
ee1.draw(win2)
ee2.draw(win2)
m2=Text(Point(5,2),'Done')
m2.setSize(15)
m2.draw(win2)
r2=Rectangle(Point(3,3),Point(7,1))
r2.draw(win2)
while True:
    p=win2.getMouse()
    if 3<=p.getX()<=7 and 1<=p.getY()<=3:
        try:
            d1=int(ee1.getText())
            d2=int(ee2.getText())
            break
        except:
            break
win2.close()

x1,x2,y1,y2 = 0,24,0,32
win=GraphWin("Snake And Ladders",d1,d2)
win.setCoords(x1,y1,x2,y2)
mes1=Text(Point(22,30),'')
mes1.setStyle('bold')
mes1.setSize(18)
mes2=Text(Point(22,28),'')
mes2.setSize(15)
base=Rectangle(Point(x1,y2), Point(x2,y2-6))
base.setFill('cyan')
base.draw(win)
base1=Rectangle(Point(x1,y2), Point(4,26))
base1.setFill('white')
base1.draw(win)
base2=Rectangle(Point(20,y2), Point(24,26))
base2.setFill('white')
base2.draw(win)
mes1.draw(win)
mes2.draw(win)
s1=Text(Point(2,31),'Dice')
s1.setStyle('bold')
s1.setSize(18)
s1.draw(win)
s2=Text(Point(x2//2, y2-3),'Snakes And Ladders')
s2.setStyle('bold')
s2.setTextColor('red')
s2.setSize(32)
s2.draw(win)
ga,gb,dv=1,1,6
snakes={99:58,93:37,19:3,59:24,47:11,84:41,25:4,72:35,69:28}
ladder={7:36,83:97,12:70,40:63,50:95,45:77}

def developer():
    global snakes,ladder
    snakes,ladder={},{}
    box()
    mes1.setText("Done")
    t1=Text(Point(12,18),'Number of Snakes and Ladders')
    t1.setSize(20)
    t1.draw(win)
    e1=Entry(Point(9,15),3)
    e2=Entry(Point(15,15),3)
    e1.draw(win)
    e2.draw(win)
    while True:
        p=win.getMouse()
        if 20<=p.getX()<=24 and 26<=p.getY()<=32:
            try:
                s,l=int(e1.getText()),int(e2.getText())
                break
            except:
                pass
            
    for i in range(s):
        t1.setText('Enter snake  start and end '+str(i))
        while True:
            p=win.getMouse()
            if 0<=p.getX()<=4 and 26<=p.getY()<=32:
                st,ed=randint(1,100),randint(1,100)
                e1.setText(str(st))
                e2.setText(str(ed))
            if 20<=p.getX()<=24 and 26<=p.getY()<=32:
                try:
                    st,ed=int(e1.getText()),int(e2.getText())
                    snakes[max(st,ed)]=min(st,ed)
                    break
                except:
                    pass
                
    for i in range(l):
        t1.setText('Enter ladder  start and end '+str(i))
        while True:
            p=win.getMouse()
            if 0<=p.getX()<=4 and 26<=p.getY()<=32:
                st,ed=randint(1,100),randint(1,100)
                e1.setText(str(st))
                e2.setText(str(ed))
            if 20<=p.getX()<=24 and 26<=p.getY()<=32:
                try:
                    st,ed=int(e1.getText()),int(e2.getText())
                    ladder[min(st,ed)]=max(st,ed)
                    break
                except:
                    pass
    e1.undraw()
    e2.undraw()
        
def box():
    r=Rectangle(Point(0,26),Point(24,0))
    r.setFill('white')
    r.draw(win)

def mode():
    global snakes
    global ladder
    box()
    mes1.setText("Create Own ")
    mes2.setText("Mode")
    k=init1("Normal","Random Board","Only One(Random)")
    if k==3:
        temo=randint(0,1)
        if temo==0:
            snakes={99:58,93:37,19:3,59:24,47:11,84:41,25:4,72:35,69:28,15:4,67:23}
            ladder={}
        else:
            snakes={}
            ladder={7:36,83:97,12:70,40:63,50:95,45:77,58:99,37:93,3:19,24:59,11:47,41:84,4:25,35:72,28:69}
    elif k==1:
        snakes={99:58,93:37,19:3,59:24,47:11,84:41,25:4,72:35,69:28}
        ladder={7:36,83:97,12:70,40:63,50:95,45:77}
    elif k==2:
        snakes={}
        ladder={}
        for i in range(9):
            st,ed=randint(1,100),randint(1,100)
            st,ed=min(st,ed),max(st,ed)
            if st not in snakes and ed not in snakes:
                ladder[st]=ed
            st,ed=randint(1,100),randint(1,100)
            st,ed=min(st,ed),max(st,ed)
            if ed not in ladder and st not in ladder:
                snakes[ed]=st      
    else:
        developer()
    set1()

def init():   
    mes1.setText("Let's Start")
    mes2.setText("New Game")
     
def init1(s11,s22,s33):
    box()
    r1=Rectangle(Point(8,22),Point(16,19))
    r1.setFill('yellow')
    r1.setWidth(2)
    r1.draw(win)
    r2=r1.clone()
    r2.move(0,-6)
    r2.draw(win)
    r3=r1.clone()
    r3.move(0,-12)
    r3.draw(win) 
    s1=Text(Point(12,20),s11)
    s1.setTextColor('red')
    s1.setSize(20)
    s1.draw(win)
    s2=Text(Point(12,14),s22)
    s2.setTextColor('red')
    s2.setSize(20)
    s2.draw(win)
    s3=Text(Point(12,8),s33)
    s3.setTextColor('red')
    s3.setSize(20)
    s3.draw(win)
    e1=Entry(Point(23,23),3)
    e1.setFill('white')
    e1.setText(str(dv))
    if s11=='Normal':
        cust=Rectangle(Point(20,26), Point(24,20))
        cust.setFill('cyan')
        t1=Text(Point(22,25),'Boost Mode')
        t2=Text(Point(22,24),'Dice limit')
        t3=Text(Point(22,23,),'Limit =')
        l1=Line(Point(20,22),Point(24,22))
        t4=Text(Point(22,21),'Set')
        temp=1
        cust.draw(win)
        t1.draw(win)
    r=0
    while r==0:
        p=win.getMouse()
        if 8<=p.getX()<=16:
            if 19<=p.getY()<=22:
                r=1
            if 13<=p.getY()<=16:
                r=2
            if 7<=p.getY()<=10:
                r=3
        if s11=='Normal':
            if temp==1 and 20<p.getX()<24 and 21<=p.getY()<=26:
                t2.draw(win)
                t3.draw(win)
                l1.draw(win)
                t4.draw(win)
                e1.draw(win)
                temp=2
            elif 20<p.getX()<24 and 20<=p.getY()<=22:
                dicevalue(e1)
        if 20<=p.getX()<=24 and 27<=p.getY()<=32:
            r=4
    r1.undraw()
    r2.undraw()
    s1.undraw()
    s2.undraw()
    r3.undraw()
    s3.undraw()
    e1.undraw()
    return r

def dicevalue(e):
    global dv
    try:
        dv=int(e.getText())
        mes2.setText("Dice updated")
        time.sleep(1)
        mes2.setText("New game")
    except:
        pass
    
def dice():
    dicera=Rectangle(Point(1,30), Point(3,26))
    dicera.draw(win)
    dicera.setFill('pink')
    s1=Text(Point(2,28),'1')
    s1.setStyle('bold')
    s1.setSize(18)
    s1.draw(win)   
    temp=randint(20,30)
    for i in range(temp):
        k=randint(1,dv)
        s1.setText(str(k))
        time.sleep(0.08)
    mes2.setText("Click to run")
    win.getMouse()
    return k

def set2():
    mes1.setText('Click Anywhere')
    mes2.setText('to go back')
    c=Text(Point(12,20),'Suryaprakash Agarwal')
    c.setTextColor('blue')
    c.setSize(30)
    c.draw(win)
    win.getMouse()
    c.undraw()
    main()

def board():
    box()
    for i in range(2,24,2):
        h=Line(Point(i,3),Point(i,23))
        h.draw(win)
        v=Line(Point(2,i+1),Point(22,i+1))
        v.draw(win)

    for i ,j in snakes.items():
        p1=position(1,i)
        p2=position(1,j)
        su=Line(Point(p1[0]+3,p1[1]+4),Point(p2[0]+3,p2[1]+4))
        su.setOutline('red4')
        ru=Rectangle(Point(p1[0]+3-1,p1[1]+4+1),Point(p1[0]+3+1,p1[1]+4-1))
        ru.setFill('red1')
        ru.draw(win)
        su.setArrow('last')
        su.draw(win)
        su.setWidth(3)

    for i ,j in ladder.items():
        p1=position(1,i)
        p2=position(1,j)
        ru=Rectangle(Point(p1[0]+3-1,p1[1]+4+1),Point(p1[0]+3+1,p1[1]+4-1))
        ru.setFill('green1')
        ru.draw(win)
        su=Line(Point(p1[0]+3,p1[1]+4),Point(p2[0]+3,p2[1]+4))
        su.setOutline('green4')
        su.draw(win)
        su.setArrow('last')
        su.setWidth(3)
    numbers()

def numbers():
    i=1
    y=2
    while i<=100:
        t=0
        y+=2
        while t<10:
            te=Text(Point(3+2*t,y),i)
            te.draw(win)
            i+=1
            t+=1
        t=0
        y+=2
        while t<10:
            te=Text(Point(21-2*t,y),i)
            te.draw(win)
            i+=1
            t+=1

def getdice():
    global ga,gb
    cust=Rectangle(Point(20,26), Point(24,24))
    cust.setFill('yellow')
    qu=cust.clone()
    qu.move(-20,0)
    qu.draw(win)
    s2=Text(Point(22,25),'A=    B=           SET')
    s2.setStyle('bold')
    s2.setSize(15)
    q2=Text(Point(2,25),'Quit')
    q2.setSize(15)
    q2.draw(win)
    e1=Entry(Point(21,25),2)
    e1.setText(str(ga))
    e1.setFill('white')
    e2=Entry(Point(22,25),2)
    e2.setText(str(gb))
    e2.setFill('white')
    while True:
        p=win.getMouse()
        if 0<=p.getX()<=4 and 26<=p.getY()<=32:
            s2.undraw()
            cust.undraw()
            e1.undraw()
            e2.undraw()
            qu.undraw()
            q2.undraw()
            return dice()
        elif 20<=p.getX()<=24 and 29<=p.getY()<=32:
            try:
                cust.draw(win)
                e1.draw(win)
                e2.draw(win)
                s2.draw(win)
            except:
                pass
        elif 23<=p.getX()<=24 and 24<=p.getY()<=26:
            try:
                ga=int(e1.getText())
            except:
                pass
            try:
                gb=int(e2.getText())
            except:
                pass
            s2.undraw()
            cust.undraw()
            e1.undraw()
            e2.undraw()
            qu.undraw()
            q2.undraw()
            return 0
        elif 0<=p.getX()<=4 and  24<=p.getY()<=26:
            mes1.setText("Confrim Quit")
            mes2.setText("Click twice Quit")
            p=win.getMouse()
            if 0<=p.getX()<=4 and  24<=p.getY()<=26:
                e1.undraw()
                e2.undraw()
                return -1
            else:
                mes1.setText("Continue")
                mes2.setText("Click Dice")
            
def getx(p):
    if p%10==0:
        if p//10%2!=0:
            return 21
        else:
            return 3
    p1=p//10+1
    p2=p%10
    if p2==0:
        p2=10
    if p1%2!=0:
        return 1+2*p2
    else:
        return 23-2*p2

def position(p1,p2):
    if p1%10==0:
        y1=p1//10
    else:
        y1=p1//10+1
    if p2%10==0:
        y2=p2//10
    else:
        y2=p2//10+1
    y1=2*y1+1
    x1=getx(p1)
    y2=2*y2+1
    x2=getx(p2)
    return [x2-x1,y2-y1]

def check(n):
    if n in snakes:
        mes1.setTextColor("red")
        mes1.setText("Snake")
        mes2.setText("Click to Slide Down")
        return snakes[n]
    if n in ladder:
        mes1.setTextColor("white")
        mes1.setText("Ladder")
        mes2.setText("Click to Climb up")
        return ladder[n]
    return 0
        
def set1():
    global ga,gb
    board()
    pawn1=Text(Point(3,4),'A')
    pawn1.setStyle('bold')
    pawn1.setTextColor('purple')
    pawn1.setSize(22)
    pawn1.draw(win)
    pawn2=Text(Point(3,4),'B')
    pawn2.setStyle('bold')
    pawn2.setSize(22)
    pawn2.setTextColor('blue')
    pawn2.draw(win)
    a,b=1,1
    while True:
        base2.setFill("purple")
        mes1.setText("Player A")
        mes2.setText("Click Dice")
        mes1.setTextColor("yellow")
        mes2.setTextColor("yellow")
        k=getdice()
        if k==-1:
            break
        if k==0:
            k=ga-a
        if a+k<=100:
            pos=position(a,a+k)
            pawn1.move(pos[0],pos[1])
            a+=k
            k=check(a)
            if k!=0:
                win.getMouse()
                pos=position(a,k)
                pawn1.move(pos[0],pos[1])
                a=k
        if a==100:
            mes2.setText("Winner")
            break
        ga=a
                
        base2.setFill("blue")
        mes1.setText("Player B")
        mes2.setText("Click Dice")
        mes1.setTextColor("yellow")
        mes2.setTextColor("yellow")
        k=getdice()
        if k==-1:
            break
        if k==0:
            k=gb-b
        if b+k<=100:
            pos=position(b,b+k)
            pawn2.move(pos[0],pos[1])
            b+=k
            k=check(b)
            if k!=0:
                win.getMouse()
                pos=position(b,k)
                pawn2.move(pos[0],pos[1])
                b=k
        if b==100:
            mes2.setText("Winner")
            break
        gb=b
    win.getMouse()
    main()
       
def main():
    global ga,gb,dv
    ga,gb,dv=1,1,6
    base2.setFill('white')
    mes1.setTextColor('black')
    mes2.setTextColor('black')
    init()
    player1='player1'
    player2='player2'
    k=init1('START','CREDITS','EXIT')
    if k==1:
        mode()
    elif k==2:
        set2()
    else:
        win.close()

main()

