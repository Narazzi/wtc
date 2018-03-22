label laydwn:
    c "aah... finally"
    scene intro with fade
    play sound knock 
    c "zzzz"
    stop sound
    c "Hm?"
    play sound knock
    stop sound
    jump meetingS
    
    return
    
label gaming:
    c "Finally time to defend some ancients. 2."
    scene dota with fade
    c "IDI NAHUY CYKA BLYAT"
    c "God damn noobs..."
    play sound knock
    c "I'm like freaking Dendi, hitting all my hooks"
    stop sound
    "There is a knock on the door."
    hide dota
    jump meetingS
    
label meetingS:
    scene meetS with fade
    "You open the door."
    "A tall girl enters your room. She seems somewhat stressed, but smiles at you."
    $intro = 3
    
    menu:
        s "Hi!"
        
        "Hi!":
            $ sophP = sophP
            
            s "I'm [s], I live in the room next to you. I saw you just got here!"
            s "Nice to meet you.  I'm the Resident Assistant in this dorm, so I figured I should come greet you and give you some information!"
            s "This is a map over the campus." 
            "[s] gives you a map."
            $map = 1
            s "This dorm has common area down the hall. We are having a meeting at 16:00 today, make sure you're there okay?"
            s "There are a lot of new people arriving today, so I have to go, but if you have any questions, please don't hesitate to ask.My room is right next to yours, so just knock."
            c "Okay, thank you, [s]"
        "Hi, I'm [c]":
            $ sophP = sophP+1
            s "Nice to meet you, [c], I'm [s]. I'm the Resident Assistant in this dorm, so I figured I should come greet you and give you some information!"
            c "Great!"
            s "This is a map over the campus." 
            "[s] gives you a map."
            $map = 1
            s "This dorm has common area down the hall. We are having a meeting at 16:00 today, make sure you're there okay?"
            s "There are a lot of new people arriving today, so I have to go, but if you have any questions, please don't hesitate to ask.My room is right next to yours, so just knock."
            c "Okay, thank you, [s]"
    "[s] goes back to her room."
    scene intro with fade 
    "1 hour later."
            
            
    jump dormMeet
        
    return
    

label dormMeet:

    $tod +=1
    scene dormMS with fade
    s "Hi everyone. I've already introduced myself, but I guess I'll repeat the introduction. My name is [s], and I am your RA. I am 21, and I'm majoring in communication."
    s "My hobbies are volleyball and that's about it. I don't really have time for other hobbies, being an RA and studying takes up most of my time, hah. I wouldn't trade it though!"
    s "I figured we could have a sort of a meet-and-greet, since we're a pretty small dorm."
    s "There are other floors to this dorm, but generally speaking, people usually don't go to the other floors."
    "Convenient, I know."
    s "Anyhow, since it's just the five of us, how about we do an introduction round? I've already done mine."
    s "[c], you first!"
    scene dormMC with fade
    c "Okay, my name is [c], and I'm 20 years old. I am majoring in computer science. My hobbies are playing games and... well, that's about it. I'm looking forward to the university experience."
    s "Okay, [a] next!"
    scene dormMA with fade
    a "*Sigh* I'm [a]. I'm 22 years old, majoring in songwriting, and my hobbies are playing different instruments and writing songs. I mainly play guitar."
    s "Excellent, now, [e]"
    scene dormME with fade
    e "Hey guys! I'm [e]! I'm 19 years old, majoring in graphic design, and my hobbies include make-up, taking pictures and editing pictures!"
    s "Loving the energy, [e]! Last one out is [r]"
    scene dormMR with fade
    r "My name is [r], I'm 23 years old and I'm majoring in video production. My hobbies are watching movies and peoplewatching."
    scene dormMaft with fade
    s "Nice to meet you all. As you know, I have an open-door policy, so if any of you have any questions, feel free to ask them. Now, that's all I had planned, but feel free to mingle or to go back to your rooms!"
    jump afterDormMeet
    
label afterDormMeet:
    scene dormMAf with fade
    menu:
        "What do you want to do?"
        
        "Talk to [e]" if metEmma == 0:
            jump talkEf
            
        "Talk to [s]" if metSoph == 0:
            jump talkSf
        
        "Talk to [a]" if metAriel == 0:
            jump talkAf
            
        "Talk to [r]" if metRiley == 0:
            jump talkRf
            
    if metEmma + metSoph + metAriel + metRiley == 4:
        c "Well, I've said hi to everyone. Might as well go back to my room"
        $tod += 1
        $intro = 100
        jump room
    
    
label talkEf:

    $metEmma = 1

    "You walk up to the spirited ganguro girl who introduced herself as Emma." 
    scene dormTE
    c "{i}An energetic girl, with grey hair and tan skin. I wouldn't mind me some of that...{/i}"
    c "{i}as long as the makeup won't ruin my bedsheets...{/i}"
    menu:
        e "Nice to meet you, [c]"
        
        "Nice to meet you too":
            c "Nice to meet you too, [e]"
            $emmaP += 1
        "Holy crap, you're stunning!":
            "Emma blushes"
            e "Well, you're direct. Thank you"
            $emmaP += 2
        "What's up with the makeup?":
            e "It's my style. Deal with it."
            "[e] walks away"
            $emmaP -= 1
    jump afterDormMeet
    
label talkSf:
    $metSoph = 1
    scene dormTS
    c "Hi again, [s]."
    s "Hi, [c]. Is there anything I can do for you?"
    menu:
        "Nothing, just wanted to say hi":
            s "Oh, well. Hi."
            
    jump afterDormMeet
    
label talkAf:
    $metAriel = 1
    scene dormTA
    c "Nice to meet you, [a]."
    a "Nice to meet you too, [c]."
    
    jump afterDormMeet
    
label talkRf:
    $metRiley = 1
    scene dormTR
    c "Nice to meet you, [r]"
    r "Nice to meet you too, [c]"
    
    jump afterDormMeet
    

