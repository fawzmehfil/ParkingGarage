import random

#-------Car Class-------#
class car():
  
  def __init__(self):
    
    self.tire_pressure = 30
    self.fuel_level = 0.57
    self.speed = 5
    self.required_oil_change = False
    self.check_engine_light = False
    self.headlights_on = True
    self.colour = "yellow"
    self.model = "BMW"

  def impeed(self, spots, i):

    if spots[i-1] == 1:
      if random.randrange(-1,2,2) > 0:
        impeed_right = False
      else:
        impeed_right = True
    else:
      impeed_right = False
    if spots[i+1] == 1:
      if random.randrange(-1,2,2) > 0:
        impeed_left = False
      else:
        impeed_left = True
    else:
      impeed_left = False
    if impeed_right == False and impeed_left == False:
      return True
    else:
      return False
    
  # checks people
  def checkPeople(self):
    time = 0
    if time == 0:
      peopleBlockingLeft = []
      peopleBlockingRight = []
      for i in range (12):
        peopleBlockingLeft.append(random.randrange(0,2))
        peopleBlockingRight.append(random.randrange(0,2))
      if time <= 3000:
        time += 1
      elif time > 3000:
        time = 0
    

  def spot_empty(self, spots_right, spots_left, i):
    
    #i gives the parking spot # that is being checked on both sides
    spots_left = []
    spots_right = []
    parkable_right = False
    parkable_left = False
    for i in range(12):
      if spots_right[i] == 0:
        parkable_right = True
      elif spots_right[i] == 1:
        parkable_right = False
      if spots_left[i] == 0:
        parkable_left = True
      elif spots_left[i] == 1:
        parkable_left = False
    return parkable_right, parkable_left
    
    
  def spot_parkable(self, spots_right, spots_left, i):

    empty_right, empty_left = self.spot_empty(spots_right, spots_left, i)
    if empty_right == True and self.impeed(spots_right, i) == True:
      parkable_right = True
    else:
      parkable_right = False
    if empty_left == True and self.impeed(spots_left, i) == True:
      parkable_left = True
    else:
      parkable_left = False
    return parkable_right, parkable_left
  

#-------Functions-------#
def autofill_spots():

  # returns lost of the spots that are fille
  spots_left = []
  spots_right = []
  for i in range(12):
    spots_right.append(random.randrange(0,2))
    spots_left.append(random.randrange(0,2))
  return(spots_right, spots_left)

def manualfill_spots():

  while True:
    parking_spaces = input('How many empty parking spaces would you like(0-18):')
    try:
      parking_spaces = int(parking_spaces)
      if parking_spaces >= 0 and parking_spaces <= 18:
        break
      else:
        print('Invalid input. Please try again.'), print()
    except Exception:
      print('Invlaid input. Please try again.'), print()

  spots_right = [1,1,1,1,1,1,1,1,1]
  spots_left = [1,1,1,1,1,1,1,1,1]
  for n in range(parking_spaces):
    if random.randrange(0,2) == 1:
      while True:
        i = random.randrange(0,9)
        if spots_right[i] == 1:
          spots_right[i] = 0
          break
    else:
      while True:
        i = random.randrange(0,9)
        if spots_left[i] == 1:
          spots_left[i] = 0
          break

  return(spots_right, spots_left)

  
#------Main Code-------#

#--Variables--#
vehicle = car()
parked = False
i = 0

# Allows for the user to select the empty parking spots
while True:
  manual_or_automatic = input("Would you like to choose how many open parking spots there will be(y or n)?: ")
  if manual_or_automatic == 'y':
    spots_right, spots_left = manualfill_spots()
    break
  elif manual_or_automatic == 'n':
    spots_right, spots_left = autofill_spots()
    break
  else:
    print('Invalid input. Please try again.'), print()

#--Main While Loop--#
while not parked:
  # Durring this while loop will be the main execution of the code
  # where the GUI will be implemented

  # The methods in the Car Class will be used to determine if the
  # parking spot next to the car is available for parking by determining
  # weather or not there is already a car in the spot, as well as if
  # the cars occupying the neighbouring spot are not impeding on the 
  # open parking spot. If this is the case then car will park in the
  # parkable spot.
  pass
  

    