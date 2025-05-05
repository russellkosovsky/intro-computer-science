# c06ex12.py
#    function to sum numbers in a list

def sumList(nums):
    total = 0
    for n in nums:
        total = total + n
    return total

def test():
    nums = list(range(10))
    print(sumList(nums))

test()
