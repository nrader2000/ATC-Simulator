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

# Imports
from tkinter import *
import random

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

# Runway Function - Nick
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

# Abort Landing Function - Connor
#function to abort landing, print msg, and cancel clearance
def abort_Landing(flightid):
    #print error message to GUI
    print("Error - Must Abort Landing.")
    
    #call cancel clearance with flightID 
    #UNKNOWN HOW TO DO RN
    #cancel_Clearance(flightid)

# Abort Takeoff Function - Connor
#function to abort takeoff, print msg, call runway, and cancel clearance
def abort_Takeoff(flightid):
    #print error message to GUI
    print("Error - Must Abort Takeoff.")
    
    #call cancel clearance with flightID 
    #UNKNOWN HOW TO DO RN
    #cancel_Clearance(flightid)
    
    #call runway class
    #NOT SURE WHY ATM, DONT THINK NEEDED
    runway(0,0)
    
    #remove progress strip
    #??? send something to GUI

# Arriving Aircrafts Class - Nick
class Arriving_Aircraft:

    # list of aircraft models (the robinson44 is our helicopter model)
    aircraft_models = ["BA747", "Cessna172", "Robinson44", "CRJ900"]

    # list of airline names to go into the flightID
    airline_names = ["SWA","DAL","ASQ","QXE"]
    
    # creates the aircraft data structure and returns it to simulator
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
        return new_aircraft

# Departing Aircrafts Class - Nick
class Departing_Aircraft:

    # list of aircraft models (the robinson44 is our helicopter model)
    aircraft_models = ["BA747", "Cessna172", "Robinson44", "CRJ900"]

    # list of navaids our departing aircrafts will head to
    navaids = ["SCHMD", "CABIT", "KLAIR", "SAGME", "SAGZA", 
               "SAJOY", "WEDOG", "CHIKN", "MELVY", "DEECE", 
               "SAGZA", "SKYPE", "MYKEY", "TEWHY", "FRALE", 
               "MUZUL", "STAAN", "TWILA", "AUGST", "LEEAN", 
               "SNYDR", "PLESS"]

    # list of airline names to go into the flightID
    airline_names = ["SWA","DAL","ASQ","QXE"]
    
    # creates the aircraft data structure and returns it to simulator
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
        return new_aircraft

# Aircraft Spawner Class - Nick
class Aircraft_Spawner:

    # list of our aircrafts being created by simulator
    aircraft_list = []

    # creates the listbox to display our list of aircrafts
    def __init__(self, tk):
        self.listbox = Listbox(tk,selectmode=SINGLE,bg='#0d212e',fg='#ffffff')
        self.listbox.configure(font=("Arial",14))
        self.listbox.place(relwidth=0.8,relheight=0.4,relx=0.1,rely=0.1)

    # appends the newly created aircraft to our list and then 
    # adds the list of aircrafts to the listbox element
    def addItem(self,ac):
        self.aircraft_list.append(ac)
        for x in self.aircraft_list:
            self.listbox.insert(END,x)

# Spawn Task - Nick
def spawn_task():

    # creates the listbox class on the UI
    ts = Aircraft_Spawner(tk)

    # randomizes if the aircraft is arriving or departing and then 
    # calls the spawn_aircraft() function to generate the data then
    # calls additem() fucntion from Aircraft_Spawner Class to make 
    # the addition to the UI
    aircraftchoice = random.randint(0,1)
    if(aircraftchoice == 0):
        newaircraft = Arriving_Aircraft()
        newaircraft = newaircraft.spawn_aircraft()
        ts.addItem(newaircraft)
    else:
        newaircraft = Departing_Aircraft()
        newaircraft = newaircraft.spawn_aircraft()
        ts.addItem(newaircraft)
    
    # wait every 10 seconds then run again
    tk.after(10000,spawn_task)

# GUI setup
tk = Tk()
tk.title("ATC-Simulator")
tk['background'] = '#183d54'
tk.geometry("1200x800")
tk.resizable(False,False)

# run spawning task concurrently with tk at startup
tk.after(0,spawn_task)

# console creation
console_printer = Listbox(tk,bg='#1d2329',fg='#ffffff')
editor = Entry(tk,bg='#1d2329',fg='#ffffff')
editor.configure(font=("Arial",16))
console_printer.configure(font=("Arial",14))
console_printer.place(relx=0.5,rely=0.7,relwidth=0.8,relheight=0.3,anchor=CENTER)
editor.place(relx=0.5,rely=0.85,relwidth=0.8,relheight=0.05,anchor=CENTER)

# mainloop
tk.mainloop()