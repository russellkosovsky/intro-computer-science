# c06ex13.py
#    function to convert list of strings to numbers

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def test():
    x = ["12", "345", "15.34"]
    toNumbers(x)
    print(x)

test()
