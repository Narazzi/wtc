## Sophia events


label sophieRoom:
    if dailyFS >= 3:
        "I've bothered her enough today..."
        jump hall
    if tod >= 7 and tod <= 17:
        show Sroomday with fade
    if tod >= 18:
        show Sroomeve with fade
        
    
    
    s "Hi, [c]. What's up?"
    menu:
        " "
        
        "Hang out" if sophP >= 10:
            $dailyFS += 1
            $dialogueRandS()
            s "Sure, have a seat. I prefer sitting on the bed when hanging out with people"
            "[s] walks over to the bed and sits down."
            hide Sroomday
            hide Sroomeve
            scene sophrtalkk
            if dialogue == 0:
                
                s "I have to admit, I didn’t expect a communications major to have so many different classes. It’s kind of funny, we have one class simply named “persuasion. It's my favorite class"
                s 'We learn different techniques of how to persuade someone and how to formulate ourselves to create a persuasive argument.'
                $sophP+=1
            if dialogue == 1:
                s 'I hate one of my classes… I chose media history and I can’t stand how boring the classes are. It’s interesting enough to see how media has developed over time, but the professor is so boring.'
                s "All he does is show us a PowerPoint presentation, and he just says what the slides say, and has one of his hands in his pocket. Every. Damn. Class."
                $sophP+=1
            if dialogue == 2:
                s "Do you ever get homesick? I really do… I miss just going around to my best friends’ house and hang out with her."
                s "I also miss gossipping about who the cutest boy is, talking about how stupid some of the stuck up girls are, not to mention who’s the sluttiest… and no, don’t get any ideas - it wasn’t me, haha"
                $sophP+=1
            if dialogue == 3:
                s "There are so many douchebags on this campus, so I have to admit, I was a little worried when I saw a man was going to move into our dorm… it seems my worries were unjustified." 
                s "You seem kind. It’s a quality a lot of people don’t have. Too many people don’t care about other people. You, however, spend time with others, me included. So, thanks."
                $sophP+=1
            if dialogue == 4:
                s "Want to know a secret? I was bullied in middle-school. I was short, chubby and I liked to read. Not a great combination, you know? But when I got to high-school, I had my growth spurt." 
                s "I got taller than all the girls, got these huge boobs, so all the boys wanted me. I both loved and hated it… It’s nice not being bullied, but having boys stare at you constantly isn’t the most comfortable situation either."
                $sophP+=1
            if dialogue == 5:
                s "Have you ever experienced euphoria? I mean, real euphoria. I haven’t, but I really want to."
                s "Don’t get me wrong, I’m not unhappy, I’m quite happy, but I haven’t ever felt that true sense of euphoria. Not through media, achievements or sex. Oh well, I’ll get there someday"
                $sophP+=1
            if dialogue == 6:
                s "What’s your favorite sexual position? Mine is cow-girl. I love being on top and being in control. Also, it’s really hot to see the guy enjoying me bouncing. I think a lot of guys like that position, because they get a nice view."
                $sophP+=1
            if dialogue == 7:
                s "I’m really horny right now. Let's play a little game."
                $sophP+=1
                $ sophHorny = 1
                $ renpy.block_rollback()
                menu:
                    "What is my favorite class?"
                    
                    "Persuasion":
                        $ renpy.block_rollback()
                        s "Good job. Now, reward one."
                        
                    "Media History":
                        $ renpy.block_rollback()
                        s "Wrong. I'm suddenly not in the mood. Please leave."
                        $tod+=1
                        jump hall
                    "Intercultural communication":
                        $ renpy.block_rollback()
                        s "Wrong. I'm not in the mood anymore. Please leave."
                        $tod+=1
                        $ renpy.block_rollback()
                        jump hall
                $ renpy.block_rollback()
                menu:
                    "What is my age?"
                    
                    "20":
                        $ renpy.block_rollback()
                        s "Yes! Here is your second reward."
                        $tod+=1
                    "21":
                        $ renpy.block_rollback()
                        s "No... You can leave now."
                        $tod+=1
                        jump hall
                    "22":
                        $ renpy.block_rollback()
                        s "No! For fucks sake. Get out."
                        $tod+=1
                        jump hall
                $ renpy.block_rollback()
                menu:
                    "What is my favorite sport?"
                    
                    "Football":
                        $ renpy.block_rollback()
                        s "No! Get out."
                        $tod+=1
                        jump hall
                    "Volleyball":
                        $ renpy.block_rollback()
                        s "You are right. Here's your third reward"
                        $tod+=1
                    "You don't like sports":
                        $ renpy.block_rollback()
                        s "God damn it, no. Leave now."
                        $tod+=1
                        jump hall
                $ renpy.block_rollback()
                menu:
                    "What is my major?"
                    
                    "Communications":
                        $ renpy.block_rollback()
                        s "Yes! And here's your final prize"
                        
                    "Media":
                        $ renpy.block_rollback()
                        s "No. Get out. Now."
                        $tod+=1
                        
                    "Journalism":
                        $ renpy.block_rollback()
                        s "Close, but no cigar. Please leave me alone" 
                        $tod+=1
                        
        "Give gift":
            menu:
#define itemIArr = ['items/cami.png', 'items/choci.png', 'items/condi.png', 'items/anali.png', 'items/dili.png', 'items/vibi.png', 'items/lubi.png', 'items/gagi.png']                
                "Give chocolates" if itemArr[1] != 0:
                    $sophItems[0]+=1
                    #chocolate, analbeads, dildo, vibrator, gagball, lube
                    c "Do you want some chocolates?"
                    if sophItems[0] >= 5:
                        s "No thank you, [c]. I have so much chocolate already."
                    else:
                        s "Of course, I love chocolate!"
                "Give Anal beads" if itemArr[3] != 0 and sophP >= 50 and sophItems[1] == 0:
                    c "Do you consider yourself open-minded?"
                    s "Where are you going with this?"
                    c "Well, I have something for you, but I'm worried you'll freak out"
                    s "Nonsense, I love gifts!"
                    c "Alright, but don't freak out!"
                    "You show [s] the anal beads"
                    s "WHAT?!"
                    c "That's why I asked you!"
                    s "Let me see it."
                    c "Alright"
                    "You hand [s] the anal beads."
                    s "So you're into this?"
                    c "Well... yeah, I wouldn't give it to you if not."
                    "[s] looks at the anal beads."
                    s "Hmm..."
                    c "{i}This doesn't look good...{/i}"
                    show sophbeadtalk
                    s "Alright. I'll hold on to this. However - you don't get to ask about it. You don't get to ask if I have used it, if I want to use it, or anything of the like, okay?"
                "Give Dildo" if itemArr[4] != 0 and sophP >= 30:
                    "[emptyArr[4]]"
                "Give Vibrator" if itemArr[5] != 0 and sophP >= 30:
                    "[emptyArr[5]]"
                "Give gag ball" if itemArr[7] != 0 and sophP >= 40:
                    "[emptyArr[7]]"
            
        "Ask out" if sophP >= 15 and tod >= 16 and sophDateDay == 0:
            $sophDateDay = 1
            $sDateSel()
            c "[s], do you want to go on a date?"
            if sophP >=15 and sophP <= 25:
                s "Alright."
            if sophP > 25:
                s "I'd love to, [c]"
            jump sophDate
                
            
        
        "Ask to dinner" if tod > 15 and (day == 5 or day == 6) and dinnerS == 0:
            $dinnerS = 1
            jump dinnerSoph
            
        "Ask about her plans for the day" if tod <= 12:
            jump testDialogue
            if day == 2 or day == 4:
                s "After class I'm heading off to work. I work at the clothes store over at the mall if you want to drop by! I work from 17 - 20."
                jump sophieRoom
            else:
                s "Not much, really. Probably studying a little. Maybe going to the pool. Not sure"
                jump sophieRoom
            
        "Flirt" if char >= 20 and dailyFS == 0:
            c "Just wanted to look say hi to the most beautiful girl on campus"
            $sophP += 1
            $dailyFS = 1
            s "Well, I suppose I should say hello to the most charming man on campus. Hello."
            jump sophieRoom
            
        "Make a move" if sophP >= 30:
            jump sophMove
            
        "Never mind, I forgot":
            jump hall
    $tod += 1
    jump hall
    return
