label court:
    "Nothing"
    return

label poolDresserFirst:

    scene poolDress with fade
    if webCLoc[-1] == 0 and itemArr[0] == 1:
        c "{i}I need to find a place to hide the camera...{/i}"
        call screen poolDress
    if webCLoc[-1] == 1:
        call screen poolDress
        jump pool
    else:
        jump poolDressNC
    return
    
label poolDressNC:
    scene poolDress
    "There is nobody in the dressing room"
    c "{i}Hmm, maybe I can install a camera somewhere here..."
    menu:
        "What do you do?"
        
        "Leave":
            $tod += 1
            jump pool
    return
    
label poolDresser:
    call screen poolDress
    return
    
label poolclosed:
    "The pool is closed"
    jump map
    return


label camInstallPool:
    scene poolDress
    if itemArr[0] >= 1:
        "You install the spycam."
        "You can access the camera feed on your computer"
        $webCLoc[-1] = 1
        $itemArr[0]-=1
        jump pool
    elif webCLoc[-1] == 1:
        menu:
            "Do you want to remove the camera?"
            
            "Yes":
                "You remove the camera."
                $webCLoc[-1] = 0
                $itemArr[0]+=1
                jump pool
                
            "No":
                "You leave the camera."
                jump pool
    else:
        c "{i}I don't have a camera...{/i}"
        jump pool
        

label camInstallPFail:
    scene poolDress
    if webCLoc[-1] == 1:
        c "{i}I have the memory of a brick... That's not where I put it...{/i}"
        jump poolDresser
    c "{i}They would have to be retarded not to find the camera here...{/i}"
    jump poolDresser
    
    
label pool:
    $timeLoc()
    if rLoc == "pool":
        scene rpool with fade
    elif aLoc == "pool":
        scene apool with fade
    elif sLoc == "pool":
        scene spool with fade
    elif eLoc == "pool":
        scene epool with fade
    else:
        scene pool with fade
    
        
    
    
    if strTrain >= 5:
        "You are exhausted, you need to rest."
        jump map
    
    if tod >= 23 or tod <= 6:
        "The pool is closed."
        jump map
    
    menu:
        "What do you want to do?"
        
        "Peek in the dressing room":
            if  (tod < 22 and tod >= 5):
                c "{i}I shouldn't do that now... I should wait until later{/i}"
                "You should come back after 22:00."
                jump pool
            if aLoc == "pool" or rLoc== "pool" or eLoc== "pool" or eLoc == "pool":
                c "{i}There's someone here... I have to wait for them to leave{/i}"
                jump pool
            else:
                jump poolDresserFirst
        
        "Go for a swim":
            "You swim for an hour"
            $strDecay = 1
            $stre += 1
            $tod += 1
            $strTrain += 1
            jump pool
            
        "Talk to [a]" if aLoc == "pool":
            a "Hey, [c]!"
            c "Hi, [a]. How are you?"
            a "I'm good."
            menu:
                "Mind if i join you?":
                    menu:
                        a "Ok, just don't splash me please!"
                        
                        "Splash":
                            show apool1
                            a "Gaah! You dick!"
                            show apool3
                            "[a] splashes you back."
                            show apool2
                            "[a] has menace in her eyes as she splashes you back."
                            show apool4
                            "[a] leaps towards you, squeezing her breasts on your face."
                            c "Hngsgnnghna"
                            a "Take that, you bastard!"
                            show apool5
                            "[a] blushes, embarrassed, realizing what she just had done."
                            a "Anyway, let's swim."
                            show apool6
                            "You spend the remaining time swimming with [a]."
                            $tod+=1
                            
                        "Don't splash":
                            show apool5
                            "You spend an hour swimming with [a]."
                            $tod+=1
                            jump pool
                "Mind if I just enjoy the view?"if arielP >= 20:
                    a "Well... okay, then."
                    "You spend an hour watching, enjoying [a] as she obviously shows off her petite body in the warm water."
                    a "I hope you enjoyed the show."
                    "[a] kisses your cheek."
                    $tod+=1
                    
                "Leave":
                    c "Well, I have to go, I was just passing by. See ya!"
                    a "Bye!"
                    "As you leave, [a] dives into the pool."
                    jump map
            
            
        "Talk to [s]" if sLoc == "pool":
            "Hi [s]"
            $tod += 1
            jump pool
            
        "Talk to [r]" if rLoc == "pool":
            "Hi [r]"
            $tod += 1
            jump pool
            
        "Talk to [e]" if eLoc == "pool":
            "Hi [e]"
            $tod += 1
            jump pool
                       

            
            
        "Leave":
            jump map
            
            
    return
