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
#from operator import ne
from tkinter import *
from tkinter.messagebox import askyesno
import random
import math
from threading import Timer
#import time

# RepeatTimer Class - Joe
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

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

# Aircraft_Spawner Class - Nick
class Aircraft_Spawner:
    
    # list of our aircrafts being created by simulator
    aircraft_list = []

    def __init__(self,tk):
        # list box taking input of spawning planes and displaying that info
        self.listbox = Listbox(tk,selectmode=SINGLE,bg='#0d212e',fg='#ffffff')
        self.listbox.configure(font=("Arial",14))
        self.listbox.bind('<Double-1>',self.click_progress_strip)
        self.listbox.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.3)

    # addItem Function - Nick
    # appends the newly created aircraft to our list and then 
    # adds the list of aircrafts to the listbox element
    def addItem(self,ac):
        ac = list(ac.values())[0],list(ac.values())[1],list(ac.values())[2],list(ac.values())[3],list(ac.values())[4],list(ac.values())[5]
        self.aircraft_list.append(ac)
        for x in self.aircraft_list:
            self.listbox.insert(END,x)

    # click_progress_strip Function - Nick
    def click_progress_strip(self,event):
        index = self.listbox.curselection()[0]
        current_aircraft = self.aircraft_list[index]
        flightID = current_aircraft[0]
        editor.delete(0,'end')
        editor.insert(0,flightID)

# Input_Grab Class - Nick
class Input_Grab:

    command = ''
    # getinput Function - Nick
    # function will assign whatever comes from the entry bar 
    # to command and then makes front end changes and then sends 
    # command to be parsed by simulator
    def getinput(self,event):
        self.command = editor.get()
        if self.command:
            editor.delete(0,'end')
            console_printer.insert(END,"==========================================================")
            console_printer.insert(END,self.command)
            simulator(self.command)
        else:
            pass

    def repeatinput(self,event):
        if self.command:
            editor.delete(0,'end')
            editor.insert(0,self.command)
        else:
            pass

    def deleteinput(self,event):
        editor.delete(0,'end')

