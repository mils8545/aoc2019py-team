import easygui
import time
import math


AOCDAY = "16"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def performPhase(signal):

    base = (0, 1, 0, -1)

    output_signal = []

    for i in range(len(signal)):

        signal_total = 0

        for j, num in enumerate(signal):

            signal_total += num * base[( (j+1)//(i+1) ) % 4 ]

        output_signal.append(abs(signal_total)%10)

    return output_signal

def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    signal = [int(num) for num in lines[0]]

    for i in range(100):
        signal = performPhase(signal)

    answer = ''.join([str(num) for num in signal[0:8]])

    return(f"first 8 digits are {answer}") 

def shortcutPhase(signal):

    output_signal = []

    running_total = 0
    for num in signal:
        running_total += num
        output_signal.append(running_total%10)
        
    return output_signal


def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    
    signal = [int(num) for num in lines[0]]
    message_offset = int(''.join([str(num) for num in signal[0:7]]))

    repeated_signal = []
    
    for i in range(10000*len(signal) - message_offset):
        repeated_signal.append(signal[-((i+1)%len(signal))])

    for i in range(100):
        repeated_signal = shortcutPhase(repeated_signal)

    message = repeated_signal[-8:]
    message.reverse()

    answer = ''.join([str(num) for num in message])

    return f"The eight-digit message is {answer}"

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