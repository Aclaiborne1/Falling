from math import pi

# constants and conversion factors
Acc_Grav = 9.8101
feet_per_meter = 3.2808399
fps_to_mph = 0.68181818

# function for converting fahrenheit to celsius
def F_to_C(degF):
        return(degF - 32.0) * (5./9.)

# function for calculating air density
def air_density(temperature):
        kelvin = F_to_C(temperature) + 273.15
        Pa = 101325 # standard sea level air pressure
        R = 287.058 # gas constant for dry air
        return(Pa/(R * kelvin))

Acceleration = Acc_Grav
interval = 0
Velocity = 0
distance = 0

mass_gms = float(raw_input("enter rocket total mass in gms: "))

Diameter = float(raw_input("enter rocket diameter in mm: "))

Coefficient_drag = float(raw_input("Enter coefficient of drag: "))

Temperature = int(raw_input("enter temperature in degrees F: "))

Mass = mass_gms / 1000.0 # mass in kilograms
Dia_meters = Diameter / 1000.0

while True:
    durationp = raw_input("fall for duration or to terminal velocity - enter (d) or (t): ")
    if (durationp in ['D','T','d','t']):
        break
    else:
        print "Please enter 'D' or 'T'"

if (durationp in ['D','d']):
        duration = float(raw_input("enter duration of fall: "))

# The following line obtains the density of air at Temperature in Fahrenheit in kg/m^3
Rho = air_density(Temperature)

# Now compute drag value
Drag_Value = 0.5 * Rho * pi * Coefficient_drag*((Dia_meters/2.0)**2)

print 'Time\td\tV(m/s)\tV(fps)\tV(mph)'

test = True

while(test):
        interval +=1
        Time=interval * 0.1
        Drag = Drag_Value * (Velocity **2)
        Force = Mass * Acc_Grav - Drag
        Acceleration = Force / Mass
        Velocity += Acceleration * 0.1
        distance += Velocity * 0.1 * feet_per_meter
        VFS = Velocity * feet_per_meter
        VMH = VFS * fps_to_mph
        print '%.2f\t%.2f\t%.2f\t%.2f\t%.2f'%(Time, distance, Acceleration, VFS, VMH)
        if (durationp in ['D', 'd']):
                test = (Time < duration)
        if (durationp in ['T', 't']):
                test = (Acceleration > 0.1)
                    
print
print 'Velocity at end of fall: %.2f miles per hour'%(VMH)        
        