#v Backend Code Starts Here v#
#################################################################################################################
# Backend_Simulator Class - Joe + Nick
class Backend_Simulator:
    
    name = 0
    timer = 0
    coordinate_timer = 0
    departure_timer = 0
    buffer = ''
    #it says in the name
    current_aircraft_list = []
    # list of aircraft models (the robinson44 is our helicopter model)
    aircraft_models = ["BA747", "Cessna172", "Robinson44", "CRJ900"]
    # list of airline names to go into the flightID
    airline_names = ["SWA","DAL","ASQ","QXE"]
    # list of navaids our departing aircrafts will head to
    destinations = [
    {"name": "SCHMD", "x_cord": -99, "y_cord": 99},
    {"name": "CABIT", "x_cord": -99, "y_cord": 85},
    {"name": "KLAIR", "x_cord": -98, "y_cord": -97},
    {"name": "SAGME", "x_cord": -45, "y_cord": -97},
    {"name": "SAGZA", "x_cord": -25, "y_cord": -97},
    {"name": "SAJOY", "x_cord": -10, "y_cord": -97},
    {"name": "WEDOG", "x_cord": 5, "y_cord": -97},
    {"name": "CHIKN", "x_cord": 0, "y_cord": -30},
    {"name": "MELVY", "x_cord": -15, "y_cord": 50},
    {"name": "DEECE", "x_cord": -10, "y_cord": 99},
    {"name": "SKYPE", "x_cord": 5, "y_cord": 99 },
    {"name": "MYKEY", "x_cord": 0, "y_cord": 99},
    {"name": "TEWHY", "x_cord": 20, "y_cord": 99},
    {"name": "FRALE", "x_cord": 40, "y_cord": 99},
    {"name": "MUZUL", "x_cord": 65, "y_cord": 50},
    {"name": "STAAN", "x_cord": 20, "y_cord": 20},
    {"name": "TWILA", "x_cord": 90, "y_cord": 5},
    {"name": "AUGST", "x_cord": -50, "y_cord": -10},
    {"name": "LEEAN", "x_cord": 35, "y_cord": -97},
    {"name": "SNYDR", "x_cord": -15, "y_cord": -5},
    {"name": "PLESS", "x_cord": -95, "y_cord": -99}
    ]
    
    def __init__(self, name):
        self.name = name
        #self.timer = RepeatTimer(3, self.check_spatials, args=())
        self.coordinate_timer = RepeatTimer(3, self.update_positions, args=())
        self.departure_timer = RepeatTimer(1, self.departure_cleared, args=())
        #self.timer.start()
        self.coordinate_timer.start()

    # spawns an aircraft to the map
    def spawn_aircraft(self):
        flightid = random.choice(self.airline_names)+str(random.randint(100, 9999))
        x_val = random.randint(-100,100)
        y_val = random.randint(-100,100)
        altitude = random.randint(3,30)
        speed_value = random.randint(100,1000)
        heading = random.randint(0,360)
        model = random.choice(self.aircraft_models)
        departing = random.randint(0,1)
        if departing:
            destination = random.choice(self.destinations)
        else:
            destination = {"name": "Arrival","x_cord": 0,"y_cord": 0}
        new_aircraft = {
            "FlightID": flightid,
            "heading": heading,
            "altitude": altitude*1000,
            "speed": speed_value,
            "model": model,
            "destination": destination["name"],
            "x_val": x_val,
            "y_val": y_val,
        }
        self.current_aircraft_list.append(new_aircraft)
        return new_aircraft

    # prints list of cirrent aircrafts
    def print_aircraft(self, flightID):
        if flightID != 0:
            for i in self.current_aircraft_list:
                if i["FlightID"] == flightID:
                    console_printer.insert(END,i)
        else:
            for i in self.current_aircraft_list:
                console_printer.insert(END,i)

    # returns all of the current flight id's
    def get_flight_ids(self):
        flight_list = []
        for i in self.current_aircraft_list:
            x = i.get("FlightID")
            flight_list.append(x)
        return flight_list

    # returns a list of the destinations
    def ret_destinations(self):
        return self.destinations

    # returns the list of current aircrafs
    def current_aircrafts(self):
        return self.current_aircraft_list

    # closes the executable program
    def close_program(self):
        answer = askyesno(title='Quit?',message='Are you sure you want to quit?')
        if answer:
            tk.destroy()
            main.kill()
        else:
            pass

    # creates a popup window with all the helpful 
    # information you would need to operate the software
    def help_window(event):
        # popup setup
        helpwindow = Toplevel(tk,bg='#183d54')
        helpwindow.title("Help")
        helpwindow.state('zoomed')
        helpwindow.resizable(False,False)
        # scrollbar setup
        scrollbar = Scrollbar(helpwindow)
        scrollbar.pack(side = RIGHT, fill = Y)
        # title label setup
        hwtitle = Label(helpwindow,text="Help")
        hwtitle.configure(bg='#183d54',fg='#ffffff',font=("Arial 32"))
        hwtitle.pack()
        # textbox setup
        hwtext = Text(helpwindow,yscrollcommand = scrollbar.set)
        hwtext.insert(INSERT,"Basic Info:\n")
        hwtext.insert(INSERT,"\nAircrafts will spawn every 15-30 seconds. You will see all the important air traffic info displayed in the top box. The bottom box will contain a console for the user to type in commands (see more info on commands down below). The box will also contain all history of the inputs the user has made into the console (valid and invalid alike) as well as the resulting output. \n")
        hwtext.insert(INSERT,"\nList of Navaids:\n")
        hwtext.insert(INSERT,"\nSCHMD{-99,99}, CABIT{-99,85}, KLAIR{-98,-97}\nSAGME{-45,-97}, SAGZA{-25,-97}, SAJOY{-10,-97}\nWEDOG{5,-97}, CHIKN{0,-30}, MELVY{-15,50}\nDEECE{-10,99}, SKYPE{5,99}, MYKEY{0,99}\nTEWHY{20,99}, FRALE{40,99}, MUZUL{65,50}\nSTAAN{20,20}, TWILA{90,5}, AUGST{50,-10}\nLEEAN{35,-97}, SNYDR{-15,-5}, PLESS{-95,-99}\n")
        hwtext.insert(INSERT,"\nHow to Use (UI):\n")
        hwtext.insert(INSERT,"\nAs an Air Traffic Controller, your job is to control the traffic of each aircraft in the airspace following safe seperation standards as well as ensuring each aircraft gets to their indicated destination.\n") 
        hwtext.insert(INSERT,"\nClick on the rows in the top box to grab the FlightID from that row's aircraft easily and then enter a command in the entrybox below the bottom box (see more info on commands below) to direct that aircraft's new movement.\n")
        hwtext.insert(INSERT,"\nHow to Use (Console Entry Bar):\n")
        hwtext.insert(INSERT,"\nTo send commands to be processed, hit the enter/return key once you have a command in the entry. Hit the up key to bring back the previous command and hit the down key to clear the entry box.\n")
        hwtext.insert(INSERT,"\n1. Understanding the Air Traffic:\n")
        hwtext.insert(INSERT,"\nFirst Item: FlightID = main value being the distinction between each aircraft. \n")
        hwtext.insert(INSERT,"Second Item: Heading(in deg) = the direction of the aircraft in degrees. \n")
        hwtext.insert(INSERT,"Third Item: Altitude(in ft) = the number of ft an aircraft is in the air. \n")
        hwtext.insert(INSERT,"Fourth Item: Aircraft Speed(in mph) = the indicated speed of the aircraft. \n")
        hwtext.insert(INSERT,"Fifth Item: Model of Aircraft = the type of aircraft. \n")
        hwtext.insert(INSERT,"Sixth Item: Destination Info = the indicated direction of the aircraft, if the aircraft is arriving to the airport the destination will be 'Arrival'. \n")
        hwtext.insert(INSERT,"\n2. Understanding the Controls/Commands:\n")
        hwtext.insert(INSERT,"\n'help' = it's how you opened this help window! \n")
        hwtext.insert(INSERT,"'about' = opens the about window. \n")
        hwtext.insert(INSERT,"'q' = quits the program. \n")
        hwtext.insert(INSERT,"'showac' = shows the current aircrafts in the airspace and their values. \n")
        hwtext.insert(INSERT,"'s' = changes the speed for an indicated aircraft(using FlightID). Must follow up the command with a valid number. Ex: <FlightID> s 500 \n")
        hwtext.insert(INSERT,"'h' = holds an indicated aircraft(using FlightID). Ex: <FlightID> h \n")
        hwtext.insert(INSERT,"'t' = clears an indicated aircraft for takeoff(using FlightID), as long as it's indicated destination is a navaid and not STL(Arrival). Ex: <FlightID> t \n")
        hwtext.insert(INSERT,"'l' = clears an indicated aircraft for landing(using FlightID), as long as it's indicated destination is STL(Arrival) and not a navaid. Ex: <FlightID> l \n")
        hwtext.insert(INSERT,"'c(l,r,navaid,#)' = changes the heading an indicated aircraft(using FlightID). Must follow up the command with either an 'l', 'r', navaid name, or valid heading number to represent the heading in degress.\nEx: <FlightID> c l, <FlightID> c r, <FlightID> c SKYPE, <FlightID> c 180 \n")
        hwtext.insert(INSERT,"'c(a)' = changes the altitude an indicated aircraft(using FlightID). Must be followed up with a value between 3 and 36(the value gets multiplied by 1000 to depict legitimate altitude). Ex: <FlightID> c a 4 \n")
        hwtext.configure(bg='#183d54',fg='#ffffff',font=("Arial 16"),bd=0,state='disabled',padx=10,pady=10,wrap=WORD)
        hwtext.pack()
    
    # creates a popup window with all the
    # information you would need to about the software
    def about_window(event):
        # popup setup
        aboutwindow = Toplevel(tk,bg='#183d54')
        aboutwindow.title("About")
        aboutwindow.state('zoomed')
        aboutwindow.resizable(False,False)
        # title label setup
        awtitle = Label(aboutwindow,text="About")
        awtitle.configure(bg='#183d54',fg='#ffffff',font=("Arial 32"))
        awtitle.pack()
        # textbox setup
        awtext = Text(aboutwindow)
        awtext.insert(INSERT,"About the Software:\n")
        awtext.insert(INSERT,"\nThe product we were assigned with developing is an Air Traffic Control Simulator, based on the atc-sim.com web app. This should be able to simulate planes approaching and taking off from the STL (St. Louis Lambert) airport, as well as planes passing through the area. The product should also give the user the ability to act as an air traffic controller by giving the user the necessary commands to be able to direct and control each of the simulated planes around the airport. Just as any Air Traffic Controller would be able to do. \n")
        awtext.insert(INSERT,"\nThe Arch Development Team:\n")
        awtext.insert(INSERT,"\n+ Sarah McLellan \n")
        awtext.insert(INSERT,"+ Joe Davidson \n")
        awtext.insert(INSERT,"+ Nick Rader \n")
        awtext.insert(INSERT,"+ Cameron Meadows \n")
        awtext.insert(INSERT,"+ Declan Worely \n")
        awtext.insert(INSERT,"+ Connor Willans \n")
        awtext.configure(bg='#183d54',fg='#ffffff',font=("Arial 16"),bd=0,state='disabled',padx=10,pady=10,wrap=WORD)
        awtext.pack() 

    # changes the speed of a certain aircraft
    def change_speed(self, flightid, speed):
        if int(speed) >= 1:
            for i in self.current_aircraft_list:
                if i["FlightID"] == flightid:
                    i["speed"] = speed
                    console_printer.insert(END,i["FlightID"]+": new speed is: "+i["speed"])
        else:
            console_printer.insert(END,"Invalid speed change, consult help page")

    # changes the heading of an aircraft, to the parameter "heading" degrees
    def change_heading(self, flightid, heading):
        for i in self.current_aircraft_list:
            if i["FlightID"] == flightid:
                i["heading"] = int(heading)
                console_printer.insert(END,i["FlightID"]+": new heading is: "+str(i["heading"])+" degrees")

    # returns the current heading of an aircraft
    def get_heading(self, flightid):
        for i in self.current_aircraft_list:
            if i["FlightID"] == flightid:
                return i["heading"]

    # changes the altitude of a certain aircraft
    def change_altitude(self, flightid, altitude):
        for i in self.current_aircraft_list:
            if i["FlightID"] == flightid:
                if int(altitude) == i["altitude"]:
                    console_printer.insert(END,"Invalid altitude change for "+i["FlightID"]+": Aircraft is currently at that altitude")
                else:
                    i["altitude"] = int(altitude)*1000
                    console_printer.insert(END,"Altitude changed for "+i["FlightID"]+": Aircraft is cleared for altitude "+str(i["altitude"])+" feet")

    #function to check spacial clearances of all the current aircraft
    #currently have a try statement towards the bottom due to an error i was having, seems to not be printing duplicates
    #tried ~ 20 times - Joe 
    def check_spatials(self):
        verticle_limit = 1000
        horizontal_limit = 50
        coordinates = []
        close_crafts = []
        for i in self.current_aircraft_list:
            flightID = i["FlightID"]
            x_val = i["x_val"]
            y_val = i["y_val"]
            altitude = i["altitude"]
            coordinates.append((flightID, int(x_val), int(y_val), int(altitude)))
        for i in coordinates:
            for j in range (1,len(coordinates)):
                j =  coordinates[j]
                verticle_dist = abs(int(j[3]) - int(i[3]))
                x_diff = abs(int(j[1])-int(i[1]))
                y_diff = abs(j[2]-i[2])
                horizontal_dist = math.sqrt(x_diff**2 + y_diff**2)
                if verticle_dist <= verticle_limit and horizontal_dist <= horizontal_limit and i[0] != j[0]:
                    close_crafts.append((i[0], j[0], horizontal_dist, verticle_dist))
        for i in close_crafts:
            for j in range(1,len(close_crafts)):
                try:
                    j = close_crafts[j]
                except Exception:
                    break
                try:
                    if i[0] == j[1]:
                        close_crafts.remove(i)
                except Exception:
                    break
        #print("Spacial error between "+i[0]+" and "+j[0]+"H,V "+str(horizontal_dist)+" "+str(verticle_dist))
        if close_crafts:
            if self.buffer == '':
                tempstring = 'Spacial error with the following aircrafts: \n'
                for i in close_crafts:
                    tstr = '\n'+i[0]+': '+i[1] # error here 
                    tempstring = tempstring+tstr
                self.buffer = tempstring
            
   
    # get_buffer Function - Joe
    def get_buffer(self):
        return self.buffer

    # clear_buffer Function  - Joe
    def clear_buffer(self):
        self.buffer = ''

    # use the distance formula to figure out new x and y values every 
    # 5 seconds then write that to the buffer to be printed - Joe
    def update_positions(self):
        for i in self.current_aircraft_list:
            currentX = i["x_val"]
            currentY = i["y_val"]
            dx = (i["speed"]/60)*math.sin(math.radians(i['heading']))
            dy = (i["speed"]/60)*math.cos(math.radians(i['heading']))
            i["x_val"] = round(currentX + dx,1)
            i["y_val"] = round(currentY + dy,1)
    
    # hold_aircraft Function - Joe
    def hold_aircraft(self, flightID):
        for i in self.current_aircraft_list:
            if i["FlightID"] == flightID:
                i['speed'] = 0
                console_printer.insert(END,"Holding Aircraft: " + flightID)
    
    # departure_cleared Function - Joe + Nick 
    def departure_cleared(self,flightID):
        for i in self.current_aircraft_list:
            if i["FlightID"] == flightID:
                if i['destination'] != 'Arrival':
                    console_printer.insert(END, flightID + " departure cleared, taking off now!")
                else:
                    console_printer.insert(END,"Error! " + flightID + " is currently in flight in the airspace. Consult the help page.")

    # landing_cleared Function - Joe + Nick
    def landing_cleared(self,flightID):
        for i in self.current_aircraft_list:
            if i["FlightID"] == flightID:
                if i['destination'] == 'Arrival':
                    console_printer.insert(END, flightID + " landing cleared, landing at STL now!")
                else:
                    console_printer.insert(END,"Error! " + flightID + " is currently not in flight in the airspace. Consult the help page.")

    
    # this is used once the termination of the program comes, we need to get rid of any concurrent processes - Joe
    def kill(self):
        self.timer.cancel()
        self.coordinate_timer.cancel()
