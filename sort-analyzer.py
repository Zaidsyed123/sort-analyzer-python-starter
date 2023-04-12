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
print(f"Sort Data: {endTime - startTime} seconds")
