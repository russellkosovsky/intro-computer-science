#class exercise for merge sort

from random import *

#helper function to merge two sorted listed to new list
def merge(list1, list2, mergedList):

    i1 = 0 #index for list 1
    i2 = 0 #index for list 2
    j = 0  #index for mergedList

    #while we still have more values in both lists to look at
    while i1 < len(list1) and i2 < len(list2):
        #if the next value in list 1 is smaller than the next value in list 2
        if list1[i1] < list2[i2]:
            #add the value from list 1 to the mergedList
            mergedList[j] = list1[i1]
            i1 += 1 
        else:
            #otherwise add the value from list2 to the mergedList
            mergedList[j] = list2[i2]
            i2 += 1
        j += 1 #increment index for mergedList

    #while any items remain in list 1, 
    while i1 < len(list1):
        #add them to end of mergedList
        mergedList[j] = list1[i1]
        i1 += 1
        j += 1

    #while any items remain in list 2
    while i2 < len(list2):
        #add them to end of mergedList
        mergedList[j] = list2[i2]
        i2 += 1
        j += 1

#simpler version (if we can remove items from list1, list2)
def merge1(list1, list2, mergedList):
    pos = 0
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            mergedList[pos] = list1.pop(0)
        else:
            mergedList[pos] = list2.pop(0)
        pos += 1

    while len(list1):
        mergedList[pos] = list1.pop(0)
        pos += 1

    while len(list2):
        mergedList[pos] = list2.pop(0)
        pos += 1
        
#merge sort
def mergeSort(nums):

    n = len(nums)
    if n > 1: #recursive case
        #split list in half
        mid = n//2
        numList1 = nums[0:mid]
        numList2 = nums[mid:n]

        #merge sort both halves
        mergeSort(numList1)
        mergeSort(numList2)

        #merge both sorted halves into one sorted list
        merge(numList1, numList2, nums)

    #base case is implicit:  do nothing when n == 1


#test driver
def main():
    #just test merge() helper function first
    nums1 = [4,6,7,10,40]
    nums2 = [1,4,67,90,100,123,235]
    nums = [0,0,0,0,0,0,0,0,0,0,0,0]
    merge(nums1,nums2,nums)
    print("merge() functino test =====================")
    print("list 1:", nums1)
    print("list 2:", nums2)
    print("merged list:", nums)
    print("\n\n")

    #mergeSort test
    nums = []
    #populate some random numbers for the list
    for i in range(15):
        nums.append(randrange(100))
    print("original list:", nums)
    mergeSort(nums)
    print("sorted list:", nums)
    
main()