label sophAsleep:
    scene soSl with fade
    "Soph sleep"
    hide soSl
    jump hall
    return
    
label sophOut:
    scene hall
    if sophP >= 10:
        c "{i}[s] is not in, but apparently her door is open{/i}"
        menu:
            "Do you enter the room?"
            
            "Yes":
                hide hall
                jump prySoph
                
            "No":
                jump hall
            
    else:
        "[s] isn't in her room..."

    jump hall
    return
    

    
label prySoph:
    scene sophroom with fade
    menu:
        "What do you do?"
        
        "Check her drawers":
            "You don't find anything of interest."
            jump prySoph
        
        "Check her computer":
            "It's password protected..."
            jump prySoph
        
        "Install spy cam" if itemArr[0] >= 1 and webCLoc[1] == 0:
            "You install a spycam in [s]' room. You can access it  from your PC."
            $itemArr[0]-=1
            jump prySoph
        "Remove spy cam" if webCLoc[1] == 1:
            "You remove the installed spycam."
            $itemArr[0]+=1
            jump prySoph
            
        "Leave":
            hide sophroom
            $tod+=1
            jump hall
    return
    

    
label sophMove:
    if sophP >= 20:
        menu:
            "What do you do?"
            
            "Kiss" if sophP >= 20:
                "You sit next to [s] and look into her eyes."
                show sophkiss
                "As you kiss her, she is taken aback by your kiss, but leans in nonetheless. Your tongue enters her warm mouth as you feel her hands on your back"
                hide sophkiss
                show sophafterkiss
                s "That was lovely, [c]. But I actually have to study. How about you go back to your room, and perhaps we can continue this tomorrow?"
                "[s] winks at you"
                $sophP+= 1
                $tod+=1
                jump hall
                
            "Blowjob" if sophP >= 35:
                "You walk over to [s], but before you get the chance to sit down, she grabs you by the hand and leads you to her bed."
                
                show bjswait
                "[s] gets down on her knees and unbuttons your pants." 
                "As she sees your dick she can't help but utter a slight gulp"
                s "*gulp* It's huge! I don't know if I'll be able to get it all in..."
                s "Only one way to find out..."
                "[s] opens her mouth and slowly starts sucking your cock, taking it as deep as she's able to."

                
                hide bjswait
                hide Sroomday
                hide Sroomeve
                
                
                $ renpy.movie_cutscene('events/soph/bj/sophbj1.m2t', delay=None, loops=5)
                $ renpy.movie_cutscene('events/soph/bj/sophbj2.m2t', delay=None)
                show bjsophscene
                #pause 10
                #$ renpy.movie_cutscene('events/soph/bj/sophbj3.m2t')
                #show bjsanim
                "You feel a huge surge of pleasure as you are about to cum."
                c "I'm cumming!"
                hide bjsophscene                
                show bjscum with flash
                show bjscum with flash
                
                "[s] takes your dick out of her mouth and points it at her face"
                hide bjscum
                hide bjscum
                show bjsafter
                s "Wow... I can see you had a lot saved up"
                s "That was fun, but I have to clean myself up. How about you go back to your room, and maybe you'll get to repeat this. Perhaps maybe you'll get some more."
                
             
                "As you get up to walk away, you see [s] licking her the cum off her lips"
                hide bjsafter
                show intro
                c  "{i}Nice...{/i}"
                hide intro
                hide bjscloth
                hide bjswait    
                hide bjsanim
                hide bjscum
                hide bjsafter
                hide Sroomeve
                hide Sroomday
                $ show_quick_menu = True
                $tod += 1
                $sophP+=1
                jump hall
    
            
            "Sex" if sophP >= 45:
                "You walk over to [s]. You push her down onto the couch and kiss her."
                
            
            #"Anal" if sophP >= 75
    