#################################################################################################################
#^ Backend Code Stops Here ^#

# spawn_task Function - Nick
def spawn_task():

    # creates the listbox class on the UI
    ts = Aircraft_Spawner(tk)

    # randomizes if the aircraft is arriving or departing and then 
    # calls the spawn_aircraft() function to generate the data then
    # calls additem() fucntion from Aircraft_Spawner Class to make 
    # the addition to the UI
    aircraftchoice = random.randint(0,1)
    if(aircraftchoice == 0):
        new_aircraft = Backend_Simulator('main')
        new_aircraft = new_aircraft.spawn_aircraft()
        ts.addItem(new_aircraft)
    else:
        new_aircraft = Backend_Simulator('main')
        new_aircraft = new_aircraft.spawn_aircraft()
        ts.addItem(new_aircraft)
    
    # wait every 15-30 seconds then run again
    waittime = random.randint(15,30)*1000
    tk.after(waittime,spawn_task)

# spatial_check Function - Joe + Nick
def spatial_check():
    # run spatial checking algorithm
    main.check_spatials()
    # print out buffer with spatail result
    if main.get_buffer() != '':
        console_printer.insert(END,main.get_buffer())
        main.clear_buffer()
    tk.after(3000,spatial_check)

# declares the "main" class/backend functionality under main
main = Backend_Simulator('main')
#start_time = time.time()

