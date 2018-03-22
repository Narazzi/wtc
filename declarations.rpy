#All declarations
#soph
define metSoph = 0
define sophP = 0
define dailyFS = 0
#chocolate, analbeads, dildo, vibrator, gagball, lube
define sophItems = [0, 0, 0, 0, 0, 0]
#Event limitations
default sophDateDay = 0
default sophHorny = 0
default sDateNo = 0
default sLoc = "roomS"
define sIrr = 0
#emma


#riley
define rIrr = 0

#ariel
default loc = "elsewhere"
default emptyArr = ["", "", "", "", "", "", "", ""]
default itemArr = [0,0,0,0,0,0,0,0]
define itemIArr = ['items/cami.png', 'items/choci.png', 'items/condi.png', 'items/anali.png', 'items/dili.png', 'items/vibi.png', 'items/lubi.png', 'items/gagi.png']
    
define examDay = 0
default exRemind = 0
default dialogue = 0
default rN = 0
define exam = [0, 0, 0, 0, 0]
define examScore = [0, 0, 0, 0, 0]
default intWeek = [0, 0, 0, 0, 0, 0, 0]
default strWeek = [0, 0, 0, 0, 0, 0, 0]
default sDateArr = [0, 0, 0, 0, 0]
default aDateArr = [0, 0, 0, 0, 0]
default rDateArr = [0, 0, 0, 0, 0]
default eDateArr = [0, 0, 0, 0, 0]
define webCLoc = [0, 0,0, 0, 0]
define grade = ""
#0 = pool, 1 = soph, 2 = emma, 3 = riley, 4 = ariel

#Cam, Choc, Condom, analbeads, dildo, vibrator, lube, gagball
default instWC = 0
default lectureNr = 0
define employed = 0
default worked = 0
default earned = 0
#[Soph, Riley, Emma, Ariel, Pool]
default aDateNo = 0
default rDateNo = 0
default eDateNo = 0
define menuIs = 0
default show_quick_menu = True
define dayNr = 1
define strDecay = 0
define intDecay = 0
define audio.knock = "audio/knock.mp3"
default aLoc = "roomA"
default rLoc = "roomR"
default eLoc = "roomE"
default tod = 15
default day = 0
define week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
default today = week[day]
define intro = 1
#daily limits

define dailyFA = 0
define dailyFR = 0
define dailyFE = 0
define helpTA = 0
define charTrain = 0
define strTrain = 0
define intTrain = 0
define dinnerS = 0


#rng
define luck = 0



define money = 100
init python:
    locations = ["Hall2", "hall", "roomA", "roomS", "roomE", "roomR", "room", "a_class", "b_class", "c_class", "court", "pool", "mall_1", "mall_2", "dorm", "dining", "sexstore", "clothesStore"]
    flash = Fade(.075, 0, .075, color="#FFF")


define inte = 5
define stre = 5
define char = 5

#Webcam installed
default wcA = 0
default wcS = 0
default wcE = 0
default wcR = 0

#Character points
define arielP = 0
define emmaP = 0
define rileyP = 0

#Met characters
define metAriel = 0
define metEmma = 0
define metRiley = 0

define a = Character("Ariel", color="#a100cf")
define s = Character("Sophia", color="#0051ca") 
define e = Character("Emma", color="#c30000")
define r = Character("Riley", color="#27ce00")
define c = Character("[chara]", color ="#00fff0")
define l = Character("Professor", color = "FFF")
define d = Character("Daisy", color="#2c005a")
define p = Character("Pam", color="#002b9a")
define recept = Character("Receptionist", color="#006975")
#animations

image bjsanim:
    "events/soph/bj/bjs1.png"
    pause 0.2
    "events/soph/bj/bjs2.png"
    pause 0.2
    "events/soph/bj/bjs3.png"
    pause 0.2
    "events/soph/bj/bjs4.png"
    pause 0.2
    "events/soph/bj/bjs3.png"
    pause 0.2
    "events/soph/bj/bjs2.png"
    pause 0.2
    "events/soph/bj/bjs1.png"
    repeat
    

