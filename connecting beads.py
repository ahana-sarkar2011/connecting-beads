import pgzrun
import random
from time import time

WIDTH = 700
HEIGHT = 500


beads=[]
lines=[]
next = 0
start = time()
gameover = False
win = False

rb = Actor("red_bead")
rb.x = random.randint(10,680)
rb.y = random.randint(10,480)
beads.append(rb)
ob = Actor("orange_bead")
ob.x = random.randint(10,680)
ob.y = random.randint(10,480)
beads.append(ob)
yb = Actor("yellow_bead")
yb.x = random.randint(10,680)
yb.y = random.randint(10,480)
beads.append(yb)
gb = Actor("green_bead")
gb.x = random.randint(10,680)
gb.y = random.randint(10,480)
beads.append(gb)
bb = Actor("blue_bead")
bb.x = random.randint(10,680)
bb.y = random.randint(10,480)
beads.append(bb)
pb = Actor("purple_bead")
pb.x = random.randint(10,680)
pb.y = random.randint(10,480)
beads.append(pb)
pib = Actor("pink_bead")
pib.x = random.randint(10,680)
pib.y = random.randint(10,480)
beads.append(pib)


def draw():
    global total
    global win
    screen.fill("black")
    number=1
    for i in beads:
        i.draw()
        number+=1
    for l in lines:
        screen.draw.line(l[0],l[1],"blue")
    if next < 10:
        total = time()-start
        total = round(total,1)
        screen.draw.text(str(total),(20,20))
    else:
        screen.draw.text(str(total),(20,20))
        if total<25:
            win = True
    if gameover == True:
        screen.fill("red")
        screen.draw.text("GAME OVER",(350,250),color="black", fontsize=70)
    if win == True:
        screen.fill("green")
        screen.draw.text("YOU WIN",(350,250),color="pink",fontsize=70)
        rbw.draw()

def update():
    pass

def on_mouse_down(pos):
    global next, lines
    if beads[next].collidepoint(pos):
        if next > 0:
            lines.append((beads[next-1].pos,beads[next].pos))
        next+=1
    else:
        lines=[]
        next=0

def timeup():
    global gameover
    gameover = True
clock.schedule(timeup,25)

pgzrun.go()