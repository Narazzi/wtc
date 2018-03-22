

label hall:
    $timeLoc()
    scene hallbg
    call screen hallway
    
label stranger:
    show hall
    "I can't just knock on some random persons door..."
    jump hall
    return
    
    
    
label hall2:
    scene hall2 
    
    if intro == 1:
        "This is the common area. Not much to do here at the moment... Nobody's here."
        menu:
            "Go back":
                jump hall
    menu:
        "What do you want to do?"
        
        "Go back":
            hide hall2
            jump hall
        "Relax":
            $tod += 1
            hide hall2
            jump hall2
    return
    
label rileyStudy:
    r "I'd love to"
    "You and Riley study for an hour"
    if inte <= 20:
        r "You haven't really studied a lot, have you?"
        "[r] isn't impressed with your intelligence... Relationship decreased"
        
label rileyInRoom:
    scene rileyRoom
    menu:
        r "What's up?"
        
        "Do you want to study together?":
            r "Sure"
            "You spend an hour studying with Riley"
            
        "Do you want to grab a bite to eat?":
            r "Sure"
            "You go with Riley to the dining hall"
            hide rileyRoom
            jump dining
            
        "I forgot":
            r "... Okay?"
            hide rileyRoom
            jump hall
            
    return
    
    
label sophSleep:
    "[s] is sleeping"
    jump hall
