### Soph
label sophDate:
    
    if sDateNo == 1:
        jump sophD1
    if sDateNo == 2:
        jump sophD2
    if sDateNo == 3:
        jump sophD3
    if sDateNo == 4:
        jump sophD4
    if sDateNo == 5:
        jump sophD5
    else:
        menu:
            "What do you do?"
            
            "Dinner and a movie":
                jump sophD1
            "Go for a walk":
                jump sophD2
            "Picnic":
                jump sophD3
            "Go shopping":
                jump sophD4
            "Go to the beach":
                jump sophD5
    #date 1
    #dinner & movie 
    #date 2
    #picnic
    #date 3
    #walk
    #date 4
    #mall
    #date 5
    #beach
    
    "You and Soph go on a date"
    
label sophD1:
    $sDateArr[0] = 1
    "Dinner & Movie"
label sophD2:
    $sDateArr[1] = 1
    "Walk"
label sophD3:
    $sDateArr[2] = 1
    "Picnic"
label sophD4:
    $sDateArr[3] = 1
    "Go shopping"
label sophD5:
    "Go to the Beach"
    $sDateArr[4] = 1
    
#### Ariel

label aDate:
    
    if aDateNo == 1:
        jump aD1
    if aDateNo == 2:
        jump aD2
    if aDateNo == 3:
        jump aD3
    if aDateNo == 4:
        jump aD4
    if aDateNo == 5:
        jump aD5
    else:
        menu:
            "What do you do?"
            
            "Dinner and a movie":
                jump aD1
            "Go for a walk":
                jump aD2
            "Picnic":
                jump aD3
            "Go shopping":
                jump aD4
            "Go to the beach":
                jump aD5
    #date 1
    #dinner & movie 
    #date 2
    #picnic
    #date 3
    #walk
    #date 4
    #mall
    #date 5
    #beach
    
    "You and ariel  go on a date"
    
label aD1:
    $aDateArr[0] = 1
    "Dinner & Movie"
label aD2:
    $aDateArr[1] = 1
    "Walk"
label aD3:
    $aDateArr[2] = 1
    "Picnic"
label aD4:
    $aDateArr[3] = 1
    "Go shopping"
label aD5:
    "Go to the Beach"
    $aDateArr[4] = 1
    
    
### Emma

label eDate:
    
    if eDateNo == 1:
        jump eD1
    if eDateNo == 2:
        jump eD2
    if eDateNo == 3:
        jump eD3
    if eDateNo == 4:
        jump eD4
    if eDateNo == 5:
        jump eD5
    else:
        menu:
            "What do you do?"
            
            "Dinner and a movie":
                jump eD1
            "Go for a walk":
                jump eD1
            "Picnic":
                jump eD1
            "Go shopping":
                jump eD1
            "Go to the beach":
                jump eD1
    #date 1
    #dinner & movie 
    #date 2
    #picnic
    #date 3
    #walk
    #date 4
    #mall
    #date 5
    #beach
    
    "You and emma  go on a date"
    
label eD1:
    $eDateArr[0] = 1
    "Dinner & Movie"
label eD2:
    $eDateArr[1] = 1
    "Walk"
label eD3:
    $eDateArr[2] = 1
    "Picnic"
label eD4:
    $eDateArr[3] = 1
    "Go shopping"
label eD5:
    "Go to the Beach"
    $eDateArr[4] = 1
    
    
### Riley

label rDate:
    
    if rDateNo == 1:
        jump rD1
    if rDateNo == 2:
        jump rD2
    if rDateNo == 3:
        jump rD3
    if rDateNo == 4:
        jump rD4
    if rDateNo == 5:
        jump rD5
    else:
        menu:
            "What do you do?"
            
            "Dinner and a movie":
                jump rD1
            "Go for a walk":
                jump rD2
            "Picnic":
                jump rD3
            "Go shopping":
                jump rD4
            "Go to the beach":
                jump rD5
    #date 1
    #dinner & movie 
    #date 2
    #picnic
    #date 3
    #walk
    #date 4
    #mall
    #date 5
    #beach
    
    "You and riley go on a date"
    
label rD1:
    $rDateArr[0] = 1
    "Dinner & Movie"
label rD2:
    $rDateArr[1] = 1
    "Walk"
label rD3:
    $rDateArr[2] = 1
    "Picnic"
label rD4:
    $rDateArr[3] = 1
    "Go shopping"
label rD5:
    "Go to the Beach"
    $rDateArr[4] = 1
    
