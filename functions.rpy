
init python:
    import math
    import random
    import time
    
    def invent():
        global emptyArr, itemArr
        i = 0
        while i < len(itemArr):
            if itemArr[i] > 0:
                emptyArr[i] = itemIArr[i]
            i+=1
        return
    
    x = random.randint(1,3)
    def rngesus():
        global luck
        luck = random.randint(1,3) 
        return

          
    def randNum(lowN, highN):
        global rN
        rN = random.randint(lowN ,highN)
        return
        
    def dialogueRandS():
        global dialogue
        if sophP >= 50:
            if sophHorny == 0:
                dialogue = random.randint(0,7)
                return
            else:
                dialogue = random.randint(0,6)
        else:
            dialogue = random.randint(0,5)
        return


    def randEnc():
        #["Hall2", "hall", "roomA", "roomS", "roomE", "roomR", "room", "a_class", "b_class", "c_class", "court", "pool", "mall_1", "mall_2", "dorm", "dining", "sexstore", "clothesStore"]
        global locations, aLoc, rLoc, eLoc, sLoc, testLoc
        
        if tod >= 17 and tod <= 20:
            tall = random.randint(1,4)
            if tall == 3:
                rLoc = locations[11]
            if tall == 4:
                eLoc = locations[11]
                
            
        
        return



        

