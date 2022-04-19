from tkinter import *
import random 

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
        #print(new_aircraft) #gui printout of aircraft
        return new_aircraft

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
        #print(new_aircraft)
        return new_aircraft

class Test:

    index = 0
    def __init__(self, tk):
        self.listbox = Listbox(tk,selectmode=SINGLE,bg='#0d212e',fg='#ffffff')
        self.listbox.place(relwidth=0.7,relheight=0.5,relx=0.1,rely=0.1)

    def addItem(self,ac):
        print(ac)
        self.listbox.insert(Test.index,ac)
        Test.index = Test.index + 1
        print(self.listbox.size())

def task():
    tt = Test(tk)
    aircraftchoice = random.randint(0,1)
    if(aircraftchoice == 0):
        newaircraft = Arriving_Aircraft('newaircraft')
        newaircraft = newaircraft.spawn_aircraft()
        tt.addItem(newaircraft)
    else:
        newaircraft = Departing_Aircraft('newaircraft')
        newaircraft = newaircraft.spawn_aircraft()
        tt.addItem(newaircraft)
    tk.after(2000,task)

tk = Tk()
tk.title("test")
tk['background'] = '#183d54'
tk.geometry("600x500")
tk.after(5000,task)
tk.mainloop()