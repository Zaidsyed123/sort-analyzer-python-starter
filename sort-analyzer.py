# SORT ANALYZER STARTER CODE

import time

def bubbleSort(anArray): 
  for i in range(0, len(anArray) - 1):
    for elements in range(0, len(anArray) - i - 1):
      if anArray[elements] > anArray[elements + 1]:
        anArray[elements], anArray[elements + 1] = anArray[elements + 1], anArray[elements]

def selectionSort(anArray):
  for i in range(len(anArray)-1):
    minIndex = i
    for el in range(i+1, len(anArray)):
      if anArray[el] < anArray[minIndex]:
        minIndex = el
    anArray[i], anArray[minIndex] = anArray[minIndex], anArray[i]

def insertionSort(anArray):
  for i in range(1, len(anArray)):
    currVal = anArray[i]
    currPos = i - 1
    
    while currPos >= 0 and anArray[currPos] > currVal:
      anArray[currPos + 1] = anArray[currPos]
      currPos -= 1
    
    anArray[currPos + 1] = currVal
 
# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp

# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

startTime = time.time()
bubbleSort(fewUniqueData)
endTime = time.time()
print(f"Sort Data: {endTime - startTime} seconds"

# Trials For BubblesSort - randomData

# 1. 68.63684129714966
# 2. 62.10103225708008
# 3. 65.17554926872253

# Trials For BubblesSort - reversedData
# 1. 85.0799789428711
# 2. 96.56564474105835
# 3. 93.78682470321655

# Trials For BubblesSort - nearlySortedData
# 1. 36.2183502746582
# 2. 40.22217345237732
# 3. 43.537169456481934

# Trials For BubblesSort - fewUniqueData
# 1. 40.988357067108154
# 2. 34.968507051467896
# 3. 39.801430463790894

# -------------------------------------------

# Trials For SelectionSort - randomData

# 1. 28.73840022087097
# 2. 32.3431453704834
# 3. 34.096534967422485

# Trials For SelectionSort - reversedData
# 1. 36.32276487350464
# 2. 28.79339337348938
# 3. 28.003393173217773

# Trials For SelectionSort - nearlySortedData
# 1. 28.34013271331787
# 2. 31.681974172592163
# 3. 30.03592538833618

# Trials For SelectionSort - fewUniqueData
# 1. 26.042191743850708
# 2. 23.623611450195312
# 3. 32.10698127746582

# -------------------------------------------

# Trials For InsertionSort - randomData

# 1. 24.127950429916382
# 2. 30.15836477279663
# 3. 33.51371169090271

# Trials For InsertionSort - reversedData
# 1. 58.75995588302612
# 2. 58.41559338569641
# 3. 61.76718807220459

# Trials For InsertionSort - nearlySortedData
# 1. 0.8497111797332764
# 2. 0.9810631275177002
# 3. 0.6878604888916016

# Trials For InsertionSort - fewUniqueData
# 1. 0.7391769886016846
# 2. 0.7868688106536865
# 3. 0.7081477642059326