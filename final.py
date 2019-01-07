
# starting file for the game 
#
# If you enjoy vPython, you might consider it as a final project...
#   docs: http://vpython.org/contents/docs/index.html
#   gallery of shapes: http://vpython.org/contents/docs/primitives.html
#
# Name: Tatiana Ermolaeva
#

from visual import *
import random
from math import*  

def make_walls():
    """ makes several walls and returns them in a list
        Docs here:  http://vpython.org/contents/docs/box.html
    """
    w0 = box(pos=(-30,0,0), axis=(0,0,1), 
             length=60, width=1, height = 0, color=color.white)
    w1 = box(pos=(0,0,-30), axis=(1,0,0), 
             length=60, width=1, height = 0, color=(255,255,255))
    w2 = box(pos=(30,10,0), axis=(0,0,1), 
             length=60, width=1, height = 20, color=(255,255,255))
    w3 = box(pos=(0,0,30), axis=(1,0,0), 
             length=60, width=1, height = 0, color=(255,255,255))
    list_of_walls = [ w0, w1, w2, w3 ]
    return list_of_walls


def make_alien():
    """ makes an alien! -- in the process, this shows how to
        group many objects into a single coordinate system ("frame")
        and treat that as a single object
        Docs here:  http://vpython.org/contents/docs/frame.html
    """
    alien = frame( pos=(-18,4,0) )  # makes a new "frame" == a container
    # with a local coordinate system that can have any number of parts...
    # here are the "parts":
    sphere( frame=alien, radius=1, color=color.green )
    sphere( frame=alien, radius=0.3, pos=(.7,.5,.2), color=color.white )
    sphere( frame=alien, radius=0.3, pos=(.2,.5,.7), color=color.white )
    sphere( frame=alien, radius=0.3, pos=(.2,.7,.5), color=color.white )
    cylinder( frame=alien, pos=(0,.9,-.2), axis=(.02,.2,-.02),  # the hat!
              radius=.7, color=color.magenta)
    return alien   # always use the _frame_, not any of its parts...

def make_iceberg():
    """makes iceberg for yeti"""
    iceberg = frame(pos=(-20, 0, 0))

    box(frame=iceberg, length=5, height=1, width=3, color=color.white )
    return iceberg 

def make_iceberg2():
    """makes iceberg for penguins"""
    iceberg2 = frame(pos=(0, 0, -20))

    box(frame=iceberg2, length=8, height=1, width=9, color=color.white )
    return iceberg2 

def pos_sb(x,y):
    """position of the snowball at the target"""
    xdef = abs(x-29)
    ydef = abs(y-10)
    cdef = sqrt(xdef**2 + ydef**2)
    if cdef < 1:
        return 10
    if cdef >= 1 and cdef < 3:
        return 5
    if cdef >= 3 and cdef < 5:
        return 2 
    else:
        return 0


