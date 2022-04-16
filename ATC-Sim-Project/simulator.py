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
import tkinter as tk
# GUI

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
tk.mainloop()
# Simulator Class

# Weather Class

# Runway Class

# Arriving Aircraft Class - Nick

# Departing Aircraft Class -  Nick

# Altitude Class

# Station Class

# Takeoff Class

# Landing Class

# Degree Class

# Scale Class

# Speed Class

# Abort Landing Class

# Abort Takeoff Class