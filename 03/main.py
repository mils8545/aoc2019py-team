import easygui
import time
import math


AOCDAY = "03"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Step:
    def __init__(self,dir,dis):
        self.dir = dir
        self.dis = dis

def parseLines(lines):
    path1 = []
    path2 = []
    for pair in lines[0].split(","):
        path1.append(Step(pair[0],int(pair[1:])))
    for pair in lines[1].split(","):
        path2.append(Step(pair[0],int(pair[1:])))
    return path1, path2

def manhatthanDistance(cross):
    x = abs(int(cross.split(",")[0]))
    y = abs(int(cross.split(",")[1]))
    return x + y


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    path1, path2 = parseLines(lines)
    for step in path1:
        print(step.dir, step.dis)
    for step in path2:
        print(step.dir, step.dis)
    
    path1points = []
    x = 0
    y = 0
    for step in path1:
        if step.dir == "U":
            for i in range(step.dis):
                y += 1
                path1points.append(str(x) + "," + str(y))
        elif step.dir == "D":
            for i in range(step.dis):
                y -= 1
                path1points.append(str(x) + "," + str(y))   
        elif step.dir == "R":
            for i in range(step.dis):
                x += 1
                path1points.append(str(x) + "," + str(y)) 
        elif step.dir == "L":
            for i in range(step.dis):
                x -= 1
                path1points.append(str(x) + "," + str(y))   

    #print(path1points)

    crosspoints = []
    # for point1 in path1points:
    #     if point1 in path2points:
    #         crosspoints.append(point1)
    # print(crosspoints)

    path2points = []
    x = 0
    y = 0
    for step in path2:
        if step.dir == "U":
            for i in range(step.dis):
                y += 1
                path2points.append(str(x) + "," + str(y))
                if path2points[-1] in path1points:
                    crosspoints.append(path2points[-1])
        elif step.dir == "D":
            for i in range(step.dis):
                y -= 1
                path2points.append(str(x) + "," + str(y))  
                if path2points[-1] in path1points:
                    crosspoints.append(path2points[-1])             
        elif step.dir == "R":
            for i in range(step.dis):
                x += 1
                path2points.append(str(x) + "," + str(y)) 
                if path2points[-1] in path1points:
                    crosspoints.append(path2points[-1])
        elif step.dir == "L":
            for i in range(step.dis):
                x -= 1
                path2points.append(str(x) + "," + str(y))   
                if path2points[-1] in path1points:
                    crosspoints.append(path2points[-1])

    #print(path2points)
    


    crosspoints.sort(key=lambda x:manhatthanDistance(x))
    print(crosspoints)



    return(f"The closest intersection point is {manhatthanDistance(crosspoints[0])} away") 

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