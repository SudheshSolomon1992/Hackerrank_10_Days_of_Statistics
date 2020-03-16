#!/bin/python3

def calculateMean(array):
    sum = 0
    for element in array:
        sum = sum + int(element)
    
    mean = sum / len(array)
    return mean

def calculateMedian(array):
    length = len(array)
    array.sort()
    temp = []
    
    if length % 2 == 0:
        temp.append(array[int(length/2)])
        temp.append(array[(int(length/2)) - 1])
        median = calculateMean(temp)

    else:
        median = array[int(length/2)]
    
    return median

def calculateMode(array):
    temp = {}
    maximum = 0

    for element in array:
        temp[element] = array.count(element)

    for key, value in temp.items():
        if value > maximum:
            maximum = value
    
    for key, value in temp.items():
        if value == maximum:
            return key

def main():
    number_of_inputs = int(input())
    array = [int(element) for element in input().strip().split(' ')[:number_of_inputs]]
    mean = calculateMean(array)
    median = calculateMedian(array)
    mode = calculateMode(array)
    print ("{:.1f}".format(mean))
    print ("{:.1f}".format(median))
    print ("{:.1f}".format(mode))

if __name__ == "__main__":
    main()
