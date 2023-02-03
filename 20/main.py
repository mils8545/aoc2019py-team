import easygui
import time
import math


AOCDAY = "20"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    return lines



def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    map = []

    for line in lines:
        row = []
        for symbol in line:
            row.append(symbol)
        map.append(row)
        # print(map[-1])
    portals = {}
    for y in range(1,len(map)-1):
        for x in range(1,len(map[0])-1):
            print(y,x)
            if map[y][x] >= "A" and map[y][x] <= "Z":
                if map[y-1][x] == ".":
                    portalname = map[y][x] + map[y+1][x]
                    if portalname not in portals:
                        portals[portalname] = [[y-1,x]]
                    else:
                        portals[portalname].append([y-1,x])
                if map[y+1][x] == ".":
                    portalname = map[y-1][x] + map[y][x]
                    if portalname not in portals:
                        portals[portalname] = [[y+1,x]]
                    else:
                        portals[portalname].append([y+1,x])
                if map[y][x+1] == ".":
                    portalname = map[y][x-1] + map[y][x]
                    if portalname not in portals:
                        portals[portalname] = [[y,x+1]]
                    else:
                        portals[portalname].append([y,x+1])
                if map[y][x-1] == ".":
                    portalname = map[y][x] + map[y][x+1]
                    if portalname not in portals:
                        portals[portalname] = [[y,x-1]]
                    else:
                        portals[portalname].append([y,x-1])    
    for portal in portals:
        print(portal,portals[portal])


   
    

    return(f"ANSWER HERE") 

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