##Riley events

label rileyRoom:
    scene rileysRoom
    "Riley room"
    jump hall
    return

label rileySleep:
    scene riSl with fade
    "Riley sleep"
    hide riSl
    jump hall
    return
    
label rileyOut:
    "Riley out"
    jump hall
    return
    
