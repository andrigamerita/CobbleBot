# CobbleBot for Python
# Copyright 2020, OctoAndri
# https://github.com/andrigamerita/CobbleBot
# Licensed under the GPLv3 license:
# https://www.gnu.org/licenses/gpl-3.0.en.html

import time
import argparse
import keyboard
import mouse

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--block",
    help="Specifies the amount of blocks that have already been generated; default is 0.")
ap.add_argument("-c", "--click",
    help="Specifies the button that acts as the Place/Interact; default is Right Mouse (MouseRight).")
ap.add_argument("-l", "--lava",
    help="Specifies the button that selects Lava in the hotbar; default is Numrow 8 (eight).")
ap.add_argument("-w", "--water",
    help="Specifies the button that selects Water in the hotbar; default is Numrow 9 (nine).")
#ap.add_argument("-s", "--stop",
#    help="Specifies the button that Stops or Exits the script; default is .")
args = ap.parse_args()

loopgen = int(0)
loopdone = int(0)
startwait = float(3.00)
loopweight = int(90)
maxblocks = int(255)
clickbtnis = str("rmouse")
clickbtn = str("")
lavabtnis = str("keyboard")
lavabtn = str("eight")
waterbtnis = str("keyboard")
waterbtn = str("nine")
#stopbtn = str("")
usedoptions = int(0)

if (str(args.block) != "None"):
    loopgen = int(args.block)
    usedoptions = int(1)

if (str(args.click) != "None"):
    if (str(args.click) == "MouseLeft"):
        clickbtnis = str("lmouse")
    else:
        clickbtn = str(args.click)
        clickbtnis = str("keyboard")
    usedoptions = int(1)

if (str(args.lava) != "None"):
    if (str(args.lava) == "MouseLeft"):
        lavabtnis = str("lmouse")
    elif (str(args.lava) == "MouseRight"):
        lavabtnis = str("rmouse")
    else:
        lavabtn = str(args.lava)
    usedoptions = int(1)

if (str(args.water) != "None"):
    if (str(args.water) == "MouseLeft"):
        waterbtnis = str("lmouse")
    elif (str(args.water) == "MouseRight"):
        waterbtnis = str("rmouse")
    else:
        waterbtn = str(args.water)
    usedoptions = int(1)

#if (str(args.stop) != "None"):
#    stopbtn = str(args.stop)
#    usedoptions = int(1)
    
if (loopgen > 0):
    loopweight = (90 + (loopgen * 120))

print("\nStarting script in " + str(startwait) + " seconds...\nPress CTRL+C in this window at any moment to Exit.")
time.sleep(startwait)
print("\nScript in progress...")
if (usedoptions != int(1)):
    print("NOTE: You started the script with default settings.\nStart it with flag -h to see all the available options.")


while (loopgen < maxblocks):
    
    lavasleep = float(loopweight * 0.05)           # At every cycle sets the wait time for Lava.
    
    if (lavabtnis == "lmouse"):                    # Select Lava
        mouse.click(button='left')                 #
    elif (lavabtnis == "rmouse"):                  #
        mouse.right_click()                        #
    else:                                          #
        keyboard.send(lavabtn)                     #
    
    if (clickbtnis == "lmouse"):                   # Place Lava
        mouse.click(button='left')                 #
    elif (clickbtnis == "rmouse"):                 #
        mouse.right_click()                        #
    else:                                          #
        keyboard.send(clickbtn)                    #
    
    time.sleep(90 * 0.05)                          # Wait for Lava to start flowing
    
    if (clickbtnis == "lmouse"):                   # Unplace Lava
        mouse.click(button='left')                 #
    elif (clickbtnis == "rmouse"):                 #
        mouse.right_click()                        #
    else:                                          #
        keyboard.send(clickbtn)                    #
    
    time.sleep(lavasleep)                          # Wait for Lava to complete its flow
    
    if (waterbtnis == "lmouse"):                   # Select Water
        mouse.click(button='left')                 #
    elif (waterbtnis == "rmouse"):                 #
        mouse.right_click()                        #
    else:                                          #
        keyboard.send(waterbtn)                    #
    
    if (clickbtnis == "lmouse"):                   # Place Water
        mouse.click(button='left')                 #
    elif (clickbtnis == "rmouse"):                 #
        mouse.right_click()                        #
    else:                                          #
        keyboard.send(clickbtn)                    #
    
    time.sleep(15 * 0.05)                          # Wait for Water to start flowing
    
    if (clickbtnis == "lmouse"):                   # Unplace Water
        mouse.click(button='left')                 #
    elif (clickbtnis == "rmouse"):                 #
        mouse.right_click()                        #
    else:                                          #
        keyboard.send(clickbtn)                    #
    
    time.sleep(2)                                  # Waits for 2 seconds in order to make Water flow correctly.
    
    loopweight = (loopweight + 120)                # At every cycle augments the wait time for Lava
    loopgen = (loopgen + 1)                        # Counts the absolute completed cycles
    
    loopdone = (loopdone + 1)                      # Counts the completed cycles
    print ("Done " + str(loopdone) + " cycle(s).") # Prints the number of completed cycles in the console.


print("\nScript completed. " + loopdone + " blocks travelled.")