# simulator Function - Joe + Nick
# function will take in command from getinput() and then 
# parses it's contents
def simulator(command):
    #print("running simulator using " + command + "!") - debugging
    if command == '':
        pass
    # q command = quit the program
    elif command.lower() == 'q':
        main.close_program()
    # help command = open the help window
    elif command.lower() == 'help':
        main.help_window()
    # about command = open the about window
    elif command.lower() == 'about':
        main.about_window()
    # showac command = display all the aircrafts that are on the list
    elif command.lower() == "showac":
        main.print_aircraft(0)
    # checking to see if the user requested an aircratf hold
    elif command.split()[0] in main.get_flight_ids() and command.split()[1].lower() == "h":
        main.hold_aircraft(command.split()[0])
    # checking to see if the user requested an aircratf to takeoff
    elif command.split()[0] in main.get_flight_ids() and command.split()[1].lower() == "t":
        main.departure_cleared(command.split()[0])
    # checking to see if the user requested an aircratf to land
    elif command.split()[0] in main.get_flight_ids() and command.split()[1].lower() == "l":
        main.landing_cleared(command.split()[0])
    # checks for a valid flightID from the console as well as any command with over 3 inputs in the console
    elif command.split()[0] in main.get_flight_ids() and len(command.split()) > 2:
        
        # checking to see if the user requested a change in speed
        if command.split()[1].lower() == "s"  and command.split()[2].isdigit():
            main.change_speed(command.split()[0], command.split()[2])
        
        # checking to see if user requested an alitude change
        elif command.split()[1].lower() == "c":
            if len(command.split()) == 3:
                # change the the heading and turn LEFT
                if command.split()[2].lower() == "l":
                    main.change_heading(command.split()[0], (main.get_heading(command.split()[0])-90))
                # change the heading based and turn RIGHT
                elif command.split()[2].lower() == "r":
                    main.change_heading(command.split()[0], (main.get_heading(command.split()[0])+90))
                # change the heading based on navaid name
                elif command.split()[2].lower() in [d["name"].lower() for d in main.ret_destinations()]:
                    destination = {}
                    aircraft = {}
                    for i in main.ret_destinations():
                        if i["name"].lower() == command.split()[2].lower():
                            destination = i
                    for i in main.current_aircrafts():
                        if i["FlightID"].lower() == command.split()[0].lower():
                            aircraft = i
                    dx = destination["x_cord"] - aircraft["x_val"]
                    dy = destination["y_cord"] - aircraft["y_val"]
                    theta = math.atan(dy/dx)
                    main.change_heading(command.split()[0],(main.get_heading(command.split()[0])+(90-theta)))
                # change the heading based on a int degree value
                elif int(command.split()[2]) >= 0 and int(command.split()[2]) <= 360: # error here, entered 'flightid c a'
                    main.change_heading(command.split()[0], command.split()[2])
            # clear and altitude change
            elif len(command.split()) == 4:
                if command.split()[2].lower() == 'a' and int(command.split()[3]) >= 3 and int(command.split()[3]) <= 30:
                        main.change_altitude(command.split()[0], command.split()[3])
            else:
                console_printer.insert(END,"Invalid Command, type 'help' for useful info")
        # error
        else:
            console_printer.insert(END,"Invalid Command, type 'help' for useful info")
    # error
    else:
        console_printer.insert(END,"Invalid Command, type 'help' for useful info")

