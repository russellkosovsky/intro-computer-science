#class exercise program: sorting

def selectionSort(nums):

    n = len(nums)

    #for each slot in the list
    for slot in range(n):

        #find the index of the smallest value among all remaining numbers
        indexOfMin = slot #start by assuming the current one is smallest

        #go through all numbers starting from the one in the current slot
        for i in range(slot,n):

            #if we find one that's smaller, record that one (index) instead
            for i in range(slot + 1,n):
                if nums[i] < nums[indexOfMin]:
                    indexOfMin = i

        #swap value in "slot" with value in "indexOfMin"
        nums[slot], nums[indexOfMin] = nums[indexOfMin], nums[slot]

def main():

    numbers = [5,2,3,6,7,2,34,5,12,432]
    selectionSort(numbers)

##    words = ["hello", "goodbye", "farewell", "greetings", "cheers", "until next time"]
##    selectionSort(words)

    print(numbers)
##    print(words)

main()
