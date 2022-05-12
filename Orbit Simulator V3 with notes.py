#--------------------------------Daniel-Baker------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math as m 
import time#Y'all know aht this is.
import matplotlib.pyplot as plt#2D mapping software
import matplotlib as mpl#2D mapping software under a different name
import tkinter#The GUI Daniel Used
from tkinter import mainloop#Buggy function I had to reimport
from mpl_toolkits.mplot3d import Axes3D#3D Mapping Software
import numpy as np#Maths program
from itertools import product, combinations#Another Maths Program
wait1=1
globalsign=2
dt=0#Difference in Time
tg=0#Time Step
xz=0#Xcoord
yz=0#Ycoord
zz=0#Zcoord
velzx=0#Xvelocity
velzy=0#Yvelocity
velzz=0#Zvelocity
           
        
def run():
    runwin = tkinter.Tk()#Creates a new GUI
    runwin.title("Orbit Sim")#Titles the GUI
    runwin.geometry("320x410")#Sizes the GUI
    runwin.configure(background="#000000")#Makes the GUI's background black
    lbl21 = tkinter.Label(runwin, text="How long to simulate for?", bg="#000000", fg="#ffffff").pack()#bf is the background colour in hexadecimal and the fg is the text colour
    lbl21 = tkinter.Label(runwin, text="Hint: 86400 works best", bg="#000000", fg="#ffffff").pack()#these are labels, just text
    ent21 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent21.pack()#Packs the Entry box(ent21) into the GUI (you must have this for all of the widgets in the GUI)
    lbl221 = tkinter.Label(runwin, text="How many seconds pass per check?", bg="#000000", fg="#ffffff").pack()#You can also put it after a line of code however then you cannot use any other widgets with it
    lbl222 = tkinter.Label(runwin, text="Hint: 10 works best", bg="#000000", fg="#ffffff").pack()
    ent22 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent22.pack()
    lbl23 = tkinter.Label(runwin, text="Starting Positon? Please state X then Y then Z.", bg="#000000", fg="#ffffff").pack()
    lbl222 = tkinter.Label(runwin, text="Hint: x=42240000, y=0, z=0 works best", bg="#000000", fg="#ffffff").pack()
    ent23 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent23.pack()
    ent24 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent24.pack()
    ent221 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent221.pack()
    lbl24 = tkinter.Label(runwin, text="Starting Velocity? Please state X then Y then Z.", bg="#000000", fg="#ffffff").pack()
    lbl24 = tkinter.Label(runwin, text="Hint: x=0, y=3071, z=0 works best", bg="#000000", fg="#ffffff").pack()
    ent25 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent26 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent27 = tkinter.Entry(runwin, bg="#000000", fg="#ffffff")
    ent25.pack()
    ent26.pack()
    ent27.pack()
    def run22():#The defs for the buttons these contain the commands that will play.
        global globalsign
        globalsign = 0
        runwin.quit()
        
    def run21():
        global globalsign
        globalsign = 1
        runwin.quit()
        
    def run23():
        runwin.quit()
            
    btn21 = tkinter.Button(runwin, text="Submit", command=run21, bg="#555555", fg="#ffffff")#These are buttons and can have a command assigned to them that will run when clicked
    btn21.pack()
        
    lbl24 = tkinter.Label(runwin, text="Automatically inputs best settings!", bg="#000000", fg="#ffffff").pack()
    btn22 = tkinter.Button(runwin, text="Auto-Fill", command=run22, bg="#555555", fg="#ffffff")#There can only be one command in the line of code, but using def you can create little scripts like run21(), run22() and run23()
    btn22.pack()
    btn23 = tkinter.Button(runwin, text="Exit", command=run23, bg="#555555", fg="#ffffff")
    btn23.pack()
    runwin.mainloop()
    if globalsign == 1:#This is where what ever you've entered into the boxes will get turned into a variable and then into numbers.(as they are originally strings)
        dt=int(ent21.get())#Globalsign is a variable that is changed based on which button you press.
        tg=int(ent22.get())
        xz=int(ent23.get())
        yz=int(ent24.get())
        zz=int(ent221.get())
        velzx=int(ent25.get())
        velzy=int(ent26.get())
        velzz=int(ent27.get())
        runwin.destroy()
    if globalsign == 0:#This is for the Auto-Fill button as these are the optimal values
        dt=86400
        tg=10
        xz=4.22e7
        yz=0
        zz=0
        velzx=0
        velzy=3071
        velzz=0
        runwin.destroy()

    t=0#Sets the time to zero
    plt.plot(0, 0, 'go')#Adds a point in the middle to the 2D graph, symbolising Earth.
    posx=[]#The X axis Array
    posy=[]#The Y axis Array
    posz=[]#The Z axis Array
    ceny=[0, 0]#The Y axis for the centre line Array
    cenz=[4.22e7, -4.22e7]#The Z axis for the centre line Array
    cenx=[0 ,0]#The X axis for the centre line Array
    posx.append(xz)#Adds original position to the X axis
    posy.append(yz)#Adds original position to the Y axis
    posz.append(zz)#Adds original position to the Z axis
    if globalsign < 2:
        while t < dt:#While the time is under the time allocated it will keep simulating
            r3, t =m.sqrt((xz*xz)+(yz*yz)+(zz*zz)), t+tg#Finding the radius to Earth
            f=(g3*m1*m2)/(r3*r3)#Finding Force.(N)
            a=-f/m2#Finding Acceleration.(M/S/S)
            ax=a*xz/r3#The X Acceleration
            ay=a*yz/r3#The Y Acceleration
            az=a*zz/r3#The Z Acceleration
            velox=velzx+ax*tg#Working out the new Xvelocity based on the old velocity and the (acceleration times the time step)
            veloy=velzy+ay*tg#Working out the new Yvelocity based on the old velocity and the (acceleration times the time step)
            veloz=velzz+az*tg#Working out the new Zvelocity based on the old velocity and the (acceleration times the time step)
            velzx=velox#Xvelocity
            velzy=veloy#Yvelocity
            velzz=veloz#Zvelocity
            xo, yo, zo = xz+(velox*(tg)), yz+(veloy*(tg)), zz+(veloz*(tg))#Working out the new X Y and Z Position based on the old position and the (new velocity times the time step)
            xz, yz, zz = xo, yo, zo#Updating
            posx.append(xo)#Adds the new x coord to the list
            posy.append(yo)#Adds the new x coord to the list
            posz.append(zo)#Adds the new x coord to the list
            #print(xo, yo, zo)
                
        plt.plot(posx, posy)#Plots the X and Y coords on a 2D Graph
        fig = plt.figure()#Puts in the requirements for a 3D Graph
        ax = fig.add_subplot(111, projection='3d')#Rights the axis for a 3D Graph
        ax.plot(cenx, ceny, cenz, 'g--')#Plots the centre point on the 3D Graph
        ax.plot(posx, posy, posz,)#Plots the X, Y and Z coords on a 3D Graph
        plt.show()#Shows both the 2D and 3D graph.
        



