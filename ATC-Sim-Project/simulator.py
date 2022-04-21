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
import math
from tkinter.messagebox import askyesno

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

# Aircraft Spawner Class - Nick
class Aircraft_Spawner:
    
    # list of our aircrafts being created by simulator
    aircraft_list = []

    def __init__(self,tk):
        # list box taking input of spawning planes and displaying that info
        self.listbox = Listbox(tk,selectmode=SINGLE,bg='#0d212e',fg='#ffffff')
        self.listbox.configure(font=("Arial",14))
        self.listbox.bind('<Double-1>',self.click_progress_strip)
        self.listbox.place(relwidth=0.8,relheight=0.4,relx=0.1,rely=0.1)

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

# Backend_Simulator - Joe + Nick
class Backend_Simulator:
    
    #it says in the name
    current_aircraft_list = []
    # list of aircraft models (the robinson44 is our helicopter model)
    aircraft_models = ["BA747", "Cessna172", "Robinson44", "CRJ900"]
    # list of airline names to go into the flightID
    airline_names = ["SWA","DAL","ASQ","QXE"]
    # list of navaids our departing aircrafts will head to
    destinations = [
    {"name": "SCHMD", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "CABIT", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "KLAIR", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "SAGME", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "SAGZA", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "SAJOY", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "WEDOG", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "CHIKN", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "MELVY", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "DEECE", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "SAGZA", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "SKYPE", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "MYKEY", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "TEWHY", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "FRALE", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "MUZUL", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "STAAN", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "TWILA", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "AUGST", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "LEEAN", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "SNYDR", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)},
    {"name": "PLESS", "x_cord": random.randint(-100,100), "y_cord": random.randint(-100,100)}
    ]
    
    # spawns an aircraft to the map
    def spawn_aircraft(self):
        flightid = random.choice(self.airline_names)+str(random.randint(1000, 9999))
        x_val = random.randint(-100,100)
        y_val = random.randint(3,30)
        z_val = random.randint(-100,100)
        speed_value = random.randint(100,10000)
        heading = random.randint(0,360)
        model = random.choice(self.aircraft_models)
        destination = random.choice(self.destinations)
        #departing = random.randint(0,1) will need to add this but will have to change the x,y,z, speeed and more
        new_aircraft = {
            "FlightID": flightid,
            "heading": heading,
            "altitude": y_val*1000,
            "model": model,
            "destination": destination["name"],
            "speed": speed_value,
            #"departing": departing,
            "x_val": x_val,
            "z_val": z_val,
        }
        self.current_aircraft_list.append(new_aircraft)
        return new_aircraft

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
        else:
            pass

    # creates a popup window with all the helpful 
    # information you would need to operate the software
    def help_window(event):
        # popup setup
        helpwindow = Toplevel(tk,bg='#183d54')
        helpwindow.geometry("600x600")
        helpwindow.title("Help")
        # title label setup
        hwtitle = Label(helpwindow,text="Help")
        hwtitle.configure(bg='#183d54',fg='#ffffff',font=("Arial 32"))
        hwtitle.pack()
        # textbox setup
        hwtext = Text(helpwindow)
        hwtext.insert(INSERT,"\nBasic Info:\n")
        hwtext.insert(INSERT,"+ Aircrafts will spawn every 15-30 seconds. You will see all the important air traffic info displayed in the top box. The bottom box will contain a console for the user to type in commands (see help on commands down below). The box will also contain all history of the inputs the user has made into the console (valid and invalid alike) as well as the resulting output. \n")
        hwtext.insert(INSERT,"\n1. Understanding the Air Traffic:\n")
        hwtext.insert(INSERT,"+ First Item: FlightID = main value being the distinction between each aircraft. \n")
        hwtext.insert(INSERT,"+ Second Item: Heading(in deg) = the direction of the aircraft in degrees. \n")
        hwtext.insert(INSERT,"+ Third Item: Altitude(in ft) = the number of ft an aircraft is in the air. \n")
        hwtext.insert(INSERT,"+ Fourth Item: Model of Aircraft = the type of aircraft. \n")
        hwtext.insert(INSERT,"+ Fifth Item: Destination Info = the indicated direction of the aircraft. \n")
        hwtext.insert(INSERT,"+ Sixth Item: Aircraft Speed = the indicated speed of the aircraft. \n")
        hwtext.insert(INSERT,"\n2. Understanding the Controls/Commands:\n")
        hwtext.insert(INSERT,"+ 'help' = it's how you opened this help window! \n")
        hwtext.insert(INSERT,"+ 'about' = opens the about window. \n")
        hwtext.insert(INSERT,"+ 'q' = quits the program. \n")
        hwtext.insert(INSERT,"+ 's' = changes the speed for an indicated aircraft(using FlightID). Must follow up the command with a valid number. \n")
        hwtext.insert(INSERT,"+ 'h' = changes the heading an indicated aircraft(using FlightID). Must follow up the command with either an 'l', 'r', navaid name, or valid heading number to represent the heading in degress. \n")
        hwtext.insert(INSERT,"+ 'c' = changes the altitude an indicated aircraft(using FlightID). Must be followed up with a value between 3 and 36(the value gets multiplied by 1000 to depict legitimate altitude). \n")
        hwtext.configure(bg='#183d54',fg='#ffffff',font=("Arial 16"),bd=0)
        hwtext.pack()   
    
    # creates a popup window with all the
    # information you would need to about the software
    def about_window(event):
        # popup setup
        aboutwindow = Toplevel(tk,bg='#183d54')
        aboutwindow.geometry("600x600")
        aboutwindow.title("About")
        # title label setup
        awtitle = Label(aboutwindow,text="About")
        awtitle.configure(bg='#183d54',fg='#ffffff',font=("Arial 32"))
        awtitle.pack()
        # textbox setup
        awtext = Text(aboutwindow)
        awtext.insert(INSERT,"About the Software:\n")
        awtext.insert(INSERT,"The product we were assigned with developing is an Air Traffic Control Simulator, based on the atc-sim.com web app. This should be able to simulate planes approaching and taking off from the STL (St. Louis Lambert) airport, as well as planes passing through the area. The product should also give the user the ability to act as an air traffic controller by giving the user the necessary commands to be able to direct and control each of the simulated planes around the airport. Just as any Air Traffic Controller would be able to do. \n")
        awtext.insert(INSERT,"\nThe Arch Development Team:\n")
        awtext.insert(INSERT,"+ Sarah McLellan \n")
        awtext.insert(INSERT,"+ Joe Davidson \n")
        awtext.insert(INSERT,"+ Nick Rader \n")
        awtext.insert(INSERT,"+ Cameron Meadows \n")
        awtext.insert(INSERT,"+ Declan Worely \n")
        awtext.insert(INSERT,"+ Connor Willans \n")
        awtext.configure(bg='#183d54',fg='#ffffff',font=("Arial 16"),bd=0)
        awtext.pack() 



    # changes the speed of a certain aircraft
    def change_speed(self, flightid, speed):
        if int(speed) >= 1:
            for i in self.current_aircraft_list:
                if i["FlightID"] == flightid:
                    i["speed"] = speed
                    console_printer.insert(END,i["FlightID"]+": new speed is: "+i["speed"])
        else:
            console_printer.insert(END,"Invalid speed change")

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
                    i[altitude] = int(altitude)*1000
                    console_printer.insert(END,"Altitude changed for "+i["FlightID"]+": Aircraft is cleared for altitude "+str(i[altitude])+" feet")


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
        new_aircraft = Backend_Simulator()
        new_aircraft = new_aircraft.spawn_aircraft()
        ts.addItem(new_aircraft)
    else:
        new_aircraft = Backend_Simulator()
        new_aircraft = new_aircraft.spawn_aircraft()
        ts.addItem(new_aircraft)
    
    # wait every 10 seconds then run again
    tk.after(10000,spawn_task)

