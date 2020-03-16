
def printandget(count,lst):
    print('game is start with player one')
    print('')
    list=[] 
    for i in range(0,count):
        print('Enter a number 1 for sang 2 for kaghaz and 3 for gheche (%s)') % (lst[i])
        x=input() 
        list.append(x)
    return list
    
def getinput(count):
    list=[]
    for i in range(0,count):
        print ('Pleas Enter a name of player(%s)') % str(i+1)
        x=raw_input() 
        list.append(x)
    return list

def showResult(namelist,answerlist):
    sang,kaghaz,gheche='sang','kaghaz','gheche'
    print('-------------------------------------')
    print('name                 answer')
    print('')
    
    for i in range(0,len(namelist)):
        if answerlist[i] == 1:
            print(namelist[i] + '                   ' + sang) 
        elif answerlist[i] == 2 :
             print(namelist[i] + '                   ' + kaghaz)
        else:
             print(namelist[i] + '                   ' + gheche)
# sang kaghaz|kaghaz sang|gheche sang|sang gheche|kaghaz gheche|gheche kaghaz                  
def rewardsOfPlayers(answerlist):
    sang,kaghaz,gheche=1,2,3
    list=[]
    if answerlist[0] == answerlist[1]:
        #TODO PLAYER DONT GET REWARDS
        setReward(0,0)
    elif  answerlist[0] == sang and answerlist[1] == kaghaz :
        #TODO PLAYER TOW WINER
        setReward(0,1)
    elif answerlist[0] == sang and answerlist[1] == gheche :
        #TODO PLAYER ONE WINER
        setReward(1,0)
    elif answerlist[0] == kaghaz and answerlist[1] == sang :
        #TODO PLAYER ONE WINER
        setReward(1,0)
    elif answerlist[0] == gheche and answerlist[1] == sang :
        #TODO PLAYER TOW WINER
        setReward(0,1)
    elif answerlist[0] == kaghaz and answerlist[1] == gheche :
        #TODO PLAYER TOW WINER
        setReward(0,1)    
    else:
        #TODO PLAYER ONE WINER
        setReward(1,0)
                                       
def setReward(r1,r2):
    #rewardPlayerone=0
    global rewardPlayertow
    global rewardPlayerone  
    rewardPlayerone +=r1 
    rewardPlayertow += r2 
    list={'playerone':'0'+str(rewardPlayerone),'playertow':'0'+str(rewardPlayertow)}
    return list
    
def show(list,listofname):
    namewiner=''
    print('name                       result')
    print(listofname[0]+'                       '+list['playerone'])
    print(listofname[1]+'                       '+list['playertow'])
    if int(list['playerone']) > int(list['playertow']):
        namewiner=listofname[0]
    else:
        namewiner=listofname[1] 
    print('winer is => ' + namewiner)                                       
count = 2
rewardPlayerone=0
rewardPlayertow=0
# 1 sang 2 kaghaz 3 gheche
listofname=getinput(count)

for i in range(0,3):
    listofanswer=printandget(count,listofname)
    showResult(listofname,listofanswer)
    rewardsOfPlayers(listofanswer)

print ('-------------------------------------')
show(setReward(0,0),listofname)
