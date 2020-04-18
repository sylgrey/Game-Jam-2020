# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Villain")
define h = Character("Henchmen")
define s = Character("Superhero")

default chosen_bait = ""
default chosen_trap = ""

# The game starts here.

label start:

    scene bg main

    show villain smile at right
    show hench stand at left

    v "Why, how I am enjoying this absolutely awful and contemptible Sunday! Not a care in the world, free as a little, plague-ridden bird. All villainous video games, no villainous work."
    h "Boss! It’s your responsibilities knocking!"
    v "What’s this? Responsibilities?"
    h "What’s the plan for the hero tonight, Boss?"
    v "...."
    v "...."
    v "Well, I’m still coming up with it, you see. Scuttle along, John and Mira, leave me to my dark work! You’re bothering me."
    h "Sorry, Boss! Of course, Boss!"

    menu:
        # TODO make these equal a piece of writing for use on line 61
        "Birthday card":
            $ chosen_bait = "bday"
        "Mom":
            $ chosen_bait = "mom"
        "Shiny Charizard POKeMON(tm) card":
            $ chosen_bait = "pkmn"
        "Underwear":
            $ chosen_bait = "underwear"
        "Mac and cheese":
            $ chosen_bait = "mac"
        "A dirty bowl":
            $ chosen_bait = "bowl"
        "Dog":
            $ chosen_bait = "dog"
        "Cardboard box":
            $ chosen_bait = "box"
        "Husband":
            $ chosen_bait = "husband"
        "Silly glasses with mustache":
            $ chosen_bait = "glasses"

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

        "Pitfall":
            v "I think I shall set up Paul's Ideal Fall Apparatus."
            h "What... are L’s for?"
            v "Check the manual, Mira!"
            h "P-I-T-F-A-C-T-M-M?"
            v "Yes. Set up the Pitfactmm."

            $ chosen_trap = "pitfall"

        "Freeze ray":
            v "I believe the freeze ray shall come most in handy. Why I am absolutely... shivering.... With glee."
            h "Didn’t Mister Super break it?"
            v "No. Igloo’d it back together."
            h "Ok boss."

            $ chosen_trap = "ray"

        "Closing walls":
            v "Have the doors that are much thicker and open except for when the hero comes been installed yet, John?"
            h "You.. mean the closing walls?"
            h "Precisely! Great job, John!"

            $ chosen_trap = "walls"

        "Traps are a coward's game":
            v "Traps are a coward's game. Mira, John- I think today is the day we face our enemies head on."
            h "Are you going to... fight....the hero, Boss?"
            v "Why, of course not. My genius logic is beyond you, as usual. Wait and watch."

            $ chosen_trap = "no trap"

label trap:

    return

label kill:

    return