image sophrtalkk:
    "images/character/soph/sophrtalk1.png"
    pause 1
    "images/character/soph/sophrtalk2.png"
    pause 1
    "images/character/soph/sophrtalk3.png"
    pause 1
    "images/character/soph/sophrtalk4.png"
    pause 1
    "images/character/soph/sophrtalk2.png"
    pause 1
    "images/character/soph/sophrtalk5.png"
    repeat
    
    
image sophbeadtalk:
    "images/character/soph/sophanalb5.png"
    pause 1
    "images/character/soph/sophanalb6.png"
    pause 1 
    "images/character/soph/sophanalb7.png"
    pause 1
    "images/character/soph/sophanalb8.png"
    pause 1
    "images/character/soph/sophanalb6.png"
    pause 1
    "images/character/soph/sophanalb8.png"
    pause 1
    "images/character/soph/sophanalb7.png"
    pause 1
    repeat
    
    
    
image pornsc1:
    "pc/porn/sc1/mast01.png"
    pause 1
    "pc/porn/sc1/mast02.png"
    pause 1
    "pc/porn/sc1/mast03.png"
    pause 1
    block:
        "pc/porn/sc1/mast04.png"
        pause 0.7
        "pc/porn/sc1/mast05.png"
        pause 0.7
        repeat 4
    block:
        "pc/porn/sc1/mast06.png"
        pause 0.6
        "pc/porn/sc1/mast07.png"
        pause 0.6
        "pc/porn/sc1/mast08.png"
        pause 0.6
        repeat 4
    block:
        "pc/porn/sc1/mast09.png"
        pause 0.4
        "pc/porn/sc1/mast10.png"
        pause 0.4
        repeat 6
    block:
        "pc/porn/sc1/mast11.png"
        pause 0.2
        "pc/porn/sc1/mast12.png"
        pause 0.2
        "pc/porn/sc1/mast13.png"
        pause 0.2
        repeat 5
    block:
        "pc/porn/sc1/mast15.png"
        pause 0.2
        "pc/porn/sc1/mast16.png"
        pause 0.2
        "pc/porn/sc1/mast17.png"
        pause 0.2
        repeat 10
    
    

#Images for scene

image bjsophscene = Movie(channel="soph", play="events/soph/bj/sophbj3.m2t")
image beadS2 = "character/soph/sophanalb1.png"
image beadS1 = "character/soph/sophanalb2.png"
image beadS3 = "character/soph/sophanalb3.png"

