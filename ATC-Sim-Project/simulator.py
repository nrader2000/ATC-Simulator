# simulator.py
# Nick Rader, Joe Davidson, Declan Worley, Sarah McLellan, Connor Willians, Cameron Meadows
# CSC-4710
# The product we were assigned with developing is an Air Traffic Control 
# Simulator, based on the atc-sim.com web app. This should be able to simulate 
# planes approaching and taking off from the STL (St. Louis Lambert) airport, 
# as well as planes passing through the area. The product should also give the 
# user the ability to act as an air traffic controller by giving the user the 
# necessary commands to be able to direct and control each of the simulated planes 
# around the airport. Just as any Air Traffic Controller would be able to do. 

# Imported Packages
from cProfile import run
import tkinter as tk
import random
from collections import namedtuple
import time

#GUI - Nick + Declan
# window creation
window = tk.Tk()
window.minsize(800,600)
#frame cration 
left_frame = tk.Frame()
right_frame = tk.Frame()

# textbox creation
textbox = tk.Text(master=left_frame)
textbox.pack()

# entrybox creation
entry = tk.Entry(master=left_frame)
entry.pack()

# heading list creation

# execution of window
left_frame.pack(side=tk.LEFT)
right_frame.pack(side=tk.RIGHT)

#Command to Run GUI - only uncomment for GUI testing and use
tk.mainloop()  

# Weather Function - Sarah
def weather():
    array = []
    x = random.randint(1,99)
    if x <= 16:
        dir = 315
    elif x <= 17 or x <= 32:
        dir = 0
    elif x <= 33 or x <= 48:
        dir = 180
    elif x <= 49 or x <= 64:
        dir = 135
    elif x <= 65 or x <= 80:
        dir = 45
    else:
        dir = 230
    array.append(dir)
    y = random.randint(0,100)
    if y < 80:
        speed = random.randint(5,15)
    elif y >= 80 or y < 90:
        speed = random.randint(0,5)
    else:
        speed = 40
    array.append(speed)
    return array

# Runway Function - ??
def runway(arrivalstatus,windDirection):
    runways = ["30R", "30L", "12R", "12L", "24", "29", "11", "6"]
    
    if(arrivalstatus == 1):
        print("Aircraft Arrival")
    else:
        if(windDirection == 315):
            runway = random.choice(runways)
            return runway
        elif(windDirection == 0):
            runway = random.choice(runways)
            return runway
        elif(windDirection == 180):
            runway = random.choice(runways)
            return runway
        elif(windDirection == 135):
            runway = random.choice(runways)
            return runway
        elif(windDirection == 45):
            runway = random.choice(runways)
            return runway
        elif(windDirection == 230):
            runway = random.choice(runways)
            return runway

# Arriving Aircraft Class - Nick
class Arriving_Aircraft:
    name = 0
    # list of the current aircrafts
    current_aircraft_list = []

    #the robinson44 is our helicopter
    aircraft_models = ["BA747", "Cessna172", "Robinson44", "CRJ900"]
    def __init__(self, name):
        self.name = name

    airline_names = ["SWA","DAL","ASQ","QXE"]
    
    def spawn_aircraft(self):
        flightid = random.choice(self.airline_names)+str(random.randint(100, 9999))
        heading = random.randint(1,365)
        model = random.choice(self.aircraft_models)
        altitude = random.randint(3000,42000)
        status = "Arrival"
        #arrivalstatus = 1
        new_aircraft = {
            "FlightID": flightid,
            "heading": heading,
            "altitude": altitude,
            "model": model,
            "status": status,
        }
        self.current_aircraft_list.append(new_aircraft)
        print(new_aircraft) #gui printout of aircraft

# Departing Aircraft Class -  Nick
class Departing_Aircraft:
    name = 0
    # list of the current aircrafts
    current_aircraft_list = []

    #the robinson44 is our helicopter
    aircraft_models = ["BA747", "Cessna172", "Robinson44", "CRJ900"]
    def __init__(self, name):
        self.name = name

    navaids = ["SCHMD", "CABIT", "KLAIR", "SAGME", "SAGZA", 
               "SAJOY", "WEDOG", "CHIKN", "MELVY", "DEECE", 
               "SAGZA", "SKYPE", "MYKEY", "TEWHY", "FRALE", 
               "MUZUL", "STAAN", "TWILA", "AUGST", "LEEAN", 
               "SNYDR", "PLESS"]

    airline_names = ["SWA","DAL","ASQ","QXE"]
    
    def spawn_aircraft(self):
        flightid = random.choice(self.airline_names)+str(random.randint(1000, 9999))
        nav = random.choice(self.navaids)
        weathervalues = weather()
        windDirection = weathervalues[0]
        depart_runway = runway(0,windDirection)
        model = random.choice(self.aircraft_models)
        altitude = 618 #altitude of STL field
        new_aircraft = {
            "FlightID": flightid,
            "Runway": depart_runway,
            "altitude": altitude,
            "model": model,
            "To": nav,
        }
        self.current_aircraft_list.append(new_aircraft)
        print(new_aircraft) #gui printout of aircraft

# Altitude Function - Joe

# Station Class - Cam

# Takeoff Function - Cam

# Landing Function - Cam

# Degree Function - ??

# Scale Function - Sarah

# Speed Function - Joe

# Abort Landing Function - Connor

# Abort Takeoff Function - Connor

# Simulator Class - Joe + Declan + Nick
class Simulator:
    running = 1
    while(running):
        aircraftchoice = random.randint(0,1)
        if(aircraftchoice == 0):
            newaircraft = Arriving_Aircraft('newaircraft')
            newaircraft.spawn_aircraft()
        else:
            newaircraft = Departing_Aircraft('newaircraft')
            newaircraft.spawn_aircraft()
        time.sleep(5)

# Run the Simulator
main = Simulator('main')