def main():
    """ this is the main function, including
        all of the data objects and the "event loop"
        which is the while True: loop that will
        be the universe's "time stream" :-)
    """
    point = 0

    # create an object named floor of class (type) box:
    floor = box(pos=(0,-1,0), length=60, width=60, height = 0.5, color=color.blue)

    # this creates a list of walls 
    Walls = make_walls()
    w0, w1, w2, w3 = Walls   

    iceberg = make_iceberg()
    iceberg2 = make_iceberg2()

    #peng = ellipsoid
    peng = ellipsoid(pos=(-10,0,0), axis=vector(0,1,0),  
                    length=5, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng1 = ellipsoid(pos=(1,0,-19), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)
   
    peng2 = ellipsoid(pos=(2,0,-20), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng3 = ellipsoid(pos=(3,0,-19), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng4 = ellipsoid(pos=(0,0,-20), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)
    
    peng5 = ellipsoid(pos=(0,0,-21), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng6 = ellipsoid(pos=(1,0,-20), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng6 = ellipsoid(pos=(2,0,-21), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng7 = ellipsoid(pos=(3,0,-20), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng8 = ellipsoid(pos=(0,0,-22), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng9 = ellipsoid(pos=(1,0,-22), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)

    peng10 = ellipsoid(pos=(2,0,-22), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)
    
    peng11 = ellipsoid(pos=(3,0,-22), axis=vector(0,1,0),  
                    length=4, height=2, width=2,  color=(1,0,0) )
    peng.vel = vector(0,0,0)


    # this creates an alien!  (it's a vPython frame)
    alien = make_alien()
    alien.vel = vector(0,0,0)  # no velocity (yet!)
    sb = sphere( radius=1, pos=(0,-5,0), color=(1,1,1) )
    sb.vel = vector(0,0,0)
    sb.thrown = False

    # color names? they are black, blue, cyan, green, gray(v), 0.0<=v<=1.0
    #                       magenta, orange, red, white, yellow
    # or you can use rgb tuples (from 0.0 to 1.0, not 0 to 255), e.g.,
    snowman = sphere( radius=1, pos=(-20,2,0), color=(0,1,0) )
    snowman = sphere( radius=0.7, pos=(-20,3,0), color=(0,1,0) )
    snowman = sphere( radius=0.5, pos=(-20,4,0), color=(0,1,0) )
    snowman.vel = vector(0,0,0)   

    target = ring(pos=(29,10,0), axis=(1,0,0), radius=1, thickness=0.3, color=(1,0,0))
    target = ring(pos=(29,10,0), axis=(1,0,0), radius=3, thickness=0.3, color=(1,0.5,0))
    target = ring(pos=(29,10,0), axis=(1,0,0), radius=5, thickness=0.3, color=(1,0.5,0.5))

    SCORE = text(text='Your score is '+str(point), pos=(-35,30,-20), 
                    align='left', height=4, width=15, depth=-0.3, color=color.blue)
    grutor_mode = True 
    # We set some variables to control the display and the event loop
    gravity = 9.8
    RATE = 30             # number of loops per second to run, if possible!
    dt = 1.0/(1.0*RATE)   # the amount of time per loop (again, if possible)
    autocenter = True     # keeps the scene centered
    scene.forward = vector(0,-3,-2)
    scene.autoscale = False
    # this is the main loop of the program! it's "time" or the "event loop"
    while True:


        rate(RATE)     # run no faster than RATE loops/second

        # +++++ start of all position updates: once per loop +++++ 

        if sb.thrown == True:
            MAG = 50
            sb.vel = (peng.pos - sb.pos)*1.0
            if mag(sb.vel) < MAG:
                n = norm(sb.vel)
                sb.vel = n*MAG
    
        peng.pos = peng.pos + peng.vel*dt           # PHYSICS!
        sb.pos = sb.pos + sb.vel*dt

        if mag(peng.vel) > .001:
            peng.vel.y = peng.vel.y - gravity*dt
        if peng.pos.y < 0:
            peng.vel=vector(0,0,0)

        # +++++ end of all once-per-loop position updates +++++ 

        # collision check for the ball and penguin
        # vector docs:   http://vpython.org/contents/docs/vector.html
        vec_from_sb_to_peng = peng.pos - sb.pos
        if mag( vec_from_sb_to_peng ) < 1 and sb.thrown == True:
            y = sb.pos.y #random.uniform(8,18)
            z = sb.pos.z  #random.uniform(-5,5)
            goal = vector(30,y,z)
            peng.vel = goal - sb.pos
            sb.vel = peng.vel
            sb.thrown = False 

        
        # colliding with wall 2, w2:
        if peng.pos.x > w2.pos.x:  # should be a random position in the wall
            peng.pos.x = w2.pos.x # stay in bounds
            marker = sphere(pos=peng.pos)
            peng.pos = vector(-10,0,0)
            peng.vel = vector(0,0,0)  # penguin stays in the wall
            sb.vel = vector(0,0,0)
            sb.pos = vector(0,-5,0)
            
        
            point += pos_sb(marker.pos.x, marker.pos.y)
            SCORE.text = 'Your score is ' + str(point)
            print(point)

            if point >= 42:
                SCORE.text = 'You won!  Congratulations! '
                print('You won!  Congratulations!') 
                break 

            
        # here, we see if the user has pressed any keys
        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()
            print "You pressed the key", s  

            if s == 'G':  # launch the peng to fly up
                scene.background = (1,1,1)
                grutor_mode = False 
                point = 42
                print("You won!")


            if s == 'l':  # launch the peng to fly up
                zvel = random.uniform(-3,3) 
                xvel = random.uniform(5,15)
                yvel = random.uniform(10,20)
                peng.vel = vector(xvel, yvel, zvel)
                print(peng.pos)


            if s == 's': # throws the snowball
                sb.pos = vector( alien.pos.x,alien.pos.y, alien.pos.z) 
                sb.thrown = True
                #sb.vel = (peng.pos - sb.pos)*1.0
                #print(alien.pos) 


            # capital R to reset things
            if s == 'R':
                peng.vel = vector(0,0,0)
                peng.pos = vector(0,0,0)
                alien.vel = vector(0,0,0)
                alien.pos = vector(-20,4,0)

            if s == 'Q':  # Quit!
                print "Quitting..."
                break  # breaks out of the main loop


        # ===== end of handling user events: keypresses and mouse =====

    print "Done with the main loop. Ending this vPython session..."
    print "Close the vPython window to finish."
# this ends the main() function - it tends to get large!


# This should be the FINAL thing in the file...
if __name__ == "__main__":   # did we just RUN this file?
    main()                   # if so, we call main()