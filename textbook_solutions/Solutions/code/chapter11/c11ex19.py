# c11ex19.py
#    Implementation of sets
#    Note: Python has a built-in set type, so implementing this is just
#          an interesting programming exercise.

# using dictionaries---efficient, but objects in set must be immutable

class DictSet:

    def __init__(self, elements):
        self.elements = {}
        for e in elements:
            self.elements[e] = True # actual assigned value irrelevant

    def addElement(self, x):
        self.elements[x] = True

    def deleteElement(self, x):
        if x in self.elements:
            del self.elements[x]

    def member(self, x):
        return x in self.elements

    def intersection(self, set2):
        inter = []
        for x in self.elements:
            if x in set2.elements:
                inter.append(x)
        return DictSet(inter)

    def union(self, set2):
        return DictSet(list(self.elements.keys()) + list(set2.elements.keys()))

    def subtract(self, set2):
        els = []
        for x in self.elements:
            if x not in set2.elements:
                els.append(x)
        return DictSet(els)

    def __str__(self):
        return "<Set: {0}>".format(list(self.elements.keys()))

# Using lists, less efficient but more general

class ListSet:

    def __init__(self, elements):
        els = []
        for x in elements:
            if x not in els:
                els.append(x)
        self.elements = els

    def addElement(self, x):
        if x not in self.elements:
            self.elements.append(x)

    def deleteElement(self, x):
        try:
            self.elements.remove(x)
        except:
            pass

    def member(self, x):
        return x in self.elements

    def intersection(self, set2):
        els = []
        for x in self.elements:
            if x in set2.elements:
                els.append(x)
        return ListSet(els)

    def union(self,set2):
        return ListSet(self.elements + set2.elements)

    def subtract(self, set2):
        els = []
        for x in self.elements:
            if x not in set2.elements:
                els.append(x)
        return ListSet(els)

    def __str__(self):
        return "<Set: {0}>".format(self.elements)



def test():
    for SetClass in [DictSet, ListSet]:
        all = SetClass([1,2,3,4,5,6,7,8,9,10])
        odds = SetClass([1,3,5,7,9])
        evens = SetClass([2,4,6,8,10])
        print("all", odds.union(evens))
        print("all", evens.union(odds))
        print("empty", odds.intersection(evens))
        print("odds", all.intersection(odds))
        print("odds", all.subtract(evens))
        
if __name__ == '__main__':
    test()
