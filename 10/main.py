import easygui
import time
from math import atan2, degrees


AOCDAY = "10"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def slopeTo(self,other):
        if (other.x - self.x) == 0:
            return 99999
        return ((other.y - self.y)/(other.x - self.x))
    def angleTo(self, other): 
        angle = atan2(other.y - self.y, other.x - self.x)
        angle = degrees(angle)
        return angle


def parseLines(lines):
    points = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                points.append(Point(x,y))

    return points



def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    asteroids = parseLines(lines)
    counts = []
    for j in range(len(asteroids)):
        asteroid = asteroids[j]
        lineOfSight = []
        for i,target in enumerate(asteroids):
            if i != j:
                lineOfSight.append(f"{asteroid.slopeTo(target)},{asteroid.angleTo(target)}")
        counts.append(len(list(set(lineOfSight))))
    return(f"The best position sees {max(counts)} asteroids.") 

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