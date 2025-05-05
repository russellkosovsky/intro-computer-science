#print out gamers ranking based on scores


def getScore(nameScore):

    #implement key function for sorting
    #need to return score as we want to sort players by score
    return nameScore[1]

def rankPlayers():
    
    #player list consists of tuples (name, score)
    players = [("zoe", 30), ("ben", 24), ("haley", 52), ("tim", 234)]

    

    #implement sorting here

    players.sort(key = getScore, reverse = True)
    
    print(players)

    #use key function to sort players based on score


rankPlayers()
