#Cave Crawling
#Entrance to the Cave
    #Do you want to walk to the left toward the dark?
        #Find torch - ignite with match?
            #Yes - find yourself in flames
            #No - Keep walking while feeling the wall. You find the wall getting hotter and hotter. Continue walking?
                #Yes - you find a bridge over a river of lava to the exit! You're safely out!
                #No- you find yourself walking back in the darkness when you find a hole in the ground. Get into the hole?
                    #Yes - you found a water slide out of the cave into the nearest river outside!
                    #No - a poisonous spider bites you on the leg! You quickly fall down and die.

    #Do you want to walk forward toward the waterfall?
        #You find an oasis with gold on the floor. Do you want to swim underneath and get the gold?
            #Yes - You get in the water and a piranha eats your leg! You're left bleeding in the water.
            #No - You stumble into a treasure chest. Do you want to pick it up?
                    #Yes - You pick up the treasure chest and find an exit nearby! You're rich!
                    #No - You leave the gold and sprint out the exit!

    #Do you want to walk to the right toward the whispers?
                #You find yourself being eaten by a group of cannibals!


def cave_game():

    direction_from_entrance=input("You've entered a dark cave. Do you want to walk to the left toward the dark, forward toward the waterfall, or to the right toward the whispers? (Please type 'left', 'forward', or 'right') ")
    if (direction_from_entrance=='left'):
        match_ignite=input("You find a torch on the ground! Do you want to ignite it with a match? (yes or no) ")
        if(match_ignite=='yes'):
            print ("You find yourself in flames! You died! ")
        if(match_ignite=='no'):
            continue_walking=input("You keep walking while feeling the wall. But you find the wall getting hotter and hotter. Do you want to continue walking? (yes or no) ")
            if(continue_walking=='yes'):
                print ("You found a bridge over a river of lava to the exit! You're safely out! ")
            if(continue_walking=='no'):
                into_hole=input("Now you find yourself walking back into the darkness but now you find a hole in the ground! Do you want to get into the hole? (yes or no) ")
                if(into_hole=='yes'):
                    print("You found a water slide out of the cave into the nearest river outside! ")
                if(into_hole=='no'):
                    print("A poisonous spider bites you on your leg! You quickly fall down on the ground and die! ")
    if (direction_from_entrance=='forward'):
        swim_decision=input("You find an oasis with gold on the floor. Do you want to swim underneath and get the gold? (yes or no) ")
        if(swim_decision=='yes'):
            print("You get in the water and a piranha eats your leg! You're left bleeding in the water. ")
        if(swim_decision=='no'):
            pick_up=input("You stumble onto a treasure chest! Do you want to pick it up? ")
            if (pick_up=='yes'):
                print("You pick up the treasure chest and find an exit nearby! You're rich! ")
            if (pick_up=='no'):
                print("You leave the gold and sprint out the exit! ")
    if (direction_from_entrance=='right'):
        print("You find yourself eaten by a group of cannibals! ")