while wait1 == 1:
    globalsign=2
    g3=0.000000000066726#Gravitational constant
    m1=5.972e24#Mass of the Earth.(KG)                                    5.9721922e+24 kg
    m2=100#Mass of the object orbiting Earth.(KG)                         100 kg
    window = tkinter.Tk()#Creates a new GUI
    window.title("Orbit Sim")#Titles new GUI
    window.geometry("320x130")#Makes the new gui 320 by 130 pixels
    window.configure(background="#000000")#Turns the background black
    def runbtn():
        window.destroy()#Closes the GUI
        run()
    def exitbtn():
        window.destroy()#Closes the GUI
        global wait1#Ends the while loop
        wait1=wait1+1#Ends the while loop
        
    lbl1 = tkinter.Label(window, text="", bg="#000000", fg="#ffffff").pack()#Adds a blank label for spacing
    lbl16 = tkinter.Label(window, text="Simulate the entire thing! Shows up on a graph!", bg="#000000", fg="#ffffff").pack()#Adds a title
    btn15 = tkinter.Button(window, text="Final Simulation", command=runbtn, bg="#555555", fg="#ffffff").pack()#Jumps to the simulation
    lbl17 = tkinter.Label(window, text="Exit the program!", bg="#000000", fg="#ffffff").pack()#Adds a title
    btn16 = tkinter.Button(window, text="Exit", command=exitbtn, bg="#555555", fg="#ffffff").pack()#Exits the entire program
    lbl17 = tkinter.Label(window, text="All made by Daniel Baker!", bg="#000000", fg="#ffffff").pack()#Adds the creator's (thats DAN) name

    
    window.mainloop()#Finally opens the newly created GUI
