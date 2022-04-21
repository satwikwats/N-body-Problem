# N-body-Problem
The N-body problem in physics involves predicting the orbits of celestial bodies in light of their gravitational interactions. 
The problem was first posed by Isaac Newton in 1687 in Principia Mathematica, and since then has gathered a lot of attention for its wide range of applications in space exploration. While there have been numerous methods provided for solving the n body problem computationally, I will highlight one of the most basic yet useful methods of solving this problem, the Leapfrog Method.

Leapfrog integration is a second order method. Here, instead of evaluating the value of velocity at time step ∆t, we evaluate v at ∆t
2 .

x1 = x0 + ∆tv1/2

Here, x1 represents distance, x0 is the initial distance and v1/2 is the initial velocity. Assuming we give initial values to x0 and v1/2 we can obtain a general formula for leapfrog method.

xn+1 = xn + ∆tvn(+1/2)

The leapfrog method has a greater accuracy than Euler Method 1, which is a first order method, but here Euler method will play a role to calculate the value of v1/2. 

This will not be a problem because it is being used just for a single step.
In general, Euler’s Method is not used to solve the n body problem because the 3 body system is already chaotic, and applying forward integration (Euler method) would increase the error rate at every time step.


##Providing Initial Conditions
To simulate the orbits of eight planets and the Sun, Trappist_1 the exoplanet system, and Blackhole and its Star it is important to gather information regarding
their initial conditions. Considering variables required to solve Newtonian
gravitational mechanics;
Fij = Gmimj ||xi − xj ||2 · (xj − xi) ||xi − xj || 

Here, xi is the position vector for the ith body, G is the gravitational constant and mi is the mass
of the body.



