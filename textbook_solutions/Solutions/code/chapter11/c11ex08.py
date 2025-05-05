# c11ex08.py
#    Function to remove duplicates

def removeDuplicates1(lst):
    # empty lst and create lst2 w/o duplicates
    lst2 = []
    while lst != []:
        item = lst.pop(0)
        if item not in  lst2:
            lst2.append(item)

    # put contents of lst2 into lst
    lst.extend(lst2)


def removeDuplicates2(lst):
    # This version uses a dictionary for better performance
    set = {}
    while lst != []:
        set[lst.pop()] = True
    # lst is now empty, fill with keys from set
    lst.extend(list(set.keys()))

