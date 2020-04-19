# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Villain")
define h = Character("Henchmen")
define s = Character("Superhero")

default chosen_bait = ""
default chosen_trap = ""
default pool = False
default pitfall = False
default ray = False
default walls = False
default no = False
default spikes = False
default pasta = False
default sharks = False
default fire = False
default water = False
default chicken = False
default dino = False
default trumpet = False
default pillow = False

#==============================================
'''============================================
CODE FOR RESEARCH GAME BELOW \/ \/ \/ \/ \/ \/   WARNING WARNING WARNING =======================================================================
===============================================
'''#===========================================

##### The game screen
screen game_scr:

    side "c b r":

        viewport id "vp":
            mousewheel True
            add "twitter main.jpg" zoom 1.1

        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")

    #  Disable cursor and enter keys
    key "K_LEFT" action Hide("nonexistent_screen")
    key "K_RIGHT" action Hide("nonexistent_screen")
    key "K_UP" action Hide("nonexistent_screen")
    key "K_DOWN" action Hide("nonexistent_screen")
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")

    # Timer ===
    # Returns "" every second, or returns "end" if time is up
    timer 1 action [Return(""), If( game_timer<1, Return("end"), SetVariable("game_timer", game_timer-1) ) ] repeat True
    
    text "{color=#000000}Automatic Windows Update in [game_timer] seconds{/color}" size 25 xpos 10 ypos 10


    for popup in sorted(all_popups, reverse=True):
        if popup["showImage"]:
            $ i = popup["popup_num"] - 1
            button:

                background None
                add popup["img"]
                xpos popup["x"]
                ypos popup["y"]
                anchor (0.5, 0.5)

                # hides the popup on click so it won't be redrawn
                action If (i == -1, SetDict(all_popups[popup["popup_num"] ], "showImage", False),
                    If (all_popups[i]["showImage"] == False,
                        SetDict(all_popups[popup["popup_num"] ], "showImage", False)))

init:
    image img1:
        "popup.png"
        zoom 1

label research_game:

    $ all_popups = []
    $ popup_images = ["img1"]

    # Before start the game, let's set the timer
    $ game_timer = 20

    # Shows the game screen
    show screen game_scr
    "Damnit, I really shouldn't have installed all those viruses for fun."
    "I'll just click these to get rid of them..."
    window hide

    # Gameplay loop
    label loop:
        $ all_popups = []
        $ popup_images = ["img1"]

        # This will make the description for all buttons (numbers, values and positions)
        python:
            for i in range (0, 1):
                all_popups.append ( {
                    "popup_num":i,
                    "img":popup_images[renpy.random.randint (0, len(popup_images)-1)],
                    "x":(renpy.random.randint (30, 90))*10,
                    "y":(renpy.random.randint (15, 50))*10,
                    "showImage":True
                    } )
        $ result = ui.interact()
        $ game_timer = game_timer
        if result == "":
            jump loop

    hide screen game_scr
    "Ah shit! Stupid automatic Windows updates."
    "Nevertheless, I think I know just what to bait Mister Super with now..."

    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)

    return

#==============================================
''' ===========================================
CODE FOR RESEARCH GAME ABOVE /\ /\ /\ /\ /\ /\   WARNING WARNING WARNING =======================================================================
===============================================
'''#===========================================

label start:

    scene bg main

    show villain smile at left
    show hench stand at right

    v "Why, how I am enjoying this absolutely awful and contemptible Sunday! Not a care in the world, free as a little, plague-ridden bird. All villainous video games, no villainous work."
    h "Boss! It’s your responsibilities knocking!"
    v "What’s this? Responsibilities?"
    h "What’s the plan for the hero tonight, Boss?"
    v "...."
    v "...."
    v "Well, I’m still coming up with it, you see. Scuttle along, John and Mira, leave me to my dark work! You’re bothering me."
    h "Sorry, Boss! Of course, Boss!"

    call research_game

    menu:
        # TODO make these equal a piece of writing for use in label bait
        "Birthday card":
            $ chosen_bait = "A birthday card"
        "Mom":
            $ chosen_bait = "mom"
        "Shiny Charizard POKeMON(tm) card":
            $ chosen_bait = "A rare Pokemon card"
        "Underwear":
            $ chosen_bait = "Underwear"
        "Mac and cheese":
            $ chosen_bait = "Mac and Cheese"
        "A dirty bowl":
            $ chosen_bait = "A dirty, nasty bowl"
        "Dog":
            $ chosen_bait = "An innocent puppy"
        "Cardboard box":
            $ chosen_bait = "A simple cardboard box"
        "Husband":
            $ chosen_bait = "His husband"
        "Silly glasses with mustache":
            $ chosen_bait = "Some silly glasses"

    jump bait

