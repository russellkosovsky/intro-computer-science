#class exercise program for binary search


#recall index() that uses Linear Search algorithm
def index(nums, t):
    #search a list to find index of the value
    #if the value is not found, return -1
    for i in range(len(nums)):
        if nums[i] == t:
            return i
    return -1


#binary search for a sorted list
def binarySearch(nums, t):
    #nums is sorted list

    #base case? when nums is empty
    if nums == []:
        return False
    #recursive case? pick mid index and
    #compare nums[mid] with value
    else:
        mid = len(nums)//2
        ###your code here

        
#binary search verson2: return the index of the given value
#this is warm-up 14. Revise binarysearch to return index
def binarySearch2(nums, low, high, t):

    #base case?
    if nums == []:
        return -1
    #recursive case
    else:
        mid = (high - low) // 2
        ###your code here
        
    #dummy return code (remove this after your implementation)
    return -1



#test your code
print(index([3,1,4,2,5],4))
#print( binarySearch( [1,2,4,5,7,23,34,35,35,48,49], 5) )
#print( binarySearch2( [1,2,4,5,7,23,34,35,35,48,49], 0, 10, 48) )
