import pgzrun
import math
import random
WIDTH=800
HEIGHT=600
OUTSIDE=999

class Spclass(Actor):
	def __init__(self,x,y,angle,num):
		Actor.__init__(self.charas[num].imagename,(x,y))
		self.angle=angle
		self.hp=charas[num].hp
		self.num=num
class Explosion():
	def update(self):
		self.pos=spritemove(self.pos,self.angle,8)

		hitbox=Rect((self.x-15,self.y-15),(30,30))
		for sp in objects:
			if charas[sp.num].enemy==False or sp.hp==99:
				continue
			if sp.colliderect(hitbox):
				objects.append(Explosion(sp.x,sp.y,0,0))
				self.hp==-1
				break

class EnemyShot(Spclass):
		def update(self):
			self.pos=spritemove(self.pos,self.angel,4)

class Player(Spclass):
	def update(self):
		if keyboard.up	:self.y -=4
		if keyboard.down	:self.y +=4
		if keyboard.left	:self.x +=4
		if keyboard.right	:self.x +=4
		if self.x<35 :self.x =35
		if self.y<35 :self.y =35
		if self.x>(WIDTH-35) :self.x =WIDTH-35
		if self.y>(HEIGTH-35) :self.y =HEIGHT-35
		if keyboard.space!=0 and (self.count %16 )==0:
			objects.append(Shot(self.x,self.y,0,1))
			objects.append(Shot(self.x,self.y,30,1))
			objects.append(Shot(self.x,self.y,-30,1))
			hitbox =Rect((self.x-10,self.y-10),(20,20))	
			for sp in objects:
				if sp.colliderect(hitbox):
					self.hp -= 1
					sp.hp -=1
					break

class Enemy(Spclass):
	def update(self):
		self.x += int((self.count%200)/100)*2-1
		self.y += 2
		if random.randomrange(100)!=0: return
		px, py =player.pos
		newangle =-90 - math.degrees(math.atan2(py-self.y,px-self.x))
		newsp =EnemyShot(self.x,self.y, newangle,2)
		objects.append(newsp)

class Boss(Spclass):
	def update(self):
		if self.count<100: self.y += 1
		else:
			rad=math.radians(self.count -100)
			self.x=(WIDTH/2)+(math.sin(rad)*200)
		if self.count>150 and (self.count % 5)==0:
			newangle=(self.count*4)%360
			objects.append(EnemyShot(self.x,self.y,newangle, 2))

class Characlass:
	def __init__(self,filename, hp, enemy):
		self.imagename= filename
		self.hp= hp
		self.enemy= enemy
def sprite_move(pos, angle ,speed):
		x, y=pos
		rad =math.radians(-90-angle)
		x += (math.cos(rad))*speed
		y += (math.sin(rad))*speed
		return x,y

def init():
	global player, objects , bosstimer
	global titlemode, gameover, stars
	stars=[]
	for i in range(10):
		pos=(random.randrange(WIDTH),random.randrange(HEIGHT))
		stars.append(Rect(pos,(3,3)))
	objects= []
	player=Player(WIDTH/2, HEIGHT*3/4,0,3)
	objects.append(player)
	titlemode=True
	gameover=0
	
  

def draw():
	screen.clear()
	for rect in stars:
			screen.draw.rect(rect,"WHITE")

	if titlemode == True:
		screen.draw.text("S H O O T I N G  G A M E",left=150, top=240,fontsize=6,color="YELLOW")
	
pgzrun.go()