# GUI setup - Nick
tk = Tk()
tk.title("ATC-Simulator")
tk['background'] = '#183d54'
tk.state('zoomed')
tk.resizable(False,False)

# run spawning task concurrently with tk at startup
tk.after(0,spawn_task)
tk.after(0,spatial_check)

# console creation
console_printer = Listbox(tk,bg='#1d2329',fg='#ffffff')
console_printer.insert(0,"==== Welcome to ATC-Simulator! ====\n")
console_printer.insert(1,"==== Enter the command 'help' for help on how to use the software! ====\n")
console_printer.insert(2,"==== Enter the command 'about' for info on the software and the team! ====\n")
editor = Entry(tk,bg='#1d2329',fg='#ffffff')
editor.configure(font=("Arial",16))
input = Input_Grab()
editor.bind('<Return>',input.getinput) # upon hitting the enter key, the function getinput() will be prompted
editor.bind('<Up>',input.repeatinput) # upon hitting the up arrow key, function repeatinput() will be prompted
editor.bind('<Down>',input.deleteinput) # upon hitting the down arrow key, function deleteinput() will be prompted
console_printer.configure(font=("Arial",14))
console_printer.place(relx=0.5,rely=0.65,relwidth=0.9,relheight=0.4,anchor=CENTER)
editor.place(relx=0.5,rely=0.875,relwidth=0.9,relheight=0.05,anchor=CENTER)

# mainloop
tk.mainloop()