image apool1 = "maps/pool/apool1.png"
image apool2 = "maps/pool/apool2.png"
image apool3 = "maps/pool/apool3.png"
image apool4 = "maps/pool/apool4.png"
image apool5 = "maps/pool/apool5.png"
image apool = "maps/pool/apool.png"
image epool = "maps/pool/epool.png"
image rpool = "maps/pool/rpool.png"
image spool = "maps/pool/spool.png"
image introA = "character/intro/ariel.png"
image introR = "character/intro/riley.png"
image introE = "character/intro/emma.png"
image introS = "character/intro/sophia.png"
image poolDress = "maps/pool/dressPool.png"
image room = "maps/dorm/room.png"
image intro = "fade.png"
image meetS = "events/meetSoph.png"
image relat = "gui/menu/relations.png"
image campus = "maps/campus.png"
image pcbg = "gui/pcscreen.png" 
image hall2 = "maps/dorm/hall2.png"
image pool = "maps/pool/pool.png"
image hallbg = "maps/dorm/hall.png"
image rileysRoom = "maps/dorm/rileyRoom.png"
image emmasRoom = "maps/dorm/emmaRoom.png"
image arielsRoom = "maps/dorm/arielRoom.png"
image sophsRoom = "maps/dorm/sophRoom.png"
image riley = "character/riley.png"
image soph = "character/soph.png"
image emma = "character/emma.png"
image ariel = "character/ariel.png"
image rileyf = "character/rileyface.png"
image dota = "events/dota.jpg"
image dormMS = "events/dormintS.png"
image dormMR = "events/dormintR.png"
image dormME = "events/dormintE.png"
define hemmeligpassord = "072597"
default secunlock = 1
image dormMA = "events/dormintA.png"
image dormMC = "events/dormintC.png"
image dormMaft = "events/dormintafter.png"
image dormMAf = "events/dormintm.png"
image dormTS = "events/dormts.png"
image dormTR = "events/dormtr.png"
image dormTA = "events/dormta.png"
image dormTE = "events/dormte.png"
image arSl = "maps/dorm/arielSleep.png"
image emSl = "maps/dorm/emmaSleep.png"
image riSl = "maps/dorm/rileySleep.png"
image soSl = "maps/dorm/sophSleep.png"
image sophbj = "character/sophbj.png"
image sophbjin = "character/sophbjin.png"
image sophbjout = "character/sophbjout.png"
image sophkiss = "character/sophkiss.png"
image restauS = "maps/restauS.png"
image restauA = "maps/restauA.png"
image restauR = "maps/restauR.png"
image restauE = "maps/restauE.png"
image burgS = "maps/burgerS.png"
image burgA = "maps/burgerA.png"
image burgE = "maps/burgerE.png"
image burgR = "maps/burgerR.png"
image rest1S = "maps/restau1S.png"
image rest1R = "maps/restau1R.png"
image rest1A = "maps/restau1A.png"
image rest1E = "maps/restau1E.png"
image Sroomday = "maps/dorm/sophinroomday.png"
image Sroomeve = "maps/dorm/sophinroomeve.png"
image Rroomeve = "maps/dorm/rilinroomdeve.png"
image Rroomday = "maps/dorm/rilinroomday.png"
image Eroomday ="maps/dorm/eminroomdeve.png" 
image Eroomeve = "maps/dorm/eminroomeve.png"
image Aroomday = "maps/dorm/ariinroomday.png"
image Aroomeve = "maps/dorm/ariinroomeve.png"
image classr_a = "maps/classmap.png"
image classr_ta = "maps/classta.png"
image mallScene = "maps/mall/mall.png"
image psychRec = "maps/mall/psychRec.png"
image clothesS = "maps/mall/clothSP.png"
image clothSoph = "maps/mall/clothsSS.png"
image sexSR = "maps/mall/sexSR.png"
image sexS = "maps/mall/sexSD.png"

#Sexual images



image poolS1= "pc/webc/pool/5.png"
image poolS2 ="pc/webc/pool/6.png"
image poolS3 ="pc/webc/pool/7.png"
image poolS4 ="pc/webc/pool/8.png"
image poolS5 ="pc/webc/pool/9.png"
image poolS6 ="pc/webc/pool/10.png"
image poolS7 ="pc/webc/pool/11.png"
image poolS8 ="pc/webc/pool/12.png"
image poolS9 ="pc/webc/pool/13.png"
image poolS10= "pc/webc/pool/14.png"
image poolS11 ="pc/webc/pool/15.png"
image poolS12 ="pc/webc/pool/16.png"
image poolS13 ="pc/webc/pool/17.png"
image poolS14 ="pc/webc/pool/18.png"
image poolS15 ="pc/webc/pool/19.png"

image bjswait = "events/soph/bj/bjs0.png"
image bjscum = "events/soph/bj/bjscum.png"
image bjsafter = "events/soph/bj/afterfacial.png"
image bjscloth = "events/soph/bj/bjscloth.png"
image sophkiss = "events/soph/sophkiss.png"
image sophaftkiss = "events/sopth/sophafterkiss.png"


#image
