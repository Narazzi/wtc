#                           0            1        2              3               4               5       6               7               8               9         10       11           12      13              14      15              16              17
#    locations = ["Hall2", "hall", "roomA", "roomS", "roomE", "roomR", "room", "a_class", "b_class", "c_class", "gym", "pool", "mall_1", "mall_2", "dorm", "dining", "sexstore", "clothesStore"]
screen aRoom:
    imagemap:
        ground "maps/dorm/arielRoom.png"
        hover "maps/arielRoom.png"
        
screen eRoom:
    imagemap:
        ground "maps/dorm/emmaRoom.png"
        hover "maps/emmaRoom.png"

screen sRoom:
    imagemap:
        ground "maps/dorm/sophRoom.png"
        hover "maps/dorm/sophRoom.png"

screen rRoom:
    imagemap:
        ground "maps/dorm/rileyRoom.png"
        hover "maps/dorm/rileyRoom.png"

screen relations:
    modal True
    imagemap:
        ground "gui/menu/relations.png"
        hover "gui/menu/relations_hover.png"

        hotspot(850,230,40,40)clicked [Hide("relations")]
        
        hbox xalign 0.38 yalign 0.545:
            text "{b}[arielP]{/b}"
        hbox xalign 0.46 yalign 0.545:
            text  "{b}[emmaP]{/b}"
        hbox xalign 0.54 yalign 0.545:
            text  "{b}[rileyP]{/b}"
        hbox xalign 0.620 yalign 0.545:
            text  "{b}[sophP]{/b}"
            
screen playerStats:
    modal True
    imagemap:
        ground "gui/menu/stat.png"
        hover "gui/menu/stathover.png"
        
        hotspot(745,102,60,60) clicked Hide('playerStats')

        text "{b}{size=+20}[stre]{/size}{/b}":
            xalign 0.575
            yalign 0.35
        text "{b}{size=+20}[inte]{/size}{/b}":
            xalign 0.575
            yalign 0.48
        text "{b}{size=+20}[char]{/size}{/b}":
            xalign 0.575
            yalign 0.61
            
screen inventory:
    $invent()
    modal True
    imagemap:
        
        ground "gui/menu/items.png"
        hover "gui/menu/items_hover.png"

        hotspot(999,195,40,40) clicked Hide("inventory")                    
        
        hbox:
            xpos 240
            ypos 235
            spacing 22
            for x in emptyArr:
                if x != "":
                    image x
            
        hbox:
            xpos 300
            ypos 290
            spacing 80
            for x in itemArr:
                if x !=0:
                    text "{b}[x]{/b}":
                        min_width 22
                    
###Places

#Campus map

screen campMap:
    modal False
    imagemap:
        ground 'maps/campus.png'
        hover 'maps/campus_hover.png'

        hotspot(950,231,301,448) action Jump ('mall')
        
        if tod>= 18 or day >= 5:
            hotspot(555,216,241,408) action Jump ('a_building_closed')
        else:
            hotspot(555,216,241,408) action Jump ('a_building')
        hotspot(303,218,209,295) action Jump ('cominglater')
        #hotspot(37,511,295,201) action Jump ('court')
        if tod >= 23 or tod <= 7:
            hotspot(175,530,160,175) action Jump ('poolclosed')
        else:
            hotspot(175,530,160,175) action Jump ('pool')
        hotspot(15,299,155,169) action Jump ('hall')
        hotspot(23,211,231,130) action Jump ('cominglater')
        hotspot(620,90,136,69) action Jump ('cominglater')
        hotspot(180,36,271,136) action Jump ('cominglater')

        #hotspot(950,231,301,448) action Jump ('mall')
        #hotspot(555,216,241,408) action Jump ('a_class')
        #hotspot(303,218,209,295) action Jump ('b_class')
        #hotspot(37,511,295,201) action Jump ('court')
        #hotspot(175,530,160,175) action Jump ('pool')
        #hotspot(15,299,155,169) action Jump ('hall')
        #hotspot(23,211,231,130) action Jump ('dininghall')
        #hotspot(620,90,136,69) action Jump ('dining6')
        #hotspot(180,36,271,136) action Jump ('c_class')


        
        
#Mall

screen mallScreen:
    imagemap:
        ground "maps/mall/mall.png"
        hover "maps/mall/mall_hover.png"
              
        
        hotspot(614,558,55,128) clicked Jump("map")
        hotspot(375,158,270,152) clicked Jump("psych")
        hotspot(875,114,70,265) clicked Jump("sexStore")
        hotspot(990,50,175,450) clicked Jump("clothesStore")
        
        
        
# Hall-map screen

