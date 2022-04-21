## TO INSTALL VPYTHON IN YOUR JUPYTER NOTEBOOK WRITE %pip install vpython and run it

from vpython import *
import numpy as np
scene = canvas() 

#G value
G=6.673e-11
myPi = np.pi
trap = 1.77e29 # mass of trappist-1
sm=6963400 #Measurement for radius-1
rm=6371000 #Measurement for radius-2
earth_mass = 6e24 #mass of earth

bm=1.02*earth_mass #mass of planet b

cm=1.16*earth_mass #mass of planet c

dm=0.30*earth_mass #mass of planet d

em=0.77*earth_mass #mass of planet e

fm=0.93*earth_mass #mass of planet f

gm=1.15*earth_mass #mass of planet g

hm=0.33*earth_mass #mass of planet h

#Defining acceleration of body a in respect of b.al interaction
def acc(a, b):
    rel_pos = b.pos - a.pos
    return G*b.mass * norm(rel_pos)/rel_pos.mag2

# Accelaration of a due to all the objects b intracting with it
def totalacc (a, objlist):
    sum_acc = vector (0,0,0)
    for b in objlist:
        if (a!=b):
            sum_acc = sum_acc + acc(a, b)
    return sum_acc


#EXOPLANET on a computer



#for initial conditions

AU = 146.9e9      #mean earth sun orbital distance
 #average velocity = 2*Pi*R/T

earth_vel = 2* myPi * AU/(365.25 *24. *60.*60.) # average velocity = 2*Pi*R/T
jupiter_vel=2* myPi *AU*5.2/(11.86*365.25*24.*60.*60)

bv=2* myPi *AU*0.0115/(1.51*24.*60.*60) #VELOCITY of planet b

cv=2* myPi *AU*0.0158/(2.42*24.*60.*60) #VELOCITY of planet c

dv=2* myPi *AU*0.0223/(4.05*24.*60.*60) #VELOCITY of planet d

ev=2* myPi *AU*0.0293/(6.10*24.*60.*60) #VELOCITY of planet e

fv=2* myPi *AU*0.0385/(9.21*24.*60.*60) #VELOCITY of planet f

gv=2* myPi *AU*0.0469/(12.36*24.*60.*60) #VELOCITY of planet g

hv=2* myPi *AU*0.0619/(18.76*24.*60.*60) #VELOCITY of planet h



# #scene.background = color.black
# scene.autoscale = 0
# #sphere(pos=vector(0,0,0),texture="C:\Users\Abc\Downloads\background.jpg")
# scene.range = 1000*AU
# scene = canvas()
scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=2500*AU,shininess=0)
scene.range = 0.1*AU



trappist = sphere(pos= vector(0,0,0), velocity = vector(0,0,0),
             mass=trap, radius = 11.5*sm, color =color.yellow)
#earth = sphere(pos= vector(AU, 0, 0), velocity = vector(0,earth_vel,0),
 #              mass=earth_mass, radius=0.05*AU, color =color.cyan)
#jupiter=sphere(pos=vector(5.2*AU,0,0),velocity=vector(0,jupiter_vel,0),
             #mass=jupiter_mass, radius=0.15*AU, color=color.red)
b = sphere(pos= vector(0.0115*AU,0,0), velocity = vector(0,bv,0),
             mass=bm, radius = 1.12*rm, color =color.orange)

c = sphere(pos= vector(0.0158*AU, 0, 0), velocity = vector(0,cv,0),
               mass=cm, radius=1.10*rm, color =color.blue)

d=sphere(pos=vector(0.0223*AU,0,0),velocity=vector(0,dv,0),
             mass=dm, radius=0.78*rm, color=color.red)

e = sphere(pos= vector(0.0293*AU,0,0), velocity = vector(0,ev,0),
             mass=em, radius = 0.91*rm, color =color.green)

f = sphere(pos= vector(0.0385*AU, 0, 0), velocity = vector(0,fv,0),
               mass=fm, radius=1.05*rm, color =color.magenta)

g=sphere(pos=vector(0.0469*AU,0,0),velocity=vector(0,gv,0),
             mass=gm, radius=1.15*rm, color=color.white)

h=sphere(pos=vector(0.0619*AU,0,0),velocity=vector(0,hv,0),
             mass=hm, radius=0.77*rm, color=color.cyan)

bodies = [trappist, b, c, d, e, f, g, h]

for b in bodies:
    b.acc = vector(0,0,0)
    b.track=curve (color = b.color)
    b.emissive=True

# set total momentum of system to zero (centre of mass frame) 
sum=vector(0,0,0)
for b in bodies:
    if (b!=trappist):
        sum=sum+b.mass*b.velocity

trappist.velocity=-sum/trappist.mass

# dt corresponds to 360 seconds here
dt=360



#Initialize leap-frog for b in bodies:
for b in bodies:
    b.velocity = b.velocity + totalacc(b, bodies)*dt/2.0

#start leap-frog
while True:
    rate(50)  #not more than 100 time steps in a second
    for b in bodies:
        #updating the positions
        b.pos = b.pos + b.velocity*dt
        b.track.append(pos=b.pos)

        #updating theelocities
        b.velocity = b.velocity + totalacc(b, bodies)*dt

    scene.center = vector(0,0,0) #view centered on the origin of CM coord system
    
    
