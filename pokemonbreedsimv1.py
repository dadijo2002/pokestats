'''
This program is used to simulate and calculate statistics for Pokemon IV breeding.

Author: Daniel Dickson
Discord: Dadijo2002#3072
Start Date: April 8, 2021

Version: 1.0
Release: December 24, 2021 
'''

import random

def get_ivs():
  '''
  This function gets the initial IVs of the pokemon being bred.
  '''

  ivs = []    # Initializes list used to keep track of all IVs
  n = 0       # Initializes stat counter for user-friendliness

  while n < 6:        # affects stat named during input collection
    if n == 0:
      stat = "HP"
    elif n == 1:
      stat = "ATK"
    elif n == 2:
      stat = "DEF"
    elif n == 3:
      stat = "SPE"
    elif n == 4:
      stat = "SPA"
    elif n == 5:
      stat = "SPD"
    iv = input("Enter IV for stat " + stat + ": ")    # Input used to ask for stat
    try:      # Input validation
      if int(iv) >= 0 and int(iv) <= 31:
        ivs.append(int(iv))   # If IV given is a valid value, it is added to the list
        n += 1
    except:   # If IV given is an invalid value, the input prompt is asked again
      n = n

  print()

  return ivs    # A list of IVs is returned

def get_guaranteed_ivs(ivs1, ivs2):
  '''
  This function gets and keeps track of any guaranteed IVs due to held items during breeding.
  '''

  proceed = False         # Flag for input validation
  is_giv1 = ""            # Whether or not Pokemon 1 passes down an IV
  is_giv2 = ""            # Whether or not Pokemon 2 passes down an IV
  ivslist = ["HP", "ATK", "DEF", "SPE", "SPA", "SPD"]
  keepIVs_type = []       # final list (len 0-2) of IV types to keep

  while proceed == False:   # Asks for input about pokemon 1 passing down an IV
    is_giv1 = input("Will pokemon 1 pass down a guaranteed IV? (Y/N) ")
    if is_giv1.upper() == "Y" or is_giv1.upper() == "N":  # Input validation
      proceed = True

  proceed = False     # reset flag for future use

  while proceed == False:   # Asks for input about pokemon 1 passing down an IV
    is_giv2 = input("Will pokemon 2 pass down a guaranteed IV? (Y/N) ")
    if is_giv2.upper() == "Y" or is_giv2.upper() == "N":   # Input validation
      proceed = True

  print()

  proceed = False     # reset flag for future use

  if is_giv1.upper() == "Y":    # If Pokemon 1 passes down an IV, this is activated
    print(*ivslist, sep="\t")
    print(*ivs1, sep="\t")
    while proceed == False:
      keepIV = input("Which IV will be passed down? ")     # Ask for which IV
      keepIV = keepIV.upper()
      if keepIV in ivslist:     # Input validation
        proceed = True
    print()
    keepIVs_type.append(keepIV)   # If valid input, keeps track of the IV and its value
  elif is_giv1.upper() == "N":
    keepIVs_type.append("")


  proceed = False
  
  if is_giv2.upper() == "Y":    # If Pokemon 2 passes down an IV, this is activated
    print(*ivslist, sep="\t")
    print(*ivs2, sep="\t")
    while proceed == False:
      keepIV = input("Which IV will be passed down? ")     # Ask for which IV
      keepIV = keepIV.upper()
      if keepIV in ivslist:     # Input validation
        proceed = True
    keepIVs_type.append(keepIV)   # If valid input, keeps track of the IV and its value

  return keepIVs_type    # Returns the IVs to keep


def isDestinyKnot():
  '''
  This function checks if a Destiny Knot is in use for breeding.
  '''
  proceed = False

  while proceed == False:   # Asks if Destiny Knot is being used
    destinyKnot = input("Is a Destiny Knot in use? (Y/N) ")
    if destinyKnot.upper() == "Y" or destinyKnot.upper() == "N":   # Input validation
      proceed = True
  
  if destinyKnot.upper() == "Y":
    return True
  else:
    return False

def getTargetIVs():
  '''
  This function asks the user how IVs of a specified value to look for.
  '''
  ivInfo = []   # A list of the final values given
  proceed = False # Flag for input validation

  while proceed == False: # Input validation (numbers within range)
    totalIVsCount = input("How many IVs are desired? ")
    desiredIVsVal = input("What should the IV's value(s) be? ")

    try:        # Input validation
      totalIVsCount = int(totalIVsCount)
    except:
      print("Invalid number of IVs given.")
      totalIVsCount = getTargetIVs()

    try:        # Input validation
      desiredIVsVal = int(desiredIVsVal)
    except:
      print("Invalid target IV value.")
      desiredIVsVal = getTargetIVs()

    if (totalIVsCount >= 0 and
        totalIVsCount <= 6 and
        desiredIVsVal >= 0 and
        desiredIVsVal <= 31):
      proceed = True

  ivInfo.append(totalIVsCount)
  ivInfo.append(desiredIVsVal)

  return ivInfo

