import easygui
import time

AOCDAY = "02"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines







class Computer:
    def __init__(self, programString):
        self.program = [int(number) for number in programString.split(",")]

    def run(self, noun, verb):
        memory = self.program.copy()
        if noun != None:
            memory[1] = noun
        if verb != None:
            memory[2] = verb
        programCounter = 0
        
        while memory[programCounter] != 99:
            if memory[programCounter] == 1:
                memory[memory[programCounter+3]] = memory[memory[programCounter+1]] + memory[memory[programCounter+2]]
                programCounter += 4
            elif memory[programCounter] == 2:
                memory[memory[programCounter+3]] = memory[memory[programCounter+1]] * memory[memory[programCounter+2]]
                programCounter += 4
            else:
                print("Error: Unknown opcode")
                break
        return memory[0]

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    
    computer = Computer(lines[0])

    result = computer.run(12, 2)
    return(f"The value at memory address 0 is {result}!") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    TARGET = 19690720 #all caps b/c it is a constant (convention)

    computer = Computer(lines[0])

    for noun in range(100):
        for verb in range(100):
            if computer.run(noun, verb) == TARGET:
                return(f"The program that produces the desired result is {100*noun+verb}")
    return(f"Didn't find an answer")

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