screen hallway:
    modal False
    imagemap:
        ground "maps/dorm/hall.png"
        hover "maps/dorm/hall_hover.png"
        
        
        
        hotspot(550,257,100,185) clicked Jump("room")
        if metSoph == 0:
            hotspot(380,200,35,285) clicked Jump("stranger")
        if metEmma == 0:
            hotspot (232, 110, 62, 463) clicked Jump("stranger")
        if metAriel == 0:
            hotspot(840,205,35,280) clicked Jump("stranger")
        if metRiley == 0:
            hotspot(965,115,70,455) clicked Jump("stranger")
            
        if metSoph == 1:
            if sLoc == 'roomS':
                hotspot(380,200,35,285) clicked Jump("sophieRoom")
            if sLoc == "sleep":
                hotspot(380,200,35,285) clicked Jump("sophAsleep")
            if sLoc != "roomS" and sLoc != "sleep":
                hotspot(380,200,35,285) clicked Jump("sophOut")
        if metEmma == 1:
            hotspot (232, 110, 62, 463) clicked Jump("emmaRoom")

            #hotspot (232, 110, 62, 463) clicked Jump("cominglaterhall")
            #if eLoc == "roomE":
                
                #hotspot (232, 110, 62, 463) clicked Jump("emmaRoom")
            #if eLoc == "sleep":
            #    hotspot (232, 110, 62, 463) clicked Jump("emmaSleep")
            #if eLoc != "roomE" and eLoc != "sleep":
              #  hotspot (232, 110, 62, 463) clicked Jump("emmaOut")
        if metAriel == 1:
            hotspot(840,205,35,280) clicked Jump("arielRoom")

            #hotspot(840,205,35,280) clicked Jump("cominglaterhall")
          #  if aLoc == "roomA":
            #    hotspot(840,205,35,280) clicked Jump("arielRoom")
            #if aLoc == "sleep":
                #hotspot(840,205,35,280) clicked Jump("arielSleep")
            #if aLoc != "roomA" and aLoc != "sleep":
                #hotspot(840,205,35,280) clicked Jump("arielOut")
                
        if metRiley == 1:
            hotspot(965,115,70,455) clicked Jump("rileyRoom")
            
            #hotspot(965,115,70,455) clicked Jump("cominglaterhall")
            #if rLoc == "roomR":
                #hotspot(965,115,70,455) clicked Jump("rileyRoom")
            #if rLoc == "sleep":
                #hotspot(965,115,70,455) clicked Jump("rileySleep")
            #if rLoc != "roomR" and rLoc != "sleep":
              #  hotspot(965,115,70,455) clicked Jump("rileyOut")

        hotspot(750,325,60,25) clicked Jump("hall2")

screen porno:
    modal True
    $ x=random.randint(1,3)
    $x=1
    imagemap:
        if x == 1:
            ground "pc/porn/sc1.png"
        if x == 2:
            ground "pc/porn/sc2.png"
        if x == 3:
            ground "pc/porn/sc3.png"
            
            
        hover "pc/porn/hover.png"
        hotspot(1230,0,50,25) clicked Jump('computer')
        
        
        

screen pcsc:
    modal False
    imagemap:
        ground "gui/pcscreen.png"
        hover "gui/pcscreen_hover.png"
        
        hotspot(1200, 680, 150,150)clicked Jump("secretP")
        hotspot(28,18,105,105) clicked Jump("folder")
        hotspot(145,18,105,105) clicked Jump("shop")
        hotspot(28,140,105,105) clicked Jump("porn")
        hotspot(145,140,105,105) clicked Jump("webcam")
        hotspot(28,270,105,105) clicked Jump("patreon")
        hotspot(0,680,105,105) clicked Jump("shutdown")
        
        hbox xalign 0.99 yalign 0.99:
            text "{b}[tod]:00{/b}"

screen webcam:
    $wcCount()
    imagemap:
        if instWC == 0:
            ground "gui/wcbg.png"
        elif instWC == 1:
            ground "gui/webc1.png"
        elif instWC == 2:
            ground "gui/webc2.png"
        elif instWC == 3:
            ground "gui/webc3.png"
        elif instWC == 4:
            ground "gui/webc4.png"
        elif instWC == 5:
            ground "gui/webcam.png"
        hover "gui/webcamhover.png"
        hotspot(1175, 59, 45,45) clicked Jump("computer")
        if instWC == 1:
            hotspot(258,102,155,155) clicked Jump("webC1")
        if instWC == 2:
            hotspot(258,102,155,155) clicked Jump("webC1")
            hotspot(460,102,155,155) clicked Jump("webC2")
        if instWC == 3:
            hotspot(258,102,155,155) clicked Jump("webC1")
            hotspot(460,102,155,155) clicked Jump("webC2")
            hotspot(665,102,155,155) clicked Jump("webC3")
        if instWC == 4:
            hotspot(258,102,155,155) clicked Jump("webC1")
            hotspot(460,102,155,155) clicked Jump("webC2")
            hotspot(665,102,155,155) clicked Jump("webC3")
            hotspot(866,102,155,155) clicked Jump("webC4")
        if instWC == 5:
            hotspot(258,102,155,155) clicked Jump("webC1")
            hotspot(460,102,155,155) clicked Jump("webC2")
            hotspot(665,102,155,155) clicked Jump("webC3")
            hotspot(866,102,155,155) clicked Jump("webC4")
            hotspot(258, 282,155,155) clicked Jump("webC5")
            
#Pool 

screen webcVid:
    modal True
    imagemap:
        ground "gui/webcvid.png"
        hover "gui/webcvidh.png"
        
        hotspot(1040, 55, 40, 40) clicked [Hide ('webcVid'), Jump('computer')]
    

screen poolDress:
    imagemap:
        ground "maps/dressPool.png"
        hover "maps/dresspoolh.png"
        
        hotspot(550,130,75,75) clicked Jump ("camInstallPool")
        hotspot(750,130,75,75) clicked Jump ("camInstallPFail")
        hotspot(95,475,75,75) clicked Jump ("camInstallPFail")
        hotspot(1000,500,75,75) clicked Jump ("camInstallPFail")
