import easygui
import time
import os

AOCDAY = "21"

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

def string2int(input_string):
    integers = []
    for char in input_string:
        integers.append(ord(char))
    return integers


def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string

   
    computer = ComputerState(lines[0])
    result = computer.run([]) 
    for char in result.outputStream:
        print(chr(char), end = '')  
    
    program = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n"
    
    result = computer.run(string2int(program)) 
    for char in result.outputStream:
        if char < 128 :
            print(chr(char), end = '')  
        else:
            return(f'The score of the robot was: {char}')

    return f"Done."


def part2(lines):
    computer = ComputerState(lines[0])
    result = computer.run([]) 
    for char in result.outputStream:
        print(chr(char), end = '')  
    
    program = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT A T\nAND A T\nOR E T\nOR H T\nAND T J\nRUN\n"
    
    result = computer.run(string2int(program)) 
    for char in result.outputStream:
        if char < 128 :
            print(chr(char), end = '')  
        else:
            return(f'The score of the robot was: {char}')

    return f"Done."

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