def breedNormal(ivs1, ivs2, keepIVs_type):
  '''
  This function simulates one breeding trial without the use of a Destiny Knot.
  '''

  ivslist = ["HP", "ATK", "DEF", "SPE", "SPA", "SPD"]
  ivIndex = 0
  finalIVs = []

  for i in range(0,6):  # generate 6 random IVs
    finalIVs.append(random.randint(0,31))
  
  # figure out if any IVs are inherited, and replace the generated one(s) with them

  if len(keepIVs_type) == 2 and keepIVs_type[0] == keepIVs_type[1]:
    #if the same IV can be inherited from both parents, randomly choose
    # which one is inherited and add to list
    ivIndex = ivslist.index(keepIVs_type[0])
    ivChoice = random.randint(0,1)
    if ivChoice == 0:
      finalIVs[ivIndex] = int(ivs1[ivIndex])
    elif ivChoice == 1:
      finalIVs[ivIndex] = int(ivs2[ivIndex])

  else:
    # if all inherited IVs are unique, figure out from which parent they are
    # inherited and add to list
    if len(keepIVs_type) == 2 and keepIVs_type[0] == "":
      ivIndex = ivslist.index(keepIVs_type[1])
      finalIVs[ivIndex] = int(ivs2[ivIndex])
    elif len(keepIVs_type) == 2:
      ivIndex = ivslist.index(keepIVs_type[0])
      finalIVs[ivIndex] = int(ivs1[ivIndex])
      ivIndex = ivslist.index(keepIVs_type[1])
      finalIVs[ivIndex] = int(ivs2[ivIndex])
    elif len(keepIVs_type) == 1 and keepIVs_type[0] != '':
      ivIndex = ivslist.index(keepIVs_type[0])
      finalIVs[ivIndex] = int(ivs1[ivIndex])

  return finalIVs

def breedDestinyKnot(ivs1, ivs2, keepIVs_type):
  '''
  This function simulates one breeding trial without the use of a Destiny Knot.
  '''

  ivslist = ["HP", "ATK", "DEF", "SPE", "SPA", "SPD"]
  ivIndex = 0
  finalIVs = [-1, -1, -1, -1, -1, -1]
  ivRandomizer = 0
  proceed = False

  # use the destiny knot while accounting for inherited IVs

  if len(keepIVs_type) == 1 and keepIVs_type[0] != '':
    # if 1 IV from the first parent is kept, add it to the list of final IVs 
    ivIndex = ivslist.index(keepIVs_type[0])
    finalIVs[ivIndex] = int(ivs1[ivIndex])

    while proceed == False:
      # generate a random IV and make sure it is not the inherited one
      # since the Destiny Knot only inherits 5 IVs, one must still be random
      ivRandom = random.randint(0,5)
      if ivRandom != ivIndex:
        finalIVs[ivRandom] = random.randint(0,31)
        proceed = True

  elif len(keepIVs_type) == 2 and keepIVs_type[0] == "":
    # if 1 IV from the second parent is kept, add it to the list of final IVs
    ivIndex = ivslist.index(keepIVs_type[1])
    finalIVs[ivIndex] = int(ivs2[ivIndex])
    # generate a random IV and make sure it is not the inherited one
    # since the Destiny Knot only inherits 5 IVs, one must still be randomne
    while proceed == False:
      ivRandom = random.randint(0,5)
      if ivRandom != ivIndex:
        finalIVs[ivRandom] = random.randint(0,31)
        proceed = True

  elif len(keepIVs_type) == 0:
    # generate any random IV
      # since the Destiny Knot only inherits 5 IVs, one must still be random
    ivRandom = random.randint(0,5)
    finalIVs[ivRandom] = random.randint(0,31)

  ivIndex = 0

  for iv in finalIVs:
    # for any IVs that have not already been generated, randomly choose from which
    # parent they are inherited and add them to the list
    if iv == -1:
      ivRandomizer = random.randint(0,1)
      if ivRandomizer == 0:
        finalIVs[ivIndex] = ivs1[ivIndex]
      elif ivRandomizer == 1:
        finalIVs[ivIndex] = ivs2[ivIndex]
    ivIndex += 1

  return finalIVs

def ivCheck(ivs1, ivs2, keepIVs_type, ivInfo, isDestinyKnot):
  '''
  This function checks how many times the simulation occurs until the number of IVs specified or greater are equal to the desired IV value.
  '''
  proceed = False   # Loops the simulation until there is a successful attempt
  count = 0   # Counts attempts
  finalIVs = []

  while proceed == False:
    # start simulating IVs based on whether or not a destiny knot is in use
    if isDestinyKnot == True:
      finalIVs = breedDestinyKnot(ivs1, ivs2, keepIVs_type)
      # keep track of total attempts
      count += 1
    else:
      finalIVs = breedNormal(ivs1, ivs2, keepIVs_type)
      # keep track of total attempts
      count += 1

    if finalIVs.count(ivInfo[1]) >= ivInfo[0]:
      # if the uer provided criteria is met, stop the simulation
      proceed = True

  return count, finalIVs    # Returns the total number of simulation trials until there was a successful attempt

