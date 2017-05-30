# -*- coding: cp949 -*-
loopFlag = 1
from internetmovie import *


#### Menu  implementation
def printMenu():
    print("\nWelcome! Movie Manager Program (xml version)")
    print("========Menu==========")
    #print("print Movie list: b")
    print("Get Movie data from title: g")
    #print("send maIl : i")
    print("========Menu==========")


def launcherFunction(menu):
    #if menu == 'b':
       #PrintMovieList(["title", ])
    if menu == 'g':
        title = str(input('input title to get :'))
        # isbn = '0596513984'
        ret = getMovieDataFromTitle(title)
   # elif menu == 'i':
    #    sendMain()
    else:
        print("error : unknow menu key")


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    MoviesFree()


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")
