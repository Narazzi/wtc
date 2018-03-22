label a_building:
    if tod >= 18:
        "The building is closing"
        jump map
    if examDay == 1:
        c "{i}I had my exam already. I'm done for the day.{/i}"
        jump map
    if tod == 7 or tod == 8 and examDay != 1:
        menu:
            "Do you attend class?"
            
            "Yes":
                jump a_class
                
            "No":
                jump map
    
    else:
        scene classr_ta with fade
        
        menu:
            "What do you want to do?"
            
            "Apply to work as a tutor" if employed == 0: 
    
                if inte < 25:
                    l "I'm sorry, you're not qualified for the position."
                    c "{i}I have to improve my intelligence...{/i}"
                    "You need an intelligence level of 25 to get the job"
                    jump a_building
                
                else:
                    l "Sure, you have been doing very well in class. There will be people here every weekday from 12 to 18. Your pay depends on your results."
                    "You can now work at the classroom every weekday between 12 and 18. You can work once a day, and you choose between 1, 2 or 3 hours of work."
                    $employed = 1
                    jump a_building
                            
            "Work as a tutor" if employed == 1 and worked == 0:
                menu:
                    "How long do you work for?"
                    
                    "1 hour":
                        $workTutor(1)
                        $worked = 1
                        $tod += 2
                        "You work as a tutor for 1 hour. You earn $[earned]. You now have $[money]."
                        jump a_building
                    "2 hours" if tod <= 16:
                        $workTutor(2)
                        $worked = 1
                        $tod += 2
                        "You work as a tutor for 2 hour. You earn $[earned]. You now have $[money]."
                        jump a_building
                    "3 hours" if tod <= 15:
                        $workTutor(3)
                        $worked = 1
                        $tod += 3
                        "You work as a tutor for 3 hour. You earn $[earned]. You now have $[money]."
                        jump a_building
            "Study alone":
                if intTrain >= 5:
                    "You have a headache from studying too much"
                    jump a_building
                "You study for an hour"
                $rngesus()
                if luck == 1:
                    "You don't feel like you learned anything."
                if luck == 2:
                    "You feel like you learned something."
                    $inte+=1
                if luck == 3:
                    "You feel like you learned a lot."
                    $inte+=2
                $intTrain+= 1
                $tod+=1
                jump a_building
                
            "Study with TA" if helpTA == 0:
                "You study with the TA for an hour."
                $helpTA = 1
                $inte+=3
                c "Thank you, Jennifer, I feel like I learned a lot!"
                $tod+=1
                jump a_building
                
            "Leave":
                jump map

    return


    
label a_building_closed:
    "The classrooms are closed..."
    jump map

    
label a_class:
    $rngesus()
    scene classr_ta with fade
    "You attend class"
    
    if day == 27:
        l "I have finished grading your exams."
        "The [l] passes out your graded exams"
        "You scored [examScore[0]]"
        $grading(examScore[0])
        if grade == "A":
            c "{i}Hell yes!{/i}"
        if grade == "B":
            c"{i}B! Pretty good!{/i}"
        if grade == "C":
            c "{i}Hm... a C. Good enough{/i}"
        if grade == "D":
            c "{i}That's too close to comfort... I need to study more.{/i}"
        if grade == "F":
            c "{i}Oh shit... I need to get my act together.{/i}"
        
        l "Let's go through all the answers to the exam."
        "The professor goes through the exam."
        $tod+=3
        jump map
    
    if lectureNr == 0:
        l "Welcome to object-oriented programming. During the course of this semester we’ll look at a lot of different concepts to improve your programming, and, of course, teach you how to take on different challenges."
        l "We'll be focusing  debugging and making your code readable to others, because as you all know, programming is often a project taken on by several programmers."
        l "As this is the first class, we won't be doing much learning, I'll just do a brief introduction of me, as you will be seeing me a lot during this semester."
        "The professor introduces himself, as well as the TA's who will be helping out with grading and tutoring."
    if lectureNr == 1:
        "First week; Designing classes"
    if lectureNr == 2:
        "2nd week; Designing classes"
    if lectureNr == 3:
        "3rd week; Designing classes"
    if lectureNr == 4:
        "4th week; Designing classes"
    if lectureNr == 5:
        "5th week; Designing classes"
    if lectureNr == 6:
        "6th week; Designing classes"
    if lectureNr == 7:
        "7th week; Designing classes"
    if lectureNr == 8:
        "8th week; Designing classes"
        
    if luck == 1:
        "You failed to pay attention..."
    if luck == 2:
        "You paid pretty good attention."
        $inte+= 1 
        "You feel smarter"
    if luck == 3:
        "You understood everything."
        $inte+=2
        "You feel a lot smarter."
    hide classr_a
    $tod += 2
    jump a_building
    return


label exam:
    $examDay = 1
    if exam[0] == 0:
        if inte <= 15:
            c "{i}I've got a bad feeling about this...{/i}"
            $randNum(20,60)
            $examScore[0] = rN
        if inte > 15 and inte <= 25:
            c "{i}This shouldn't be too bad{/i}"
            $randNum(50,80)
            $examScore[0] = rN
        if inte > 25:
            c "{i}This should be easy!{/i}"
            $randNum(70, 100)
            $examScore[0] = rN
        "First exam!"
    if exam[0] == 1:
        "Second exam!"
        if inte <= 30:
            c "{i}I've got a bad feeling about this...{/i}"
            $randNum(20,60)
            $examScore[1] = rN
        if inte > 30 and inte <= 45:
            c "{i}This shouldn't be too bad{/i}"
            $randNum(50,80)
            $examScore[1] = rN
        if inte > 45:
            c "{i}This should be easy!{/i}"
            $randNum(70, 100)
            $examScore[1] = rN
    if exam[0] == 2:
        "Third exam!"
        if inte <= 45:
            c "{i}I've got a bad feeling about this...{/i}"
            $randNum(20,60)
            $examScore[2] = rN
        if inte > 45 and inte <= 60:
            c "{i}This shouldn't be too bad{/i}"
            $randNum(50,80)
            $examScore[2] = rN
        if inte > 60:
            c "{i}This should be easy!{/i}"
            $randNum(70, 100)
            $examScore[2] = rN
    if exam[0] == 3:
        "Fourth exam!"
        if inte <= 50:
            c "{i}I've got a bad feeling about this...{/i}"
            $randNum(20,60)
            $examScore[3] = rN
        if inte > 50 and inte <= 70:
            c "{i}This shouldn't be too bad{/i}"
            $randNum(50,80)
            $examScore[3] = rN
        if inte > 70:
            c "{i}This should be easy!{/i}"
            $randNum(70, 100)
            $examScore[3] = rN
    if exam[0] == 4:
        "Fifth exam!"
        if inte <= 60:
            c "{i}I've got a bad feeling about this...{/i}"
            $randNum(20,60)
            $examScore[4] = rN
        if inte > 60 and inte <= 85:
            c "{i}This shouldn't be too bad{/i}"
            $randNum(50,80)
            $examScore[4] = rN
        if inte > 85:
            c "{i}This should be easy!{/i}"
            $randNum(70, 100)
            $examScore[4] = rN
    $tod+=4
    jump map
    
