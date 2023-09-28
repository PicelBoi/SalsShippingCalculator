import time
import shutil
import sys
from os import system, name
# Functions
def clear():
 
    # for windows   
    if name == 'nt':  
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def center(string):
	# Turn it into string form
	complete = str(string)
	complete = complete.center(shutil.get_terminal_size().columns)
	for y in range(int(shutil.get_terminal_size().lines / 2)):
		complete = "\n" + complete
	return str(complete)


print("""						  Welcome to...
  ___       _ _      ___ _    _           _              ___      _         _      _                 _   __  
 / __| __ _| ( )___ / __| |_ (_)_ __ _ __(_)_ _  __ _   / __|__ _| |__ _  _| |__ _| |_ ___ _ _  __ _/ | /  \ 
 \__ \/ _` | |/(_-< \__ \ ' \| | '_ \ '_ \ | ' \/ _` | | (__/ _` | / _| || | / _` |  _/ _ \ '_| \ V / || () |
 |___/\__,_|_| /__/ |___/_||_|_| .__/ .__/_|_||_\__, |  \___\__,_|_\__|\_,_|_\__,_|\__\___/_|    \_/|_(_)__/ 
                               |_|  |_|         |___/                             
					(Sal's Shipping Calculator v1.0)                           
						Made by PicelBoi
         			       Give us a sec, we're loading.........
""")
time.sleep(3)
clear()
loop = 1
while loop == 1:	
	try:
		loop = 0
		weight = input(center("How heavy is the item you wish to be delivered?? (Must be in lbs)"))
		if weight == "exit":
			sys.exit("Goodbye!")
		else:
			weight = int(weight)
	except:
		loop = 1
		clear()
		print(center("Please enter a number, float, or integer, not a word, string, boolean, etc."))
		time.sleep(3)
		clear()
cost = 0
clear()

time.sleep(1)

clear()
print(center("Calculating how much it will cost for: " + str(weight) + " lbs"))
time.sleep(3)
def SalsCalculator(shipping):
  if shipping == 1:
    # Ground Shipping
    if weight <= 2:
      cost = 1.50 * weight + 20
    elif weight > 2 or weight <= 6:
      cost = 3.00 * weight + 20
    elif weight > 6 or weight <= 10:
      cost = 4.00 * weight + 20
    elif weight >= 10:
      cost = 4.75 * weight + 20
  elif shipping == 2:
    # Ground Shipping Premium
    cost = 125
  elif shipping == 3:
    # Drone Shipping
    if weight <= 2:
      cost = 4.50 * weight + 20
    elif weight > 2 or weight <= 6:
      cost = 9.00 * weight + 20
    elif weight > 6 or weight <= 10:
      cost = 12.00 * weight + 20
    elif weight >= 10:
      cost = 14.25 * weight + 20
  return str(cost)

#Tell the customer
clear()
print(center("Shipping Cost for Sal's Ground Shipping: $" + SalsCalculator(1)))
input(center("Press Enter to go next..."))
print(center("Shipping Cost for Sal's Ground Shipping Premium: $" + SalsCalculator(2)))
input(center("Press Enter to go next..."))
print(center("Shipping Cost for Sal's Drone Shipping: $" + SalsCalculator(3)))
input(center("Press Enter to go next..."))
clear()
print("Thanks for using Sal's Shipping Calculator! Goodbye.")
print("""Credits:
	 
	 -Codeacademy for the idea
	 -Me (PicelBoi) for making it happen that lots of people did before
	 -Python for existing """)
