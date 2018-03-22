label mall:
    scene mallScene
    call screen mallScreen
    return

label sexStore:
    if rLoc == "sexStore":
        scene sexSR with fade
        if rIrr >= 10:
            c "{i}I shouldn't bother [r] anymore{/i}"
        
        while True:
            
            menu:
                r "Hey, [c]. What's up?"
                
                "Chat":

                    if rIrr >= 10:
                        r "Get. Out. Now."
                        "{i}[r] kicks you out{/i}"
                        $rileyP -=5
                        jump mall
                    if rIrr >= 5 and rIrr < 10:
                        r "You know, I do work here. You don't {i}have{/i} to keep bugging me"
                        c "{i}Maybe I should leave her alone...{/i}"
                        $rIrr +=2
                        $rileyP -= 2
                    if rIrr < 5:
                        $randNum(1,3)
                        if rN == 1:
                            c "How are you, [r]?"
                            r "I'm good, not many people here today, so I get to relax, which is a nice change of pace."
                            $rIrr += 1
                        if rN == 2:
                            c "What's cookin', good lookin'?"
                            r "... No. Just, no."
                            $rIrr += 1
                        if rN == 3:
                            c "What do you recommend?"
                            r "It really depends on what you like. I {i}really{/i} like the gag ball, but that is too extreme for some. You can never go wrong with a vibrator either."
                            $rIrr += 1
                "Buy something":
                    while True:
                        menu:
                            r "What tickles your fancy?"
                            
                            "Condoms - $10":
                                if money < 10:
                                    r "Umm.. maybe you should get some actual money? I doubt you'll need these until you do"
                                    "{i}You can't afford it{/i}"
                                if money >= 10:
                                    r "Alrighty, here you go. 3 condoms. Good on you for being safe."
                                    $itemArr[2] += 3
                                    $money=money-10
                            "Lube - $20":
                                if money < 20:
                                    r "No money, no smooth jacking it."
                                    "{i}You can't afford it{/i}"
                                if money >= 20:
                                    if rileyP >= 10:
                                        r "Aww, you bought that with me in mind? I have my own, but I like the thought."
                                    else:
                                        r "Good choice! Tonight you'll experience the joy of a near frictionless workout. Have fun!"
                                    $itemArr[6] += 1
                                    $money=money-20
                            "Gag ball - $30":
                                if money < 30:
                                    r "Hng hnng... no. You need the money."
                                    "{i}You can't afford it{/i}"
                                if money >= 30:
                                    if rileyP >= 20:
                                        r "I'm looking forward to trying it on."
                                    else:
                                        r "A grunt says more than a thousand words. Hngnjoy"
                                    $itemArr[7] += 1
                                    $money=money-30
                            "Dildo - $50":
                                if money <50:
                                    r "Sorry, you won't get to insert this without money."
                                    "{i}You can't afford it{/i}"
                                if money >=50:
                                    if rileyP > 30:
                                        r "I have my own, but the more the merrier!"
                                    else:
                                        r "Going to a party? Here you go!"
                                    $itemArr[4] += 1
                                    $money=money-50
                            "Vibrator - $75":
                                if money<75:
                                    r "Vi...no. Show me the money."
                                    "{i}You can't afford it{/i}"
                                if money >=75:
                                    if rileyP >= 40:
                                        r 'Very nice, something for me to "wear" when we go out'
                                    else:
                                        r "This one is fun when you're outside. But be careful, it's a little noisy."
                                    $itemArr[5] += 1
                                    $money=money-75
                            "Anal beads - $100":
                                if money < 100:
                                    r "Sorry, you're fucked. But not by this guy."
                                    "{i}You can't afford it{/i}"
                                if money >= 100:
                                    if rileyP > 50:
                                        r "I have lube, so don't worry about that"
                                        if rileyP > 75:
                                            c "Oh no you don't, you're going to bite the pillow."
                                            r "Rough, huh? I like it."
                                    else:
                                        r "Be careful with this, it might... disappear. Oh, and if you don't have it already, you should get some lube"
                                    $itemArr[3] += 1
                                    $money=money-100
                            "Never mind":
                                jump sexStore
                            
                "Leave":
                    jump mall

    if rLoc != "sexStore":
        scene sexS with fade
        while True:
            menu:
                d "Hi, welcome to Condoments! What can I do for you?"
                
                
                "Chat":
                    d "As much as I enjoy talking about our selection, I'm too busy, sorry."
                    
                "Ask about [r]":
                    c "When does [r] work?"
                    d "She works every Wednesday and Friday, from 17:00 to 20:00"
                    
                "Buy something":
                    while True:
                        menu:
                            d "What can I get you?"
                            
                            "Condoms - $10":
                                if money < 10:
                                    "{i}You can't afford it{/i}"
                                if money >= 10:
                                    d "3 condoms. Here you go."
                                    "{i}You buy three condoms.{/i}"
                                    $itemArr[2] += 3
                                    $money=money-10
                            "Lube - $20":
                                if money < 20:
                                    "{i}You can't afford it{/i}"
                                if money >= 20:
                                    d "Here you go."
                                    "{i}You buy a bottle of lube.{/i}"
                                    $itemArr[6] += 1
                                    $money=money-20
                            "Gag ball - $30":
                                if money < 30:
                                    "{i}You can't afford it.{/i}"
                                if money >= 30:
                                    d "Here you go."
                                    "{i}You buy a gag ball.{/i}"
                                    $itemArr[7] += 1
                                    $money=money-30
                            "Dildo - $50":
                                if money <50:
                                    "{i}You can't afford it.{/i}"
                                if money >=50:
                                    d "Here you go."
                                    "{i}You buy a dildo.{/i}"
                                    $itemArr[4] += 1
                                    $money=money-50
                            "Vibrator - $75":
                                if money<75:
                                    "{i}You can't afford it.{/i}"
                                if money >=75:
                                    d "Here you go."
                                    "{i}You buy a vibrator.{/i}"
                                    $itemArr[5] += 1
                                    $money=money-75
                            "Anal beads - $100":
                                if money < 100:
                                    "{i}You can't afford it.{/i}"
                                if money >= 100:
                                    d "Here you go."
                                    "{i}You buy anal beads.{/i}"
                                    $itemArr[3] += 1
                                    $money=money-100
                            "Never mind":
                                jump sexStore

                
                "Leave":
                    d "Bye bye!"
                    jump mall
    return
    
    
    
