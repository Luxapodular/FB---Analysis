from htmlParse import *
#Define all friends and find out when you friended them .



    
monthToIndex = {
                "January" : 1,
                "February" : 2,
                "March" : 3,
                "April" : 4,
                "May" : 5, 
                "June" : 6, 
                "July" : 7,
                "August" : 8, 
                "September" : 9,
                "October" : 10,
                "November" : 11,
                "December" : 12
                }

dayToIndex = {
              "Sunday" : 1,
              "Monday" : 2,
              "Tuesday" : 3,
              "Wednesday" : 4,
              "Thursday" : 5, 
              "Friday" : 6,
              "Saturday" : 7
              }

abbrToMonth = {
               "Jan" : "January",
               "Feb" : "February",
               "Mar" : "March",
               "Apr" : "April",
               "May" : "May",
               "Jun" : "June",
               "Jul" : "July",
               "Aug" : "August",
               "Sep" : "September", 
               "Oct" : "October", 
               "Nov" : "November",
               "Dec" : "December"
               }

abbrToMonthLen = {
               "Jan" : 7,
               "Feb" : 8,
               "Mar" : 5,
               "Apr" : 5,
               "May" : 3,
               "Jun" : 4,
               "Jul" : 4,
               "Aug" : 6,
               "Sep" : 9, 
               "Oct" : 7, 
               "Nov" : 8,
               "Dec" : 8
               }

abbrToDay = {
             "Mon" : "Monday",
             "Tue" : "Tuesday",
             "Wed" : "Wednesday",
             "Thu" : "Thurday",
             "Fri" : "Friday",
             "Sat" : "Saturday",
             "Sun" : "Sunday"
             }

abbrToDayLen = {
             "Mon" : 7,
             "Tue" : 8,
             "Wed" : 10,
             "Thu" : 9,
             "Fri" : 7,
             "Sat" : 9,
             "Sun" : 7
             }

days = dayToIndex.keys()
months = monthToIndex.keys()

def dayOfWeek():
    # 5 is number of days into 2014 for sunday
    daystotal = (365*(year() - 1)) + (int(floor((year()-1)/4))) -(int(floor((year() - 1)/100))) + (int(floor((year() - 1)/400))) + day()
    return daystotal % 7

def metaLineFilter(wall):
    metaList = []
    for line in wall:
        temp = ""
        for c in line:
            temp = temp + c
            if temp == '<div class="meta">':
                metaList.append(line)
                
    return metaList    

def filterLines(lineList):
    newList = []
    
    for line in lineList:
        divFree = line.strip('<div class="meta">')
        a = divFree.split(" EST")
        b = divFree.split(" EDT")
        if len(a) >= 2:
            divFree = a
        else: 
            divFree = b
        
        if divFree[1][0:22] == "</div>Luca Damasco and":
            newList.append(divFree)
            
    return newList

def findTimes(dictionary, friendList):
    global abbrToMonth, monthToIndex, abbrToDay, abbrToDayLen, abbrToMonthLen

      
    for item in friendList:
        
        day = item[0][0:3]
        temp = ""
        for c in day:
            temp += c
            
        day = temp
        
        dayLen = abbrToDayLen[day]
            
#         dayI = dayToIndex[abbrToDay[day]]
        
        month = item[0][dayLen + 1 : dayLen+4]
        
        monI = monthToIndex[abbrToMonth[month]]
        
        monLen = abbrToMonthLen[month]
        
        index = dayLen + monLen
        
        dayI = item[0][index + 2: index + 4]
        
        
        if dayI[1] == ",":
            dayI = dayI[0]
            
        dayLen = 2
        
        index += 2 + 3
        
        year = item[0][index : index + 5]
        
        print item[1]
        
        
        
        
            
        
        
            
            
def defineFriends(wall):
    global friendDict, dateSinceFriend
    with open("friends.txt", "r") as inf:
        friends = inf.readlines()
    
    friendDict = {}
    dateSinceFriend = {}
    
    for friend in friends:
        friendDict[friend.strip("\n")] = 0
        dateSinceFriend[friend.strip("\n")] = 0
        
    ageOfFriendship(dateSinceFriend,wall)
    
        
def ageOfFriendship(dictionary,wall):
    metaList = metaLineFilter(wall)
    filtered = filterLines(metaList)
    findTimes(dictionary, filtered)
            
            
            
    

            
                



    
    
