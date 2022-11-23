import easygui
import time
import os

AOCDAY = "15"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class RunResult:
    def __init__(self, outputStream, opCode):
        self.outputStream = outputStream
        self.opCode = opCode

class ComputerState:
    def __init__(self, programString):
        self.memory = [int(number) for number in programString.split(",")]
        self.programCounter = 0
        self.offset = 0

    def memCheck(self, address):
        while len(self.memory) <= address:
            self.memory.append(0)

    def run(self,inputStream):
        outputStream = []

        INSTRUCTIONLENGTHS = {
            '1': 4,
            '2': 4,
            '3': 2,
            '4': 2,
            '5': 3,
            '6': 3,
            '7': 4,
            '8': 4,
            '9': 2
        }

        opCode = self.memory[self.programCounter] % 100
        while self.memory[self.programCounter] != 99:

            opCode = self.memory[self.programCounter] % 100
            paramA = self.memory[self.programCounter] % 1000 // 100
            paramB = self.memory[self.programCounter] % 10000 // 1000
            paramC = self.memory[self.programCounter] % 100000 // 10000

            addressA = 0
            if paramA == 0:
                addressA = self.memory[self.programCounter+1]
            elif paramA == 1:
                addressA = self.programCounter+1
            elif paramA == 2:
                addressA = self.memory[self.programCounter+1] + self.offset
            self.memCheck(addressA)

            if(INSTRUCTIONLENGTHS[str(opCode)] >= 3):
                addressB = 0
                if paramB == 0:
                    addressB = self.memory[self.programCounter+2]
                elif paramB == 1:
                    addressB = self.programCounter+2
                elif paramB == 2:
                    addressB = self.memory[self.programCounter+2] + self.offset
                self.memCheck(addressB)

            if(INSTRUCTIONLENGTHS[str(opCode)] >= 4):
                addressC = 0
                if paramC == 0:
                    addressC = self.memory[self.programCounter+3]
                elif paramC == 1:
                    addressC = self.programCounter+3
                elif paramC == 2:
                    addressC = self.memory[self.programCounter+3] + self.offset
                self.memCheck(addressC)

            # print(self.programCounter, opCode, paramA, paramB, paramC, addressA, addressB, addressC)
            # print(self.memory)

            if opCode == 1:
                self.memory[addressC] = self.memory[addressA] + self.memory[addressB]

            elif opCode == 2:
                self.memory[addressC] = self.memory[addressA] * self.memory[addressB]

            elif opCode == 3:
                if len(inputStream) < 1:
                    return RunResult(outputStream,opCode)
                self.memory[addressA] = inputStream.pop(0)

            elif opCode == 4:
                outputStream.append(self.memory[addressA])

            elif opCode == 5:
                if self.memory[addressA] != 0:
                    self.programCounter = self.memory[addressB] - 3

            elif opCode == 6:
                if self.memory[addressA] == 0:
                    self.programCounter = self.memory[addressB] - 3

            elif opCode == 7:
                if self.memory[addressA] < self.memory[addressB]:
                    self.memory[addressC] = 1
                else:
                    self.memory[addressC] = 0

            elif opCode == 8:
                if self.memory[addressA] == self.memory[addressB]:
                    self.memory[addressC] = 1
                else:
                    self.memory[addressC] = 0

            elif opCode == 9:
                self.offset += self.memory[addressA]

            else:
                print("Error: Unknown opcode")
                break

            self.programCounter += INSTRUCTIONLENGTHS[str(opCode)]

        opCode = self.memory[self.programCounter] % 100
        return RunResult(outputStream,opCode)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

def opposite(current_direction):
    if current_direction == 1:
        return 2
    if current_direction == 2:
        return 1
    if current_direction == 3:
        return 4
    if current_direction == 4:
        return 3

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string

    computer = ComputerState(lines[0])

    seen_points = []
    current_path = []
    current_point = Point(0,0)
    current_direction = 1
    moves = [Point(0,0),Point(0,1),Point(0,-1),Point(-1,0),Point(1,0)]
    seen_points = [str(current_point)]
    done = False
    oxygen_location = None
    

    while not done:
        while current_direction < 5:
            moved_point = current_point + moves[current_direction]
            if str(moved_point) not in seen_points:
                result = computer.run([current_direction])
                output = result.outputStream[0]
            else:
                output = 0
            if output != 0:
                current_path.append(current_direction)
                seen_points.append(str(moved_point))
                current_direction = 1
                current_point = moved_point
                if output == 2:
                    oxygen_location = current_point
                    return f"It would take {len(current_path)} moves to get to the oxygen location."
            else:
                current_direction += 1
        computer.run([opposite(current_path[-1])])
        current_point = current_point + moves[opposite(current_path[-1])]
        current_direction = 1
        current_path.pop(-1)
        
        if len(current_path) == 0:
            done = True
#   uncomment to draw map
    # for i in range(-25,26):
    #     line = ""
    #     for j in range(-25,26):
    #         checkpoint = Point(j,i)
    #         if checkpoint == oxygen_location:
    #             line += "o"
    #         elif checkpoint == Point(0,0):
    #             line += "@"
    #         elif str(checkpoint) in seen_points:
    #             line += " "
    #         else:
    #             line += "#"
    #     print(line)


    # print(seen_points)
    return f"Didn't find the oxygen location"


def part2(lines):
    computer = ComputerState(lines[0])

    seen_points = []
    current_path = []
    current_point = Point(0,0)
    current_direction = 1
    moves = [Point(0,0),Point(0,1),Point(0,-1),Point(-1,0),Point(1,0)]
    seen_points = [str(current_point)]
    done = False
    oxygen_location = None
    

    while not done:
        while current_direction < 5:
            moved_point = current_point + moves[current_direction]
            if str(moved_point) not in seen_points:
                result = computer.run([current_direction])
                output = result.outputStream[0]
            else:
                output = 0
            if output != 0:
                current_path.append(current_direction)
                seen_points.append(str(moved_point))
                current_direction = 1
                current_point = moved_point
                if output == 2:
                    oxygen_location = current_point
                    # return f"It would take {len(current_path)} moves to get to the oxygen location."
            else:
                current_direction += 1
        computer.run([opposite(current_path[-1])])
        current_point = current_point + moves[opposite(current_path[-1])]
        current_direction = 1
        current_path.pop(-1)
        
        if len(current_path) == 0:
            done = True
    
    oxygen_queue = [[oxygen_location, 0]]
    oxygenated_points = [str(oxygen_location)]

    while len(oxygenated_points) < len(seen_points):
        current_point,current_mins = oxygen_queue.pop(0)
        for i in range(1,len(moves)):
            next_point = current_point + moves[i]
            if str(next_point) in seen_points:
                if str(next_point) not in oxygenated_points:
                    # print(str(next_point),current_mins+1) # uncomment to see oxygen dispersal
                    oxygenated_points.append(str(next_point))
                    oxygen_queue.append([next_point, current_mins + 1])
  

    # print(seen_points)
    return f"It takes {oxygen_queue[-1][-1]} minutes for the ship to completely fill with oxygen"

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