#declares the "main" class/backend functionality under main
main = Backend_Simulator()

# getinput Function - Nick
# function will assign whatever comes from the entry bar 
# to command and then makes front end changes and then sends 
# command to be parsed by simulator
def getinput(command):
    command = editor.get()
    if command:
        editor.delete(0,'end')
        console_printer.insert(END,command)
        console_printer.insert(END,"====================")
        simulator(command)
    else:
        pass

# simulator Function - Joe + Nick
# function will take in command from getinput() and then 
# parses it's contents
def simulator(command):
    #print("running simulator using " + command + "!") - debugging
    if command.lower() == 'q':
        main.close_program()
    elif command.lower() == 'help':
        main.help_window()
    elif command.lower() == 'about':
        main.about_window()
    # checks for a valid flightID from the console
    elif command.split()[0] in main.get_flight_ids():
        console_printer.insert(END,"You entered a valid flightID")
        # checking to see if the user requested a change in speed
        if command.split()[1].lower() == "s"  and command.split()[2].isdigit():
            main.change_speed(command.split()[0], command.split()[2])
        elif command.split()[1].lower() == "h":
            # change the heading and turn LEFT
            if command.split()[2].lower() == "l":
                main.change_heading(command.split()[0], (main.get_heading(command.split()[0])-90))
            # change the heading and turn RIGHT
            elif command.split()[2].lower() == "r":
                main.change_heading(command.split()[0], (main.get_heading(command.split()[0])+90))
            # change the heading and turn to a NAVAID
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
                dy = destination["y_cord"] - aircraft["z_val"]
                theta = math.atan(dy/dx)
                main.change_heading(command.split()[0],(main.get_heading(command.split()[0])+(90-theta)))
            # change the heading based on a int value
            elif int(command.split()[2]) >= 0 and int(command.split()[2]) <= 360:
                main.change_heading(command.split()[0], command.split()[2])
            # error
            else: 
                console_printer.insert(END,"Invalid Command")
        # checking to see if user requested an alitude change
        elif command.split()[1].lower() == "c" and int(command.split()[2]) >= 3 and int(command.split()[2]) <= 30:
            main.change_altitude(command.split()[0], command.split()[2])
        # error
        else:
            console_printer.insert(END,"Invalid Command")
    # error
    else:
        console_printer.insert(END,"Invalid Command")

# GUI setup - Nick
tk = Tk()
tk.title("ATC-Simulator")
tk['background'] = '#183d54'
tk.geometry("1200x700")
#tk.resizable(False,False)

# run spawning task concurrently with tk at startup
tk.after(0,spawn_task)

# console creation
console_printer = Listbox(tk,bg='#1d2329',fg='#ffffff')
console_printer.insert(0,"==== Welcome to ATC-Simulator! ====")
console_printer.insert(1,"==== Enter the command 'help' for help on how to use the software! ====")
console_printer.insert(2,"==== Enter the command 'about' for info on the software and the team! ====")
editor = Entry(tk,bg='#1d2329',fg='#ffffff')
editor.configure(font=("Arial",16))
editor.bind('<Return>',getinput) # upon hitting the enter key, the function getinput() will be prompted
console_printer.configure(font=("Arial",14))
console_printer.place(relx=0.5,rely=0.7,relwidth=0.8,relheight=0.3,anchor=CENTER)
editor.place(relx=0.5,rely=0.9,relwidth=0.8,relheight=0.05,anchor=CENTER)

# mainloop
tk.mainloop()