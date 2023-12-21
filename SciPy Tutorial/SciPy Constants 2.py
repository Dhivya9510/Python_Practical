# SciPy Constants

# Constants in SciPy
  # As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.
  # These constants can be helpful when you are working with Data Science.
  # PI is an example of a scientific constant.

#Example:
  # Print the constant value of PI:

from scipy import constants

print(constants.pi)

# Constant Units
  # A list of all units under the constants module can be seen using the dir() function.

# Example
   # List all constants:

from scipy import constants

print(dir(constants))

# Unit Categories
  # The units are placed under these categories:

# Metric      - (Meter)
# Binary      - (Bytes)
# Angle       - (Radians)
# Mass        - (KG)
# Time        - (Seconds)
# Length      - (Meters)
# Pressure    - (Pascals)
# Speed       - (Meters per Second)
# Volume      - (Cubic Meters)
# Temperature - (Kelvin)
# Force      - (Newton)
# Energy     - (Joules)
# Power      - (Watts)
# Area       - (Square Meters)

# Metric (SI) Prefixes:
   # Return the specified unit in meter (e.g. centi returns 0.01)

from scipy import constants

print(constants.yotta)
print(constants.zetta) 
print(constants.exa) 
print(constants.peta) 
print(constants.tera) 
print(constants.giga) 
print(constants.mega) 
print(constants.kilo) 
print(constants.hecto) 
print(constants.deka) 
print(constants.deci) 
print(constants.centi) 
print(constants.milli) 
print(constants.micro) 
print(constants.nano) 
print(constants.pico) 
print(constants.femto) 
print(constants.atto) 
print(constants.zepto) 

# Binary Prefixes:
  # Return the specified unit in bytes (e.g. kibi returns 1024)
  # Example

from scipy import constants

print(constants.kibi)
print(constants.mebi)
print(constants.gibi)
print(constants.tebi)
print(constants.pebi)
print(constants.exbi)
print(constants.zebi)
print(constants.yobi)

# Mass:
  # Return the specified unit in kg (e.g. gram returns 0.001)
  # Example: from scipy import constants

print(constants.gram)        #0.001
print(constants.metric_ton)  
print(constants.grain)       
print(constants.lb)         
print(constants.pound)       
print(constants.oz)          
print(constants.ounce)     
print(constants.stone)       
print(constants.long_ton)    
print(constants.short_ton)   
print(constants.troy_ounce) 
print(constants.troy_pound)  
print(constants.carat)       
print(constants.atomic_mass) 
print(constants.m_u)         
print(constants.u) 

# Angle:
  # Return the specified unit in radians (e.g. degree returns 0.017453292519943295)
  # Example

from scipy import constants
print(constants.degree)     
print(constants.arcmin)     
print(constants.arcminute)  
print(constants.arcsec)    
print(constants.arcsecond) 
 
# Time:
   # Return the specified unit in seconds (e.g. hour returns 3600.0)
   # Example
from scipy import constants
print(constants.minute)     
print(constants.hour)        
print(constants.day)         
print(constants.week)       
print(constants.year)        
print(constants.Julian_year) 

# Length:
  # Return the specified unit in meters (e.g. nautical_mile returns 1852.0)
  # Example
from scipy import constants

print(constants.inch)              #0.0254
print(constants.foot)              #0.30479999999999996
print(constants.yard)             
print(constants.mile)            
print(constants.mil)              
print(constants.pt)                
print(constants.point)            
print(constants.survey_foot)       
print(constants.survey_mile)       
print(constants.nautical_mile)     
print(constants.fermi)             
print(constants.angstrom)          
print(constants.micron)            
print(constants.au)               
print(constants.astronomical_unit) 
print(constants.light_year)        
print(constants.parsec)    

# Pressure:
  # Return the specified unit in pascals (e.g. psi returns 6894.757293168361)
  # Example
from scipy import constants

print(constants.atm)         
print(constants.atmosphere)  
print(constants.bar)         
print(constants.torr)        
print(constants.mmHg)       
print(constants.psi)   

# Area:
  # Return the specified unit in square meters(e.g. hectare returns 10000.0)
  # Example
from scipy import constants

print(constants.hectare) 
print(constants.acre)  

# Volume:
  # Return the specified unit in cubic meters (e.g. liter returns 0.001)
  # Example
from scipy import constants

print(constants.liter)            
print(constants.litre)            
print(constants.gallon)           
print(constants.gallon_US)        
print(constants.gallon_imp)       
print(constants.fluid_ounce)      
print(constants.fluid_ounce_US)   
print(constants.fluid_ounce_imp) 
print(constants.barrel)           
print(constants.bbl)  

# Speed:
   # Return the specified unit in meters per second (e.g. speed_of_sound returns 340.5)
   # Example
from scipy import constants

print(constants.kmh)           
print(constants.mph)         
print(constants.mach)           
print(constants.speed_of_sound) 
print(constants.knot)  

# Temperature:
  # Return the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)
  # Example
from scipy import constants

print(constants.zero_Celsius)      
print(constants.degree_Fahrenheit) 

# Energy:
   # Return the specified unit in joules (e.g. calorie returns 4.184)
   # Example
from scipy import constants

print(constants.eV)           
print(constants.electron_volt) 
print(constants.calorie)       
print(constants.calorie_th)    
print(constants.calorie_IT)    
print(constants.erg)           
print(constants.Btu)          
print(constants.Btu_IT)       
print(constants.Btu_th)        
print(constants.ton_TNT)   

# Power:
  # Return the specified unit in watts (e.g. horsepower returns 745.6998715822701)
  # Example
from scipy import constants

print(constants.hp)         
print(constants.horsepower) 

# Force:
  # Return the specified unit in newton (e.g. kilogram_force returns 9.80665)
  # Example
from scipy import constants

print(constants.dyn)            
print(constants.dyne)            
print(constants.lbf)             
print(constants.pound_force)    
print(constants.kgf)             
print(constants.kilogram_force) 