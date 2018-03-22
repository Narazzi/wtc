

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

    
#Special thanks to ToxicTechnophile for ideas and critique

# The game starts here.
label splashscreen:
    scene splash
    with Pause(9)
    return

label start:
    show intro
    "First and foremost, thank you for taking an interest in my game. I hope you enjoy it."
    "This game contains imagery of a sexual nature. By playing this game, you are agreeing that you are over 18 years  or your countries equivalent."
    menu:
        "Told you I would ask you."
        
        "I am over 18 or my countries equivalent":
            "Excellent. Let's go!"
     
        "I am not over 18 or my countries equivalent":
            return
    $ chara = renpy.input("First thing's first. What's your name?")
    $ chara = chara.strip() 
    if chara  == "":
        "That's a shit name, let's call you {color=#00fff0}Peter{/color}"
        $ chara = "Peter"
    "Welcome to College, {color=#00fff0}[c]{/color}!"
    
    "Please keep in mind: This game is still in development. There are certain areas that are unavailable, and the characters' storylines are not yet completed."
    "As any college student, you will have to manage your time wisely. If you don't go to class and study, you will fail your exams, and eventually drop out. This will end the game prematurely"
    "Also, you are a single student, which means you will also be looking for a better half. There are four girls in your dorm, and although the college probably has more students, your lovelife will revolve around them.{size=-15}No it's not lazy{/size}"
    "The semester lasts 120 days, and there are several different endings."
    "First, let me introduce you to the residents."
    scene introA with dissolve
    "This is {color=#a100cf}[a]{/color}."
    "[a] is 22 years old. She is an introvert, and with that comes shyness and a lot of silence. She doesn't say much, most of her words are on the page in the form of songs."
    scene introS
    "This is {color=#0051ca}[s]{/color}."
    "[s] is 21 years old. She is outgoing and proper. Don't be afraid to talk to her, as she is a social person, but be careful with your words, if you say something improper, she may dislike you."
    scene introE
    "This is {color=#c30000}[e]{/color}."
    "[e] is 19 years old. She is very outgoing, and adores the ganguro style. If you hear yelling in the dorm, it is near guaranteed it is [e]. She is very loud, and doesn't take things too seriously."
    scene introR
    "This is {color=#27ce00}[r]{/color}."
    "[r] is 23 years old. She is a laid back woman who is very sexual. [r] is not very talkative, but when she does talk, it's not unlikely she will be saying something dirty."
    scene hall
    "You should head to your room. It's straight ahead."
    #"Thank you very much for playing my game. If you want to support me and this game, visit www.patreon.com/norezza"
    jump hall
    
    
label cominglater:
    "This is coming in a later update"
    jump map
    
label cominglaterhall:
    scene rileyRoom with fade
    "This is coming in a later update"
    hide rileyRoom
    jump hall
    
label lateNight:
    jump room
    return
