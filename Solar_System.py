## TO INSTALL VPYTHON IN YOUR JUPYTER NOTEBOOK WRITE %pip install vpython and run it 

from vpython import *
import numpy as np
scene = canvas() 


#define the value of G
G=6.673e-11
sun_mass = 2e30 #SUN'S MASS

#Defining acceleration of body a in respect of b.
def acc(a, b):
    rel_pos = b.pos - a.pos
    return (G*b.mass * norm(rel_pos)/rel_pos.mag2)

# Accelaration of a due to all the objects b intracting with it
def totalacc (a, objlist):
    sum_acc = vector (0,0,0)
    for b in objlist:
        if (a!=b):
            sum_acc = sum_acc + acc(a, b)
    return sum_acc
  
  
  #REQUIRED CONSTANTS AND INITIAL CONDITIONS
G=6.673e-11
myPi = np.pi
sun_mass = 2e30
mercury_mass=3.285e23

earth_mass = 6e24

venus_mass=0.815*earth_mass

mars_mass=0.107*earth_mass

saturn_mass=95.16*earth_mass

uranus_mass=14.54*earth_mass

neptune_mass=17*earth_mass



jupiter_mass=1.9e27

AU = 149.6e9       #mean earth sun orbital distance


earth_vel = 2* myPi * AU/(365.25 *24. *60.*60.) # average velocity = 2*Pi*R/T

jupiter_vel=2* myPi *AU*5.2/(11.86*365.25*24.*60.*60)

ml=1.59*earth_vel #MERCURY'S VELOCITY

vl=1.176*earth_vel #VENUS'S VELOCITY

mars_v=0.808*earth_vel #MARS'S VELOCITY

sl=0.325*earth_vel #SATURN'S VELOCITY

ul=0.228*earth_vel #URANUS'S VELOCITY

nl=0.182*earth_vel #NEPUTUNE'S VELOCITY

# plu_v=2* myPi *AU*39.5/(248*365.25*24.*60.*60) #PLUTO'S VELOCITY


#ANIMATION
scene.background = color.white
scene.autoscale = 0
scene.range = 10*AU



#CREATING OBJECTS
sun = sphere(pos= vector(0,0,0), velocity = vector(0,0,0),
             mass=sun_mass, radius = 0.1*AU, color =color.yellow)

earth = sphere(pos= vector(AU, 0, 0), velocity = vector(0,earth_vel,0),
               mass=earth_mass, radius=0.05*AU, color =color.cyan)

jupiter=sphere(pos=vector(5.2*AU,0,0),velocity=vector(0,jupiter_vel,0),
              mass=jupiter_mass, radius=0.15*AU, color=color.red)

mercury = sphere(pos= vector(0.387*AU,0,0), velocity = vector(0,ml,0),
             mass=mercury_mass, radius = 0.05*AU, color =color.orange)

venus = sphere(pos= vector(0.723*AU, 0, 0), velocity = vector(0,vl,0),
               mass=venus_mass, radius=0.08*AU, color =color.blue)

mars=sphere(pos=vector(1.524*AU,0,0),velocity=vector(0,mars_v,0),
             mass=mars_mass, radius=0.04*AU, color=color.red)

saturn = sphere(pos= vector(9.573*AU,0,0), velocity = vector(0,sl,0),
             mass=saturn_mass, radius = 0.1*AU, color =color.green)

uranus = sphere(pos= vector(19.1*AU, 0, 0), velocity = vector(0,ul,0),
               mass=uranus_mass, radius=0.1*AU, color =color.magenta)

neptune=sphere(pos=vector(30.1*AU,0,0),velocity=vector(0,nl,0),
             mass=neptune_mass, radius=0.1*AU, color=color.black)
# pluto=sphere(pos=vector(39.5*AU,0,0),velocity=vector(0,plu_v,0),
#              mass=plu_m, radius=0.05*AU, color=color.red)




bodies = [sun, earth, mercury, jupiter, neptune, uranus, mars, venus, saturn]

for b in bodies:
    b.acc = vector(0,0,0)
    b.track=curve (color = b.color)
    b.emissive=True
    
    
    # set total momentum of system to zero (centre of mass frame) 
sum=vector(0,0,0)
for b in bodies:
    if (b!=sun):
        sum=sum+b.mass*b.velocity

sun.velocity=-sum/sun.mass


# dt corresponds to 180000 SECONDS here
dt=30*60*100

#LEAP-FROG

for b in bodies:
    b.velocity = b.velocity + totalacc(b, bodies)*dt/2.0 #initalizing it at dt/2


while True:
    rate(50)  #not more than 100 time steps in a second
    for b in bodies:
        #update the positions
        b.pos = b.pos + b.velocity*dt
        b.track.append(pos=b.pos)

        #update the velocities
        b.velocity = b.velocity + totalacc(b, bodies)*dt

    scene.center = vector(0,0,0) #view centered on the origin of CM coord system

    
    
    



