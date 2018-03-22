label tooLate:
    $loc = "room"
    
    c "{i}It's getting late. I should get back to my room{/i}"
    "You go back to your room"
    jump room

label map:
    #scene campus with fade
    scene campus
    call screen campMap
    #hide campus

label room:
    $ show_quick_menu = True
    $loc = "room"
    $quick_menu = True
    show room with fade
    
    if dayNr == 28:
        scene fade
        "You have reached the end of the game in this version. I hope you are enjoying the game so far."
        return
## EXAM 1
    if dayNr == 18 and exRemind == 0:
        c "{i}Two days until the exam{/i}"
        $exRemind = 1
    if dayNr == 19 and exRemind == 0:
        c "{i}I have an exam tomorrow... I should study.{/i}"
        $exRemind = 1
    if dayNr == 20 and exRemind == 0 and tod >= 6:
        "Exam1"
        $exRemind = 1
        jump exam
## EXAM 2
    if dayNr == 38 and exRemind == 0:
        c "{i}Two days until the exam{/i}"
        $exRemind = 1
    if dayNr == 39 and exRemind == 0:
        c "{i}I have an exam tomorrow... I should study.{/i}"
        $exRemind = 1
    if dayNr == 40 and exRemind == 0 and tod >= 6:
        "Exam2"
        $exRemind = 1
        
## EXAM 3
        
    if dayNr == 58 and exRemind == 0:
        c "{i}Two days until the exam{/i}"
        $exRemind = 1
    if dayNr == 59 and exRemind == 0:
        c "{i}I have an exam tomorrow... I should study.{/i}"
        $exRemind = 1
    if dayNr == 60 and exRemind == 0 and tod >= 6:
        $exRemind = 1
        "Exam3"
        
## EXAM 4
    
    if dayNr == 78 and exRemind == 0:
        c "{i}Two days until the exam{/i}"
        $exRemind = 1
    if dayNr == 79 and exRemind == 0:
        c "{i}I have an exam tomorrow... I should study.{/i}"
        $exRemind = 1
    if dayNr == 80 and exRemind == 0 and tod >= 6:
        $exRemind = 1
        "Exam4"
        
## EXAM 5

    if dayNr == 98 and exRemind == 0:
        c "{i}Two days until the exam{/i}"
        $exRemind = 1
    if dayNr == 99 and exRemind == 0:
        c "{i}I have an exam tomorrow... I should study.{/i}"
        $exRemind = 1
    if dayNr == 100 and exRemind == 0 and tod >= 6:
        $exRemind = 1
        "Exam5"
    
    
    if intro == 3:
        jump dormMeet
    if intro == 1:
        menu:
            "What do you want to do?"
            
            "Play videogames":
                $intro == 2
                jump gaming
                
            "Take a nap":
                "You take a nap"
                $intro == 2
                jump laydwn
                
    
        
    else:
        menu:
            "What do you want to do?"
            
            "Go to class" if tod >= 7 and tod <= 10 and day <= 4:
                "You go to class"
                hide room
                jump a_class
            
            "Practice your charisma" if tod >=  7:

                if charTrain >= 5:
                    "You have trained charisma too much today"
                    jump room
                "You spend an hour training charisma."
                $rngesus()
                if luck == 1:
                    $char += 0
                    c "{i}Well, that did nothing...{/i}"
                if luck == 2:
                    $char+= 1
                    c "{i}Hey, I feel a big more charismatic!{/i}"
                if luck == 3:
                    $char+=2
                    c "{i}Man, I could charm the pants of a nun!{/i}"
                $tod+=1
                $charTrain+=1
                jump room
            
            "Leave your room":
                if tod <= 6:
                    "It's too late to leave..."
                    jump room
                $loc = "elsewhere"
                hide room
                jump hall
            
            "Go outside":
                if tod <= 6:
                    c "{i}It's too late to go out, I should go to bed{/i}"
                    jump room
                $loc = "elsewhere"
                hide room
                jump map            
            
            "Sit on the computer":
                if tod <= 6:
                    c "{i}I should go to bed...{/i}"
                    jump room
                hide room
                jump computer
            "Take a nap" if tod <= 19 and tod >= 6:
                "You take a nap"
                $tod += 1
                hide room
                jump room 
                
            "Go to sleep" if tod >= 20 or tod <= 5:
                "You go to sleep"
                $loc = "elsewhere"
                $doDecay()
                $reset()
                $dayNr += 1
                $day+= 1
                if day > 6:
                    $day = 0
                $whichDay()
                $tod = 7
                hide room with dissolve
                jump room
    return
    
    
label secretP:
    if secunlock == 0:
        $ hemmelig = renpy.input ("Enter code")
        if hemmelig == hemmeligpassord:
            "Enjoy"
            $secunlock = 1
            jump unlockedSec
        else:
            "Sorry, buddy. You can get the code if you're a patreon. {size=-10}Or somewhat familiar with renpy.{/size}{size=-15}pleasesupportme{/size}"
            jump computer
    if secunlock == 1:
        jump unlockedSec
        
        
label unlockedSec:
    $ renpy.movie_cutscene("maps/hemmelig1.m2t")
    $ renpy.movie_cutscene("maps/hemmelig2.m2t")
    $ renpy.movie_cutscene("maps/hemmelig3.m2t")
    
    jump computer

