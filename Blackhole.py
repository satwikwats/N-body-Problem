## TO INSTALL VPYTHON IN YOUR JUPYTER NOTEBOOK WRITE %pip install vpython and run it

from vpython import *
import numpy as np
scene = canvas() 


G=6.673e-11# value of universal gravitational constant

myPi = np.pi

cl=3e8 #speed of light

trap = 2e30 #mass of sun

A=4e6*trap #Sagittarius A*

l=5e12 #angular momentum ##GUESS

ct=(G*l**2*A)/cl**2 #G*M*l**2/c**2 #CORRECTION TERM FROM GENERAL RELATIVITY


#Defining acceleration of body a in respect of b.
def acc(a, b):
    rel_pos = b.pos - a.pos
    return (G*b.mass * norm(rel_pos)/rel_pos.mag**2)+ct*norm(rel_pos)/rel_pos.mag**3

# Accelaration of a due to all the objects b intracting with it
def totalacc (a, objlist):
    sum_acc = vector (0,0,0)
    for b in objlist:
        if (a!=b):
            sum_acc = sum_acc + acc(a, b)
    return sum_acc


 #Blackhole on a computer

earth_mass = 6e24 #in kg
S2=14*trap#mass of S2
S62=6.1*trap#mass of S62
S55=3*trap#mass of S55

#for initial conditions

AU = 146.9e9      #mean earth sun orbital distance
 #average velocity = 2*Pi*R/T

S2_v=(2.5*cl)/100 #2.5% speed of light #velocity of S2

S62_v= myPi *AU*970/(9.9*365.25*24.*60.*60) #velocity of S62

S55_v=myPi *AU*833/(12.98*365.25*24.*60.*60) #velocity of S55


# #scene.background = color.black
# scene.autoscale = 0
# #sphere(pos=vector(0,0,0),texture="C:\Users\Abc\Downloads\background.jpg")
# scene.range = 1000*AU
# scene = canvas()
scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=2500*AU,shininess=0)
scene.range = 1000*AU



#objects making up our black hole system
blackhole = sphere(pos= vector(0,0,0), velocity = vector(0,0,0),
             mass=A, radius = 20.5*AU,color=color.red)

S2 = sphere(pos= vector(118*AU,0,0), velocity = vector(0,S2_v,0),
            mass=S2, radius = 10.12*AU, color =color.cyan)
S62 = sphere(pos= vector(970*AU,0,0), velocity = vector(0,S62_v,0),
              mass=S62, radius=9*AU, color =color.white)
S55=sphere(pos=vector(833*AU,0,0),velocity=vector(0,S55_v,0),
             mass=S55, radius=9*AU, color=color.green)


bodies = [blackhole, S2, S62, S55]

for b in bodies:
    b.acc = vector(0,0,0)
    b.track=curve (color = b.color)
    #a=attach_light(b, offset=vec(0,0,0), color=color.black)
    b.emissive=True

# set total momentum of system to zero (centre of mass frame) 
sum=vector(0,0,0)
for b in bodies:
    if (b!=blackhole):
        sum=sum+b.mass*b.velocity

blackhole.velocity=-sum/blackhole.mass

# dt corresponds to 10000 seconds here
dt=100000

#Initialize leap-frog 

for b in bodies:
    b.velocity = b.velocity + totalacc(b, bodies)*dt/2.0 #finding velocity at dt/2


while True:
    rate(100)  #not more than 100 time steps in a second
    for b in bodies:
        #updating the positions
        b.pos = b.pos + b.velocity*dt
        b.track.append(pos=b.pos)

        #updating the velocities
        b.velocity = b.velocity + totalacc(b, bodies)*dt

    scene.center = vector(0.00251*AU,0,0) #view centered CM coordinate system



 
