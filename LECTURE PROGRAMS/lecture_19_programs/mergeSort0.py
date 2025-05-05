# exercise for merge sort

from random import *

# helper function to merge two sorted listed to new list
def merge(lst1, lst2, lst3):
    # merge sorted lists lst1 and lst2 into lst3
    # these indexes keep track of current position in each list
    
    i1 = 0 # index for list 1
    i2 = 0 # index for list 2
    i3 = 0 # index for mergedList
    n1 = len(lst1)
    n2 = len(lst2)

    # while we still have more values in both lists to look at
    while i1 < n1 and i2 < n2:
        # if the next value in list 1 is smaller than the next value in list 2
        if lst1[i1] < lst2[i2]:
            # add the value from list 1 to the mergedList
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        # otherwise add the value from list2 to the mergedList
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1  # item added to lst3

    # while any items remain in list 1, 
    while i1 < len(lst1):
        # add them to end of mergedList
        # Copy remaining items (if any) from lst1
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1

    # while any items remain in list 2
    while i2 < len(lst2):
        # add them to end of mergedList
        # Copy remaining items (if any) from lst2
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

# merge sort
def mergeSort(nums):

    # length of the list
    n = len(nums)
    
    # recursive case... a list has more than one item (not empty)
    if n > 1:
        # split list in half
        mid = n//2
        numList1 = nums[0:mid]
        numList2 = nums[mid:n]

        # merge sort both halves
        mergeSort(numList1)
        mergeSort(numList2)

        # merge both sorted halves into one sorted list
        merge(numList1, numList2, nums)
        
    # base case:  do nothing when n == 1
    if n == 1:
        None 

#testerrr
def main():
    # test merge()
    nums1 = [4,6,7,10,40]
    nums2 = [1,4,67,90,100,123,235]
    nums = [0,0,0,0,0,0,0,0,0,0,0,0]
    merge(nums1,nums2,nums)
    print("========================================== TEST: merge() =========================================")
    print("list 1:", nums1)
    print("list 2:", nums2)
    print()
    print("merged list:", nums)
    print()

    # test mergeSort()
    nums = []
    # populate some random numbers for the list
    for i in range(15):
        nums.append(randrange(100))

    print("========================================== TEST: mergeSort() =========================================")
    print("original list:", nums)
    mergeSort(nums)
    print()
    print("sorted list:", nums)
    
main()