def simOneBreed():
  '''
  This function wull simulate one egg's stats.
  '''

  # get the IVs of both parents
  ivs1 = get_ivs()
  ivs2 = get_ivs()

  destinyKnot = False

  print("-"*20)

  finalIVs = []
  
  # ask which IVs are inherited if any
  keepIVs_type = get_guaranteed_ivs(ivs1, ivs2)

  # ask if destiny knot is in use if less than 2 parents are using a power item
  # to inherit IVs
  if len(keepIVs_type) < 2 or keepIVs_type[0] == "":
    destinyKnot = isDestinyKnot()
    print()
  
  # simulate breeding depending on destiny knot status
  if destinyKnot == True:
    finalIVs = breedDestinyKnot(ivs1, ivs2, keepIVs_type)
  else:
    finalIVs = breedNormal(ivs1, ivs2, keepIVs_type)

  return finalIVs

def simTallyBreed():
  '''
  This function simulates egg stats until the user's requirements are met.
  '''
  destinyKnot = False
  finalIVs = []

  # get the IVs of both parents
  ivs1 = get_ivs()
  ivs2 = get_ivs()

  print("-"*20)

  # get what stats the user wants to see
  ivInfo = getTargetIVs()
  
  # figure out which IVs will be inherited via power items
  keepIVs_type = get_guaranteed_ivs(ivs1, ivs2)

  # If less than 2 parents are using power items, figure out if destiny knot
  # is in use
  if len(keepIVs_type) < 2:
    destinyKnot = isDestinyKnot()
    print()
  elif len(keepIVs_type) == 2 and keepIVs_type[0] == '':
    # this condition is for if the second parent is using a power item but
    # the first is not
    destinyKnot = isDestinyKnot()
    print()
  
  # simulate breeding based on whether or not there is a destiny knot in use
  if destinyKnot == True:
    totalSims = ivCheck(ivs1, ivs2, keepIVs_type, ivInfo, True)
  else:
    totalSims = ivCheck(ivs1, ivs2, keepIVs_type, ivInfo, False)

  return totalSims

def simHundredTallyBreed():
  '''
  This function simulates egg stats until the user's requirements are met 100 times, then
  produces an average count until that condition was met.
  '''
  destinyKnot = False
  finalIVs = []
  totalSims = 0

  # get the IVs of both parents
  ivs1 = get_ivs()
  ivs2 = get_ivs()

  print("-"*20)

  # get the stats the user wants to see
  ivInfo = getTargetIVs()
  
  # figure out which IVs will be inherited via power items
  keepIVs_type = get_guaranteed_ivs(ivs1, ivs2)

  # If less than 2 parents are using power items, figure out if destiny knot
  # is in use
  if len(keepIVs_type) < 2:
    destinyKnot = isDestinyKnot()
    print()
  elif len(keepIVs_type) == 2 and keepIVs_type[0] == '':
    # this condition is for if the second parent is using a power item but
    # the first is not
    destinyKnot = isDestinyKnot()
    print()
  
  # simulate breeding based on whether or not there is a destiny knot in use 100 times
  for i in range(0,100):
    if destinyKnot == True:
      results = ivCheck(ivs1, ivs2, keepIVs_type, ivInfo, True)
      # add the total simulations to the count
      totalSims += results[0]
    else:
      results = ivCheck(ivs1, ivs2, keepIVs_type, ivInfo, False)
      # add the total simulations to the count
      totalSims += results[0]
  
  # calculate the average eggs until desired stats were achieved
  totalSimsAvg = totalSims / 100

  return totalSimsAvg

def printResults(result):
  """
  This function prints out the results of the simulation for options 1 and 2 (since
  they both display the final IVs) of the simulator in a user-friendly format.
  """
  ivslist = ["HP", "ATK", "DEF", "SPE", "SPA", "SPD"]

  print("-"*20)
  print()
  print("Offspring IVs:")
  print(*ivslist, sep="\t")
  print(*result, sep="\t")

def menu():

  choice = 0

  print("1. Simulate one egg for IVs")
  print("2. Simulate one egg until desired IVs")
  print("3. Simulate one egg until desired IVs one hundred times")

  while choice > 3 or choice < 1:
    # input validation
    choice = int(input("Please choose an option: "))

  print()
  
  # start each corresponding simulation and print the results
  if choice == 1:
    result = simOneBreed()
    printResults(result)
  elif choice == 2:
    result = simTallyBreed()
    print("Number of eggs: ", result[0])
    printResults(result[1])
  elif choice == 3:
    result = simHundredTallyBreed()
    print("Average number of eggs: ", result)

menu()