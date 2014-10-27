from htmlParse import *
import string
#Define all friends and find out when you friended them .
    
# I joined Sunday, January 18, 2009

def defineFriends(wall):
    global friendDict, dateSinceFriend
    with open("friends.txt", "r") as inf:
        friends = inf.readlines()
    
    friendDict = {}
    dateSinceFriend = {}
    
    for friend in friends:
        friendDict[friend.strip("\n")] = 0
        dateSinceFriend[friend.strip("\n")] = 0
        
    ageOfFriendship(dateSinceFriend, friendDict,wall)
    return rateWallPosts(friendDict, dateSinceFriend, wall)
    
    
#Calculates rough distance between two dates as tuples. 
def distanceBetweenDates(start, end):
    return end[0] - start[0] + \
    end[1] * 30 - start[1] * 30 + \
    end[2] * 365 - start[2] * 365 
    
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

def gaugeResponses(friendDict, dateSinceFriend, filtered):
    for item in filtered:
        time = findTime(item[0])
        
        name = findNameExtended(item[1])
        
        if not(name == "%s" % myName):
            try:
                dist = distanceBetweenDates((myDay, myMonth, myYear), (time[0],time[1],time[2]))
                coeff = map(dist, 0, today, 0, 4)
                friendDict[name] = friendDict[name] + (1 * coeff)
            except:
                friendDict[name] = 1 * coeff
                
def findNameExtended(item):
    item = item.strip("</div>")
    lower = string.lowercase
    check = False
    name = ""
    for c in item:
        if c.isspace():
            name += c
            check = True
        elif check and c.islower() and not(c == "d"):
            return name.strip()
        else:
            check = False
            name += c
            
         

def findTimes(dictionary, friendDict, friendList):
    for item in friendList:
        timeFriended = findTime(item[0])
        name = findName(item[1].strip("</div>").strip("</p"))
        
        timeTillFriend = (timeFriended[0] - myDay) + \
                    ((timeFriended[1] * 30) - (myMonth * 30)) + \
                    ((timeFriended[2] * 365) - (myYear * 365))
              
        friendedFor = map(timeTillFriend, 0, today, today, 0)
        
        dictionary[name] = int(friendedFor)
        friendDict[name] = 0
        
def findName(item):
    # Ignore "Luca Damasco and"
    start = 17
    
    #Ignore " are now friends."
    end = len(item) - 17
    
    return item[start:end]

def findTime(item):
            
        day = item[0:3]
        temp = ""
        for c in day:
            temp += c
            
        day = temp
        
        dayLen = abbrToDayLen[day]
            
#         dayI = dayToIndex[abbrToDay[day]]
        
        month = item[dayLen + 1 : dayLen+4]
        
        monI = monthToIndex[abbrToMonth[month]]
        
        monLen = abbrToMonthLen[month]
        
        index = dayLen + monLen
        
        dayI = item[index + 2: index + 4]
        
        
        if dayI[1] == ",":
            dayI = dayI[0]
            
        dayLen = 2
        
        index += 2 + 3
        
        year = item[index : index + 5]   
        
        return (int(dayI), int(monI), int(year)) 
        
def ageOfFriendship(dictionary, friendDict, wall):
    metaList = metaLineFilter(wall) #Only shows meta data on wall. 
    
    filtered = filterLines(metaList,True) #Filters to find only friendings
    
    findTimes(dictionary, friendDict, filtered) #Finds out how long you've been a friend and adds it to the dictionary. 
   
def rateWallPosts(friendDict, dateSinceFriend, wall):
    metaList = metaLineFilter(wall)
    
    filtered = filterLines(metaList, False)
    
    gaugeResponses(friendDict, dateSinceFriend, filtered)
    
    friendListTup = []
    friendList = friendDict.keys()
    
    for name in friendList:
        friendListTup.append((name, friendDict[name]))
        
    finalList = []
    for friend in friendListTup:
        if not(friend[1] == 0):
            finalList.append(friend)

    finalList.sort(key = lambda friend : friend[1])
    
    return finalList
    
def filterLines(lineList, check):
    newList = []
        
    for line in lineList:
        divFree = line.strip('<div class="meta">')
        a = divFree.split(" EST")
        b = divFree.split(" EDT")
        if len(a) >= 2:
            divFree = a
        else: 
            divFree = b
        
        if check:
            if divFree[1][0:22] == "</div>%s and" % myName:
                newList.append(divFree)
        else:
            if not(divFree[1][0:22] == "</div>%s and" % myName) :
                newList.append(divFree)
            
    return newList

def initDefine():
   global today, myName, myMonth, myYear, myDay
   
   myName = "Luca Damasco"
   myMonth = 1
   myDay = 18
   myYear = 2009
   
   today = distanceBetweenDates((myDay, myMonth, myYear), 
                             (day(), month(), year()))

   
initDefine()
            
            
    
            
            
    

            
                



    
    
