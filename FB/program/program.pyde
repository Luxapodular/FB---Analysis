from defineFriends import *
from htmlParse import *
wall = parseWall()

list = defineFriends(wall)

tenLeast = []

nFriends = 10

for i in range(nFriends):
    tenLeast.append(list[i][0])
    
print tenLeast

def setup():
    size(1000,800)
    textAlign(CENTER)
    background(0x3b5998)
    textSize(50)
    a = loadFont("LucidaGrande-48.vlw")
    textFont(a)
    text("Social Strangers", width / 2, height * .1)
    for i in range(nFriends):
        xLoc = ((i % 2) * width * .5 ) + width * .25
        yLoc = height * (.15 * (i % 5)) + height * .25
        print xLoc, yLoc
        textSize(30 + i)
        text(tenLeast[i], xLoc, yLoc)



"""
##########################################
#Define Weight of each online interaction#
##########################################

#Categories could be narrowed and different types of interactions 
#could receive different weights ex. a post which is a question could 
#receive more points thana  post that is a statement. 

#From Them - People interacting with me
hbd = -1 #A Wall Post saying hbd. 
happyBirthday = .5 #A wall pos saying happy birthday
wallPost = 1 #Any other post to your wall. 
theyLike = 1 #They like a post on my wall. 
theyComment = 2 #They comment on a post on my wall
theyPoke = .5 #They poke me.
theyTag = 2 #They tag me in something.  

#From Me - Me interacting with others 
iHbd = -1 #I post hbd on their wall. 
iHappyBirthday = 1 #I post happy birthday on their wall. 
iWallPost = 2 #I post something on their wall. 
iLike = 2 #I like something they have posted. 
iComment = 3 #I comment on a post of theirs. 
iPoke = 1 #I poke them 
iTag = 2 #I tag someone in a post. 

#Together
relationship = 100 #Previously been in a relationship with
familyMember = 100 #Person is listed as a family member with you. 
taggedWith = 10 #Tagged with them in a photo/video
message = 5 #In a private message thread with them.

#Formula for points based on time since friended
# map(TimeSincePost, 0, TotalFbTime, 0, 1) ## Multiplier.



#####################
##Implement Sorting##
#####################

######################
## Find Old Friends ##
######################

"""







