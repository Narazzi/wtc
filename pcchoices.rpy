init python:
    import random

label computer:
    $instWC = 0
    $timeLoc()
    $ show_quick_menu = False
    hide screen porno
    scene pcbg
    if tod <= 6:
        c "{i}It's late... I should go to bed{/i}"
        jump room
    call screen pcsc
    return        

label folder:
    if intTrain >= 5:
        "You have a headache from studying too much today."
        jump computer
    menu:
        "Do you want to spend an hour studying?"
        
        "Yes":
            "You study for an hour. You feel smarter"
            python:
                tod += 1   
                inte = inte + 1
            jump computer
        "No":
            jump computer
    return

    
    
label cam1:
    $randNum(1,15)
    $tod+= 1
    show screen webcVid
    if rN == 1:
        show poolS1:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
        hide poolS1
    elif rN == 2:
        
        show poolS2:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 3:
        show poolS3:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 4:
        show poolS4:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 5:
        show poolS5:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 6:
        show poolS6:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 7:
        show poolS7:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 8:
        show poolS8:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 9:
        show poolS9:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 10:
        show poolS10:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 11:
        show poolS11:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 12:
        show poolS12:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 13:
        show poolS13:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 14:
        show poolS14:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
    elif rN == 15:
        show poolS15:
            zoom 0.7
            xalign 0.42
            yalign 0.485
        pause
        
    jump computer
label cam2:
    "Test2"
    jump computer
label cam3:
    "Test3"
    jump computer
label cam4:
    "Test4"
    jump computer
label cam5:
    "Test5"
    jump computer
    
label webC1:
    if webCLoc[0] == 1:
        jump cam1
    elif webCLoc[1] == 1:
        jump cam2
    elif webCLoc[2] == 1:
        jump cam3
    elif webCLoc[3] == 1:
        jump cam4
    elif webCLoc[4] == 1:
        jump cam5
    
    jump computer
    
label webC2:
    if webCLoc[1] == 1:
      jump cam2
    elif webCLoc[2] == 1:
       jump cam3
    elif webCLoc[3] == 1:
        jump cam4
    elif webCLoc[4] == 1:
        jump cam5
    elif webCLoc[0] == 1:
        jump cam1
    
    jump computer
    
label webC3:
    if webCLoc[2] == 1:
        jump cam3
    elif webCLoc[3] == 1:
        jump cam4
    elif webCLoc[4] == 1:
        jump cam5
    elif webCLoc[0] == 1:
        jump cam1
    elif webCLoc[1] == 1:
        jump cam2
    
    jump computer
    
label webC4:
    if webCLoc[3] == 1:
        jump cam4
    elif webCLoc[4] == 1:
        jump cam5
    elif webCLoc[0] == 1:
        jump cam1
    elif webCLoc[1] == 1:
        jump cam2
    elif webCLoc[2] == 1:
        jump cam3
    
    jump computer
    
label webC5:
    if webCLoc[4] == 1:
        jump cam5
    elif webCLoc[0] == 1:
        jump cam1
    elif webCLoc[1] == 1:
        jump cam2
    elif webCLoc[2] == 1:
        jump cam3
    elif webCLoc[3] == 1:
        jump cam4
    
    jump computer
    
label shop:
    menu:
        "What do you want to buy? You currently have $[money]"
#itemIArr
 #0Cam, 1Choc, 2Condom, 3analbeads, 4dildo, 5vibrator, 6lube, 7gagball
        "Spy cam - $500":
            if money >= 500:
                "You bought a Spy Camera"
                $itemArr[0] += 1
                $money -= 500
                jump shop
            if money < 500:
                "You don't have enough money"
                jump shop
        "Chocolate - $25":
            if money >= 25:
                "You bought some chocolates"
                $itemArr[1] += 1
                $money -= 25
                jump shop
            if money < 25:
                "You don't have enough money"
                jump shop
        "Condoms - $10":
            if money >= 10:
                "You bought four condoms"
                $itemArr[2] += 3
                $money -= 10
                jump shop
            if money < 10:
                "You don't have enough money"
                jump shop           
        "Never mind":
            jump computer            
    return
    
label porn:
    $tod += 1
    menu:
        "Do you want to spend an hour watching porn?"
    
        "Yes":
            show screen porno
            show pornsc1
            pause
            hide screen porno
            hide pornsc1
        "No":
            jump computer
    return
    
label webcam:
    $wcCount()
    #if wcA + wcS + wcE + wcR == 0:
      #  "You dont have any cameras installed"
        #jump computer
    if instWC >= 1:
        menu:
            "Watching cameras will take an hour. Are you sure you want to check your cameras?"
            
            "Yes":
                call screen webcam
            "No":
                jump computer
    else:
        "You have no cameras installed"
        jump computer
    return
    
label patreon:
    "Not implemented yet"
    #$ webbrowser.open("http://www.patreon.com/narazzi")
    jump computer
    
label shutdown:
    menu:
        "Are you sure you want to turn off the computer?"
        
        "Yes":
            $show_quick_menu = True
            jump room
        "No":
            jump computer
    return
