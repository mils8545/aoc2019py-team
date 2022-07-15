import easygui
import time
import math


AOCDAY = "01"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def fuelCalc(mass):
    if (math.floor((mass)/3)-2) <0:
        return 0
    else:
        return math.floor((mass)/3)-2

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    totalFuel = 0
    for line in lines:
        # totalFuel += math.floor(int(line)/3)-2
        totalFuel += fuelCalc(int(line))

    #return("You require a fuel amount of "+str(totalFuel)+".")
    return(f"You require a fuel amount of {(totalFuel)}.")

def part2(lines):
    # Code the solution to part 1 here, returning the answer as a string
    totalFuel = 0
    for line in lines:
        calcedFuel = fuelCalc(int(line))
        while calcedFuel > 0:
            totalFuel = totalFuel + calcedFuel
            calcedFuel = fuelCalc(calcedFuel)
    return(f"You require a new fuel amount of {(totalFuel)}.")

def main ():
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
        return
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2019 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()