label clothesStore:
    if sLoc == "clothesStore":
        scene clothSoph
        if sIrr >= 10:
            c "{i}I shouldn't bother [s] anymore...{/i}"
            jump mall
        s "Hi, [c]!"
        while True:
            menu:
                
                "Chat":
                    c "Hi, [s]. How are you?"
                    $randNum(1,3)
                    if sIrr < 5:
                        if rN == 1:
                            s "Im good! It's been quite busy here today, a lot of people picking up their orders, so the time is just flying by. How are you?"
                            $sIrr += 1
                        if rN == 2:
                            s "Pretty good, It's been quiet, so I have done a lot of studying. You have to love it, getting paid to study!"
                            $sIrr += 1
                        if rN == 3:
                            s "Getting by, [c]. A bit tired, I've had a long week so far."
                            $sIrr += 1
                    if sIrr >= 10:
                        s "{b}LET ME WORK{/b}"
                        "[s] kicks you out of the store"
                        $sophP -= 5
                        jump mall
                    if sIrr >= 5 and sIrr < 10:
                        s "You know... you could let me work"
                        c "{i}Maybe I should leave her alone...{/i}"
                        $sophP -= 1
                        $sIrr += 2
                    
                "Buy something":
                    if sIrr < 5:
                        s "I don't really think there is anything of interest here for you. We tailor everything, and I doubt you'll fit into our clothes, hehe."
                        $sIrr += 1
                    if sIrr >= 10:
                        s "{b}JUST LEAVE{/b}"
                        "[s] kicks you out of the store"
                        $sophP -= 5
                        jump mall
                    if sIrr >= 5 and sIrr < 10:
                        s "How many times do I have to tell you, {b}{i}There is nothing in this store for you{/b}{/i}"
                        c "{i}Maybe I should leave her alone...{/i}"
                        $sIrr += 2
                        $sophP -=1
                        
                    
                "Leave":
                    s "Bye!"
                    jump mall
    else:
        scene clothesS
        while True:
            menu:
                p "Hi, welcome to Sew it Seams! What can I do for you?"
                
                
                "Chat":
                    p "I apologize, I can't chat. I'm too busy"
                    jump clothesStore
                
                "Ask about [s]":
                    c "When does [s] work?"
                    p "She works every Wednesday and Friday, from 17:00 to 20:00"
                    
                "Buy something":
                    menu:
                        p "I'm sorry, you don't seem to have an order in. Are you picking up for someone else?"
                        
                        "No": 
                            jump clothesStore              
           
                "Leave":
                    p "Have a good one."
                    jump mall
                        
                        
    jump mall
    
    return
    
label psych:
    scene psychRec with fade
    menu:
        recept "Welcome to Psyche. What can I do for you?"
        
        "Chat":
            $randNum(1,3)
            if rN == 1:
                recept "The name Psyche is actually from the Greek goddess of the soul. You should check out the history about her, it's quite amazing."
            if rN ==2:
                recept "I know it may seem strange to have a psychiatrist in a mall, but we're actually quite popular, especially with students. We help with stress-managing."
            if rN==3:
                recept "Currently we have only one employed psychiatrist, but we're hoping we'll be able to expand to have two, that way we can help more people."
            jump psych
            
        "Set up an appointment":
            "Coming in a later update"
            jump psych
        
        "Leave":
            recept "Have a nice day!"
            jump mall
            
            
            
            
    jump mall
    return
