import easygui
import time
import math


AOCDAY = "08"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines



def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    WIDTH = 25
    HEIGHT = 6
    DEPTH = len(lines[0])//(WIDTH*HEIGHT)

    img = [[[0 for i in range(WIDTH)] for j in range(HEIGHT)] for k in range(DEPTH)]
    # for i,pixel in enumerate(lines[0]):
    #     img[i//DEPTH][i%DEPTH//HEIGHT][i%HEIGHT//WIDTH] = int(pixel)
    for i in range(len(lines[0])):
        img[i//(WIDTH*HEIGHT)][(i%(WIDTH*HEIGHT))//WIDTH][(i%WIDTH)] = int(lines[0][i])
    fewest0 = 150000
    fewest1 = 0
    fewest2 = 0

    for layer in img:
        flat = [pixel for line in layer for pixel in line]
        count0 = flat.count(0)
        if count0 < fewest0:
            fewest0 = count0
            fewest1 = flat.count(1)
            fewest2 = flat.count(2)

    return(f"the product of 1s and 2s in the layer with the least 0s is {fewest1*fewest2}") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    WIDTH = 25
    HEIGHT = 6
    DEPTH = len(lines[0])//(WIDTH*HEIGHT)

    img = [[[0 for i in range(WIDTH)] for j in range(HEIGHT)] for k in range(DEPTH)]
    # for i,pixel in enumerate(lines[0]):
    #     img[i//DEPTH][i%DEPTH//HEIGHT][i%HEIGHT//WIDTH] = int(pixel)
    for i in range(len(lines[0])):
        img[i//(WIDTH*HEIGHT)][(i%(WIDTH*HEIGHT))//WIDTH][(i%WIDTH)] = int(lines[0][i])
    fewest0 = 150000
    fewest1 = 0
    finalimg = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            layer = 0
            while img[layer][y][x] == 2:
                layer += 1
            finalimg[y][x] = img[layer][y][x]
    for row in finalimg:
        something = ""
        for pixel in row:
            if pixel == 1:
                something = something + "@"
            else:
                something = something + " "
        print(something)
    
    return "Read text above"

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