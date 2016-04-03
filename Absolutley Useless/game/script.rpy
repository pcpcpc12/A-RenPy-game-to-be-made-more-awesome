# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image theend = Text("{color=#f00f00}{size=80}This text thing was code copy pasted from...{/size}{/color}", xalign=0.5, yalign=0.5)
image theend2 = Text("{color=#f00f00}{size=80}KomiTsuku on the Lemma Soft forums!{/size}{/color}", xalign=0.5, yalign=0.5)
image theend3 = Text("{color=#f00f00}{size=80}Thanks for playing! You can add stuff to this at my github repo for this game!!{/size}{/color}", xalign=0.5, yalign=0.5)
# Declare characters used by this game.
define p = Character('pcpcpc12', color="#c8ffc9")
define r = Character('Renny', color="#c8ffc0")


# The game starts here.
label start:

    p "You've created a new Ren'Py game."

    r "Once you add a story, pictures, and music, you can release it to the world!"

    r "Well, what do we do?"

    p "I dunno..."

    p "I WANT a visual editor for Renpy' now!"
 
    r "Not my fault, I'm only a representation of Renpy'!"
 
    p "Well ask then!"

    r "DON'T YOU SAY THAT! WE'RE IN A VISUAL NOVEL DUMBASS!"

    p "Nevermind..."  

    r "................."
    
    p "Hey you! Go to the game's github repo and make this epic!"
    
    r "Also try the snapshots there!"
    
    "Really, there was nothing to do!!!"
    
    p "Roll the credits...."
    
    p " HELLO? CREDITS! You're a picture wich was already initalized in the game!"


    return
