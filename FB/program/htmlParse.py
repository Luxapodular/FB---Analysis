def parseWall():
    newList = []
    complete = []
    
    with open("wall.htm", "r") as inf:
        wall = inf.readlines()
    
    for item in wall:
        wallEdit = item.split('<p>')
        newList.append(wallEdit)

    for item in newList:
        for line in item:
            complete.append(line)
        
    return complete