label bait:

    v "Yes... yes... to lure the hero here, this is what we need! HENCHMAN! Come here!"
    h "You don’t have to yell, Boss. What is it?"
    v "Bait, John. We need bait. I’ve done some gruesome research, very complicated, and have come upon the perfect solution."
    h "What is it, Boss?"
    v "[chosen_bait], and quickly! As they say in showbiz- motivation is everything."
    h "You got it, Boss!"
    h "And what about a trap, Boss? What should we set up?"
    v "Yes, of course, why, I know just the thing...."

    menu:
        # TODO make these equal a piece of writing for use on line x
        "Open pool":
            v "Open the pool, Henchman Mira. I think I should go for a swim today. Or maybe not. Depends what I put inside, I guess. Maybe after."
            h "I’d love to go swimming after, Boss!"
            v "Absolutely fantastic, Mira! Put out a memo. After the hero's death, pool party!"

            $ chosen_trap = "pool"
            $ pool = True

        "Pitfall":
            v "I think I shall set up Paul's Ideal Tumbling Fall Apparatus."
            h "What... are L’s for?"
            v "Check the manual, Mira!"
            h "P.I.T.F.A....C.M.M?"
            v "Yes. Set up the Pitfactmm."

            $ chosen_trap = "pitfall"
            $ pitfall = True

        "Freeze ray":
            v "I believe the freeze ray shall come most in handy. Why I am absolutely... shivering.... With glee."
            h "Didn’t Mister Super break it?"
            v "No. Igloo’d it back together."
            h "Ok boss."

            $ chosen_trap = "ray"
            $ ray = True

        "Closing walls":
            v "Have the doors that are much thicker and open except for when the hero comes been installed yet, John?"
            h "You.. mean the closing walls?"
            h "Precisely! Great job, John!"

            $ chosen_trap = "walls"
            $ walls = True

        "Traps are a coward's game":
            v "Traps are a coward's game. Mira, John- I think today is the day we face our enemies head on."
            h "Are you going to... fight....the hero, Boss?"
            v "Why, of course not. My genius logic is beyond you, as usual. Wait and watch."

            $ chosen_trap = "no trap"
            $ no = True

label kill:

h "You got it, Boss! And what'll be the killing blow?"
v "I'm way ahead of you, Mira, and do not rush me!"
v "Hm... uh...Oh! I know just the thing."

menu:
    "Spikes":
            v "Scatter the spikes, my good friend. I believe we have a nasty little hero to skewer."
            h "Great idea, Boss! A hero kebab!"

            $ spikes = True

    "Spaghetti":
            v "Last potluck, do you remember, we ALL made spaghetti by sheer coincidence?"
            h "Yeah, haha. Carb night."
            v "Yes, but today, it's DIE night!"

            $ pasta = True

    "Sharks":
        v "Suit up, my little guppies. Retrieve Jimmy, Martin, and John 2 from the tanks! They are going to have a SUPER lunch."
        h "I thought we had been promoted to bass, Boss?"

        $ sharks = True

    "Fire":
        v "Call me Daddy Satan, because it's about to got hot in here! The flame jets, my little devils!"
        h "Oh, is is Friday night already?!"

        $ fire = True

    "Water":
        v "With haste, Henchmen! Fill this bucket with water from the tap. I'd LAKE it to be a little more WET in here."
        h "4/10, Boss."
        v "I try my best."

        $ water = True

    "Chicken":
        v "Fetch my leftovers, Mira! When we're through with this detestable super, they truly won't know what hit them.."
        h "The chicken, Boss?"
        v "Yes, that's what I said."

        $ chicken = True

    "Dinosaur":
        v "Loose the raptor cage. It's about to get Jurassic Park in this lair of villainly and evil. Doctor Faye Tality? More like, Doctor Alan Grant."
        h "Do you want all of the raptors, Boss?"
        v "No. Just Sasha and Bellamonte. Greogy and Harold are naughty boys."

        $ dino = True

    "Big Trumpet":
        v "Toot toot, John. Toot toot."
        h "The trumpet, STAT!"

        $ trumpet = True

    "Pillow":
        v "What time is it, Mira?"
        h "2:00 on the dot, Boss."
        v "Precisely as I thought. Nefarious Nap Time."

        $ pillow = True

if pool and spikes:
    jump pool_spikes

label pool_spikes:
    "Your henchman spend time carefully opening the pool and scattering spikes at the bottom, arraying them in a pattern of doom and death. It seems to you a stroke of genius."
    v "Yes. This seems like a stroke of genius to me."
    h "Are you... congratulating yourself?"
    v "Nobody else was doing it and I need my ego high before this encounter. Mister Super has a way of getting under my skin..."
    s "Did someone say MISTER SUPER?"
    v "God, no-"
    s "It is I, Mister Super, here to put an end to your dastardly deeds for the last time, Doctor Faye Tality!"
    v "I’m sure you are, Mister Super. But were you expecting THIS?"
    "With a yank of a nearby lever, Mister Super is yanked up into the air by a large mechanical claw."
    s "What’s this?!"
    v "Your doom."
    "He struggles against the claws, pulling at them with all he has. But not even his Mister Super Super Strength(TM) can save him now."
    "You hit the button atop the level, and the claw releases. Mister Super falls, impaled on the spikes scattered at the bottom of the pool."
    v "...."
    v "I can’t believe that worked."

    return
