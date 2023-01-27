import easygui
import time
import math


AOCDAY = "18"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
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

    startX = 0
    startY = 0
    keys = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                startX = x
                startY = y
            if map[y][x] >= "a" and map[y][x] <= "z":
                keys.append(map[y][x])


    moves = [[0,1],[0,-1],[1,0],[-1,0]]

    visited = {}
    queue = [[startY,startX,"",0]]


    counter = 0
    while True:
        current = queue.pop(0)
        y = current[0]
        x = current[1]
        keysHeld = current[2]
        moves_made = current[3]
        if len(keysHeld) == len(keys):
            return moves_made
        counter += 1
        if counter %10000 == 0:
            print(counter,y,x,keysHeld,moves_made)
        visited[f"{x},{y},"+keysHeld] = 0
        # need to account for count of moves
        for move in moves:
            next = map[y+move[1]][x+move[0]]
            newX = x+move[0]
            newY = y+move[1]
            if next != "#":
                if not(next  >= "A" and next <= "Z" and (next.lower() not in keysHeld)):
                    # movestring = f"{x},{y},"+"".join(keysHeld)
                    newkey = ""
                    if next >= "a" and next <= "z" and (next not in keysHeld):
                        newkey = next
                    target = f"{newX},{newY},"+''.join(sorted(keysHeld+newkey))
                    if target not in visited:
                        queue.append([newY,newX,''.join(sorted(keysHeld+newkey)),moves_made+1])









    


        
    

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