#Cam, Choc, Condom, analbeads, dildo, vibrator, lube, gagball

        
    def doDecay():
        ranS = random.randint(0,5)
        ranI = random.randint(0,5)
        global intWeek, strWeek, day, strDecay, stre, inte
        dayStr = 0
        dayInt = 0
        if strDecay == 1:
            strWeek[day] == 1
            strDecay == 0
        if intDecay == 1:
            intWeek[day] == 1
            intDecay == 0
        if day == 6:
            for i in strWeek:
                dayStr += strWeek[i]
            if dayStr > 3:
                stre == stre
            elif dayStr <= 3:
                stre -= ranS
            for j in intWeek:
                dayInt += intWeek[j]
            if dayInt > 3:
                inte == inte
            elif dayInt <= 3:
                inte -= ranI
        intWeek = [0, 0, 0, 0, 0, 0, 0]
        strWeek = [0, 0, 0, 0, 0, 0, 0]
        return
            
        
        return

    def grading(points):
        global grade
        if points <= 59:
            grade = "F"
        elif points >= 60 and points <= 69:
            grade = "D"
        elif points >= 70 and points <= 79:
            grade = "C"
        elif points >= 80 and points <= 89:
            grade = "B"
        elif points >= 90:
            grade = "A"
        return
        
    def workTutor(hours):
        global money, earned, inte
        if inte > 25 and inte < 40:
            earned = int(math.ceil(hours * (inte * 0.1)))
        else:
            earned = int(math.ceil(hours * (inte * 0.2))) 
        money += earned
        
    def wcCount():
        global instWC
        instWC = 0
        for x in webCLoc:
            instWC+= x
        return
    
    def reset():
        global sophHorny, charTrain, dailyFS, studyTA, strTrain, intTrain, charTrain, dinnerS, instWC, worked, earned, sIrr, rIrr, exRemind, examDay
        sophHorny = 0
        charTrain = 0        
        dailyFS = 0
        dailyFA = 0
        dailyFE = 0
        dailyFR = 0
        studyTA = 0
        strTrain = 0
        intTrain = 0
        charTrain = 0
        dinnerS = 0
        instWC = 0
        worked = 0
        earned = 0
        sIrr = 0
        rIrr = 0
        exRemind = 0
        examDay = 0
        return

    def timeandDay():
        global tod, day, dayNr
        if tod  ==  24:
            tod = 0
            reset()
            day+=1
            dayNr+=1
            if day > 6:
                day = 0
        return
                
    def whichDay():
        global week, today, day
        today = week[day]
        return

        
        
    def sDateSel():
        global sDateArr, sDateNo
        if sDateArr[-1] == 1:
            return
        else:
            for i in sDateArr:
                if sDateArr[i] == 0:
                    sDateNo = i+1
                    return
        return
        
    def aDateSel():
        global aDateArr, aDateNo
        if aDateArr[-1] == 1:
            return
        else:
            for i in aDateArr:
                if aDateArr[i] == 0:
                    aDateNo = i+1
                    return
        return
        
    def eDateSel():
        global eDateArr, eDateNo
        if eDateArr[-1] == 1:
            return
        else:
            for i in eDateArr:
                if eDateArr[i] == 0:
                    eDateNo = i+1
                    return
        return
        
    def rDateSel():
        global rDateArr, rDateNo
        if rDateArr[-1] == 1:
            return
        else:
            for i in rDateArr:
                if rDateArr[i] == 0:
                    rDateNo = i+1
                    return
        return

    def timeLoc():
        y = random.randint(1,5)
        global aLoc, eLoc, sLoc, rLoc, day, tod
        if day <= 4:
            if tod <= 6:
                aLoc = "sleep"
                rLoc = "sleep"
                eLoc = "sleep"
                sLoc = "sleep"
            elif tod >= 7 and tod <= 8:
                aLoc = "roomA"
                rLoc = "roomR"
                eLoc = "roomE"
                sLoc = "roomS"
            elif tod >= 9 and tod <= 10:
                aLoc = "a_class"
                eLoc = "b_class"
                rLoc = "b_class"
                sLoc = "c_class"
            elif tod == 11:
                aLoc = "dining"
                eLoc = "dining"
                rLoc = "dining"
                sLoc = "dining"
            elif tod >= 12 and tod <= 14:
                aLoc = "b_class"
                eLoc = "c_class"
                rLoc = "c_class"
                sLoc = "a_class"
            elif tod == 15:
                aLoc = "roomA"
                rLoc = "roomR"
                eLoc = "roomE"
                sLoc = "roomS"
            elif tod == 16:
                aLoc = "dining"
                rLoc = "dining"
                eLoc = "dining"
                sLoc = "dining"
            elif tod >= 17 and tod <= 21:
                if day == 2 or day == 4:
                    rLoc = "sexStore"
                elif day == 1 or day == 3:
                    sLoc = "clothesStore"
        
                if y == 1:
                    aLoc = "pool"
                    eLoc= "roomE"
                    rLoc= "roomR"
                    sLoc= "mall"
                elif y == 2:
                    aLoc= "mall"
                    eLoc= "pool"
                    rLoc= "roomR"
                    sLoc= "roomS"
                elif y == 3:
                    aLoc= "roomA"
                    eLoc= "mall"
                    rLoc= "pool"
                    sLoc= "roomS"
                elif y == 4:
                    aLoc= "roomA"
                    eLoc= "roomE"
                    rLoc= "mall"
                    sLoc= "pool"
                elif y == 5:
                    aLoc= "roomA"
                    eLoc= "pool"
                    rLoc= "roomR"
                    sLoc= "roomS"
            elif tod >= 22:
                aLoc= "roomA"
                eLoc= "roomE"
                rLoc= "roomR"
                sLoc= "roomS"

                
                    
        
        if day >= 5:
            if tod <= 6:
                aLoc = "sleep"
                rLoc = "sleep"
                eLoc = "sleep"
                sLoc = "sleep"
            elif tod >= 7 and tod <= 10:
                aLoc= "roomA"
                eLoc= "roomE"
                rLoc= "roomR"
                sLoc= "roomS"
            elif tod == 11:
                aLoc= "dining"
                eLoc= "dining"
                rLoc= "mall"
                sLoc= "mall"
            elif tod >= 12 and tod <= 14:
                if y == 1:
                    aLoc = "pool"
                    eLoc= "roomE"
                    rLoc= "roomR"
                    sLoc= "mall"
                elif y == 2:
                    aLoc= "mall"
                    eLoc= "pool"
                    rLoc= "roomR"
                    sLoc= "roomS"
                elif y == 3:
                    aLoc= "roomA"
                    eLoc= "mall"
                    rLoc= "pool"
                    sLoc= "roomS"
                elif y == 4:
                    aLoc= "roomA"
                    eLoc= "roomE"
                    rLoc= "mall"
                    sLoc= "pool"
                elif y == 5:
                    aLoc= "roomA"
                    eLoc= "pool"
                    rLoc= "roomR"
                    sLoc= "roomS"
            elif tod == 15:
                aLoc= "roomA"
                eLoc= "roomE"
                rLoc= "roomR"
                sLoc= "roomS"
            elif tod == 16:
                aLoc= "dining"
                eLoc= "dining"
                rLoc= "dining"
                sLoc= "dining"
            elif tod >=  17 and  tod <= 20:
                if y == 1:
                    aLoc = "pool"
                    eLoc = "mall"
                    rLoc = "roomR"
                    sLoc = "roomS"
                elif y == 2:
                    aLoc = "mall"
                    eLoc = "pool"
                    rLoc = "roomR"
                    sLoc = "roomS"
                        
                elif y == 3:
                    aLoc = "roomA"
                    eLoc = "pool"
                    rLoc = "mall"
                    sLoc = "roomS"
                        
                elif y == 4:
                    aLoc = "roomA"
                    eLoc = "roomE"
                    rLoc = "pool"
                    sLoc = "mall"
                        
                elif y == 5:
                    aLoc = "roomA"
                    eLoc = "roomE"
                    rLoc = "roomR"
                    sLoc = "roomS"
            elif tod >= 21:
                aLoc = "roomA"
                eLoc = "roomE"
                rLoc = "roomR"
                sLoc = "roomS"