label dinnerSoph:
    #show intro with fade
    menu: 
        "Where do you go?"
        
        "Burger place":
            "You take [s] to the burgerplace at the mall."
            hide Sroomeve 
            hide Sroomday
            show burgS with fade
            menu:
                "Do you pay for her food?"
                
                "Yes ( - $ 20)" if money >= 20:
                    $money-=20
                    $sophP += 2
                    s "Oh, thank you, [c]. Such a gentleman!"
                    "[s] smiles."
                    
                "No, just my own ( - $10)":
                    $sophP += 1
                    $money-=10
                    
                "Oh shit, I can't afford it" if money < 10:
                    $sophP -=2
                    c "Umm... could you cover for me? I forgot my wallet"
                    "Sophie sighs"
                    s "Really? Alright, I'll cover for you this time"
                    "Sophie did not appreciate that..."
                    
 #           hide intro

            menu:
                " "
                
                "How's it going, [s]?" if char >= 15:
                    $sophP+=1
                    s "Pretty good, I've got a lot on my plate, though. Being an RA is taking up more time than I expected it to."
                    "I guess it's worth it, it looks good on my syllabus and I do enjoy helping people. I just hope it won't have a negative effect on my grades. So far so good."
                    "[s] smiles."
                
                "Good food, right?":
                    s "Yeah, it's alright. I do love a burger, but the atmosphere could be improved"
                    "You aren't very good at talking to people... Maybe you should work on your charisma..."
            
                    
            s "Thanks for taking me out to dinner, [c]. It can get lonely eating  alone every day"
            "[s] smiles and gives you a hug"
            hide burgS
            
        
        "Nice restaurant":
            "You go to a nice restaurant."
            show rest1S with fade
            s "Wow, this is such a nice restaurant!"
            c "Yeah, sometimes you have to treat yourself"
            s "Damn straight!"
            "[s] smiles at you"
            "You both sit down and the waiter comes to take your order"
            s "So how's it going, [c]?"
            menu:
                " "
                
                "Pretty good!":
                    c "Pretty good, actually. I'm enjoying the campus, the people and the RA"
                    "You smile as she blushes"
                    $sophP+=2
                    s "I'm happy to hear it!"
                    
                "Not so good":
                    c "It could be better. Even though I like the campus, the classes are pretty rough, but what can you do?"
                    $sophP+=1
                    s "Aww, that's too bad. There are quite a few tutors and Teacher assistants who are willing to help out after class in the classrooms. Maybe you should talk to them?"
                    c "Good idea!"
            "After chatting for 10 minutes, the food arrives"
            hide rest1S
            show restauS with fade
            s "Oh my god, this food is so good!"
            c "I definitely agree. You can't get food this good other places on campus!"
            s "Too bad it's kind of expensive, or else I would've eaten here every day!"
            c "You have to treat your self once in a while, but if you make it a habit, suddenly it won't be as good."
            s "No doubt."
            
            "15 minutes later, the check arrives"
            menu:
                " "
                
                "Offer to pay ( - $50)" if money >= 50:
                    $sophP += 2
                    s "Really, [c]? Are you sure?"
                    c "Of course"
                    "You put down $50."
                    $money -= 50
                "Split the bill ( -$25)":
                    s "So, 50/50 split, right? That'll be $25 each"
                    "You put down $25"
                    $money -= 25
                "Shit, I don't have enough money" if money < 25:
                    $sophP -= 2
                    c "Umm... I forgot my wallet... can you cover for me?"
                    "[s] sighs"
                    s "Fine. But remember your wallet next time"
                    "[s] really didn't like that..."
            hide restauS
    
    $tod+=2
    jump hall
    return
    
label sophBJ:
    show sophBJ:
        xalign 0.75
        yalign 0.5
    
    menu:
        "Where do you cum?"
        
        "In her mouth":
            hide sophBJ
            show sophBJin
        
        "On her face":
            hide sophBJ
            show sophBJout
