import easygui
import time
import math


AOCDAY = "24"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def bioDiversity(generation):
    value = 1
    score = 0
    for y in range(len(generation)):
        for x in range(len(generation[0])):
            if generation[y][x] == "#":
                score += value
            value *= 2
    return score

def nextGeneration(generation):
    next = []
    for y in range(len(generation)):
        newLine = []
        for x in range(len(generation[0])):
            neighbours = 0
            if y > 0 and generation[y-1][x] == "#":
                neighbours += 1
            if y < len(generation) - 1 and generation[y+1][x] == "#":
                neighbours += 1
            if x > 0 and generation[y][x-1] == "#":
                neighbours += 1
            if x < len(generation[0]) - 1 and generation[y][x+1] == "#":
                neighbours += 1
            if generation[y][x] == "#":
                if neighbours == 1:
                    newLine.append("#")
                else:
                    newLine.append(".")
            else:
                if neighbours == 1 or neighbours == 2:
                    newLine.append("#")
                else:
                    newLine.append(".")
        next.append(newLine)
    return next

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    eris = []
    for line in lines:
        newLine = []
        for spot in line:
            newLine.append(spot)
        eris.append(newLine)
    seen = [bioDiversity(eris)]
    while True:
        eris = nextGeneration(eris)
        score = bioDiversity(eris)
        if score in seen:
            # # Uncomment next 3 lines to print out last generation.
            # print("-----")
            # for line in eris:
            #     print("".join(line))
            return score
        else:
            seen.append(score)
        # # Uncomment next 3 lines to print out generations.
        # print("-----")
        # for line in eris:
        #     print("".join(line))
        

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    pass

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