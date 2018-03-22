##Ariel events

label arielRoom:
    scene arielsRoom
    "Ariel room"
    jump hall
    return
    
label arielSleep:
    scene arSl with fade
    "ariel sleep"
    hide arSl
    
    jump hall
    return
    
label arielOut:
    "Ariel is out"
    "You know?"
    jump hall
    return
