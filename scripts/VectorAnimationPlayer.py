import keyboard
import anki_vector

robot = anki_vector.Robot("00a10a53")       # Define Vector robot object
robot.connect()                             # Connect to the robot

robot.behavior.drive_off_charger()

anim_list = robot.anim.anim_list            # Get the list of animations available

keyVerif = True

for anim in anim_list :
    print(str(len(anim_list)) + " animations available")            # Show the amount of animations available
    print("Animation number " + str(anim_list.index(anim) + 1))     # Show the animation number
    print("Animation name : " + anim)                               # Show the name of the animation
    while True :                                                    # Replay loop
        if keyVerif:
            print("Playing")                                        # Show when animation is playing
            robot.anim.play_animation(anim)                         # Play animation
            print("Continue (c), Replay (r)")                       # Ask to continue or replay
        key = keyboard.read_key()                                   # 
        if key == 'c':
            print("-------------------- Next Animation --------------------")
            keyVerif = True
            break
        elif key == 'r':
            keyVerif = True
        else:
            keyVerif = False
            
