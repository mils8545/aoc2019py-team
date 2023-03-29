import easygui
import time
import math


AOCDAY = "22"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines



def part1(lines):
    # Code the solution to part 1 here, returning the answer as a string
    DECKSIZE = 10007
    card_position = 2019
    
    for line in lines:
        parsed = line.split(" ")
        if parsed[0] == "cut":
            card_position = cut(int(parsed[1]),card_position, DECKSIZE)
            # print("Cut: " , str(card_position))
        elif parsed[-1] == "stack":
            card_position = deal_into(card_position, DECKSIZE)
            # print("Stack: " + str(card_position))
        else:
            card_position = deal_with(int(parsed[-1]), card_position, DECKSIZE)
            # print("Increment: " + str(card_position))
    return f'Card 2019 is at position {card_position}.'
    # print(cut(6,4,10))
        
def cut(n, current, decksize):
    return (current - n ) % decksize

def deal_into(current, decksize):
    return (current - decksize + 1) * -1 

def deal_with(inc, current, decksize):
    return (current * inc % decksize)
        
        
        
    
    

    return(f"ANSWER HERE") 

def part2(lines):
    # Code the solution to part 2 here, returning the answer as a string
    DECKSIZE = 119315717514047
    card_position = 2020
    
    SHUFFLE = 101741582076661
    
    
    a = 1
    b = 0
    
    for line in lines:
        parsed = line.split(" ")
        if parsed[0] == "cut":
            a, b = cut_mod(a, b, int(parsed[1]), DECKSIZE)
        elif parsed[-1] == "stack":
            a, b = deal_into_mod(a, b, DECKSIZE)
        else:
            a, b = deal_with_mod(a, b, int(parsed[-1]), DECKSIZE)
    ma = pow(a, SHUFFLE, DECKSIZE)
    mb = (b*(ma-1)*inv(a-1, DECKSIZE)) % DECKSIZE
    return 'The card at position 2020 is ' + str(((card_position-mb)*inv(ma, DECKSIZE)) % DECKSIZE) + '.'

        
        
def cut_mod(a, b, n, m):
    return [a, (b-n) % m]

def deal_into_mod(a, b, m):
    return [-a % m, (-b-1) % m]

def deal_with_mod(a, b, n, m):
    return [(n*a) % m, (n*b) % m]

def power_mod(a, b, k, m):
    return [int(pow(a, k, m)), int(b*(1-pow(a, k, m)/(1-a))) % m ]

def inv(a, n):
    return pow(a, n-2, n)
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