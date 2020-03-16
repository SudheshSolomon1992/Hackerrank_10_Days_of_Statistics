#!/bin/python3

def calculateWeightedMean(length, array_A, array_B):
    numerator = 0
    denominator = 0
    
    for i in range(length):
        numerator = numerator + array_A[i] * array_B[i]
        denominator = denominator + array_B[i]

    return numerator / denominator

def main():
    length = int(input())
    array_A = [int(element) for element in input().strip().split(' ')[:length]]
    array_B = [int(element) for element in input().strip().split(' ')[:length]]
    weightedMean = calculateWeightedMean(length, array_A, array_B)
    print ("{:.1f}".format(weightedMean))

if __name__ == "__main__":
    main()
