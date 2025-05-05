
def Max(lst):
    if len(lst)==1:
        return lst[0]
    else:
        remaining_max = Max(lst[1:]
        if lst[0] > remaining_max:
            return lst[0]
        else:
            return remaining_max
