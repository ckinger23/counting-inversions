'''
Homework 5: Counting Inversions
Carter King
Dr. Sanders
CS 355 Advanced Algorithms
21 October 2018
Python 3
'''

import sys

'''
Function: SortAndCountInversions(list, length)
 This function uses a variation of MergeSort to simultaneously sort a list of numbers and calculate the number of inversions
 parameters: list - a list of integers to be sorted
             length - the number of items in list
 returns: newList - sorted list of integers
          x + y + z - number of inversions
'''

def SortAndCountInversions(list, length):
    if length < 2: #one item in last, already sorted
        return list, 0
    else:
        firstHalf = list[:len(list) // 2]  #split list in half
        secondHalf = list[len(list) // 2:]

        firstHalfSortedList, x = SortAndCountInversions(firstHalf, len(firstHalf)) #recursive call on each half
        secondHalfSortedList, y = SortAndCountInversions(secondHalf, len(secondHalf))
        counter = 0
        newList, z = SortAndCountInversionsAux(firstHalfSortedList,secondHalfSortedList, counter)


        return newList, x + y + z #return sorted list and number of inversions


'''
Function: SortAndCountInversionsAux(listA, listB, count)
 This function is a helper function to the SortAndCountInversions function in 
 order to reassemble the split lists into sorted order and count the number of inversions
 while doing so
 parameters: 
    listA - A list of integers to be compared to listB
    listB - A list of integers to be compared to listA
    count - a counter keeping tally of the number of inversions
 returns: sortedList - A single list of the sorted integers
          counter - current number of inversions
'''

def SortAndCountInversionsAux(listA, listB, count):

    sortedList = []
    counter = count

    while(len(listA) != 0 and len(listB) != 0): #while elements still available to compare
        if listA[0] > listB[0]: #sorting entrance into sortedList
            sortedList.append(listB[0])
            for elements in listA:
                counter += 1 #Inversion since item from listB sorted before item in listA
            del listB[0]
        else:
            sortedList.append(listA[0])
            del listA[0]

    while (len(listA) != 0): #if anything left in the passed lists, append to sortedList
        sortedList.append(listA[0])
        del listA[0]

    while (len(listB) != 0):
        sortedList.append(listB[0])
        del listB[0]

    return sortedList, counter


'''
Function: parseFile(filename)
 This function takes a .txt file of integers and appends them to a list  
 parameters: filename - a string of the name of the file 
 returns: list - a list of integers from the file
'''

def parseFile(filename):
    list = []
    infile = open(filename, 'r') #read the file and add elements to list
    for line in infile:
        value = int(line)
        list.append(value)
    return list


def main():
    # Show them the default len is 1 unless they put values on the command line
    print(len(sys.argv))
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
    else:
        fileName = input("What .txt file would you like to use? ")
        list = parseFile(fileName)
        sortedList, numInversions = SortAndCountInversions(list, len(list))
        print("There are", numInversions, "number of inversions in this list. ")


main()