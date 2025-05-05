

# [2 25pts] Given a string, compute recursively a new string where 
# identical chars that are adjacent in the original string are 
# separated from each other by a "*".
#     pairStar("hello") → "hel*lo"
#     pairStar("xxyy") → "x*xy*y"
#     pairStar("aaaa") → "a*a*a*a" 

def pairStar(s):
    if len(s) <= 1:
        return s
    
    if s[0] == s[1]:
        return s[0] + "*" + pairStar(s[1:])
    else:
        return s[0] + pairStar(s[1:])


print(pairStar("hello"))


def stringClean(s):
    if len(s) <= 1:
        return s
    
    # if the first character and the second character are the same
    if s[0] == s[1]:
        return stringClean(s[1:])
    else:
        return s[0] + stringClean(s[1:])

print(stringClean("yyzzza"))   
print(stringClean("abbbcdd"))  
print(stringClean("Hello"))    


def endX(s):
    if len(s) <= 1:
        return s
    
    # if the first character is 'x'
    if s[0] == 'x':
        return endX(s[1:]) + 'x'
    else:
        return s[0] + endX(s[1:])

print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))
