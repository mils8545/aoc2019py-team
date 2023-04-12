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
        
def outerCount(generation2D):
    top_count = 0
    bottom_count = 0
    right_count = 0
    left_count = 0
    for i in range(5):
        if generation2D [0][i] == '#':
            top_count += 1
        if generation2D [-1][i] == '#':
            bottom_count += 1
        if generation2D [i][0] == '#':
            left_count += 1
        if generation2D [i][-1] == '#':
            right_count += 1
    return [top_count,bottom_count,left_count,right_count]

def innerCount(generation2D):
    top_count = 0
    bottom_count = 0
    right_count = 0
    left_count = 0
    
    if generation2D [1][2] == '#':
        top_count += 1
    if generation2D [3][2] == '#':
        bottom_count += 1
    if generation2D [2][1] == '#':
        left_count += 1
    if generation2D [2][3] == '#':
        right_count += 1
    return [top_count,bottom_count,left_count,right_count]

def nextGeneration3D(generation3D):
    next = []
    next.append([[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]])
    top_count,bottom_count,left_count,right_count = outerCount(generation3D[0])
    if top_count == 1 or top_count == 2:
        next[0][1][2] = '#'
    if bottom_count == 1 or bottom_count == 2:
        next[0][3][2] = '#'
    if left_count == 1 or left_count == 2:
        next[0][2][1] = '#'
    if right_count == 1 or right_count == 2:
        next[0][2][3] = '#'
    for z in range(len(generation3D)):
        newPlane = []
        if z > 0:
            top_count,bottom_count,left_count,right_count = innerCount(generation3D[z-1])
        else:
            top_count = 0
            bottom_count = 0
            left_count = 0
            right_count = 0
        if z < len(generation3D)-1:
            innertop_count,innerbottom_count,innerleft_count,innerright_count = outerCount(generation3D[z+1])
        else:
            innertop_count = 0
            innerbottom_count = 0
            innerleft_count = 0
            innerright_count = 0
        for y in range(len(generation3D[z])):
            newLine = []
            for x in range(len(generation3D[z][0])):
                neighbours = 0
                if y > 0 and generation3D[z][y-1][x] == "#":
                    neighbours += 1
                if y == 0:
                    neighbours += top_count
                if y < len(generation3D[z]) - 1 and generation3D[z][y+1][x] == "#":
                    neighbours += 1
                if y == 4: 
                    neighbours += bottom_count
                if x > 0 and generation3D[z][y][x-1] == "#":
                    neighbours += 1
                if x == 0:
                    neighbours += left_count
                if x < len(generation3D[z][0]) - 1 and generation3D[z][y][x+1] == "#":
                    neighbours += 1
                if x == 4:
                    neighbours += right_count
                if y == 1 and x == 2:
                    neighbours += innertop_count
                if y == 3 and x == 2:
                    neighbours += innerbottom_count
                if y == 2 and x == 1:
                    neighbours += innerleft_count
                if y == 2 and x == 3:
                    neighbours += innerright_count
                if y == 2 and x == 2:
                    neighbours = 10

                if generation3D[z][y][x] == "#":
                    if neighbours == 1:
                        newLine.append("#")
                    else:
                        newLine.append(".")
                else:
                    if neighbours == 1 or neighbours == 2:
                        newLine.append("#")
                    else:
                        newLine.append(".")
            newPlane.append(newLine)
        next.append(newPlane)
    next.append([[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]])
    innertop_count,innerbottom_count,innerleft_count,innerright_count = innerCount(generation3D[-1])
    if innertop_count == 1:
        for i in range(5):
            next[-1][0][i] = "#"
    if innerbottom_count == 1:
        for i in range(5):
            next[-1][-1][i] = "#"
    if innerleft_count == 1:
        for i in range(5):
            next[-1][i][0] = "#"
    if innerright_count == 1:
        for i in range(5):
            next[-1][i][-1] = "#"

    return next


def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    eris = [[]]
    for line in lines:
        newLine = []
        for spot in line:
            newLine.append(spot)
        eris[0].append(newLine)
    for i in range(200):
        eris = nextGeneration3D(eris)
    print(eris)
    count = 0
    for z in range(len(eris)):
        for y in range(5):
            for x in range(5):
                if eris[z][y][x] == "#":
                    count += 1
    print(count)

    
   

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