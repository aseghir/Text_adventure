# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 08:45:06 2018

@author: Moka
"""
"""
    DocString:
    
    A) Introduction:
    In this game, you will be a soldier. Your mission is to locate and apprehend
    a militia leader and to provide your fellow soldier with all the backup
    they need to make this mission successful
    
    Round 1: Decide what you want to do before starting the mission.
    Round 2: Get to a nearby village and standby for further orders.
    Round 3: Get to downtown and provide support to your comrades.
    Round 4: Get in the hospital and catch the leader.
    Round 5: Final faceoff with the militia leader.
    
    B) Known Bugs and/or Errors:
    None.
    
"""
from sys import exit
import random

def start():
    print(""" 
          You are at the base now, and you are about to leave for your misssion.
          """)
    input("<Press enter to continue>\n")
    The_base()  

def The_base():
    print("""
    You are about to be deployed, you're running a bit late, 
    any final thing you want to do before leaving for the mission?
    1) Call wife.
    2) Use the bathroom.
    3) Ready to go
    4) Bail out from the mission
    """)
    
    choice1 = input("> ")

    if "1" in choice1 or "call" in choice1 or "wife" in choice1:
        print("\nYour wife is waiting for you to return, make sure you do\n")
        input("<Press enter to continue>\n")
        village_2()
    
    elif "2" in choice1 or "use bathroom" in choice1 or "bathroom" in choice1:
        print("""\nOkay, now head to the tank, they're waiting for you.""")
        input("<Press enter to continue>\n")
        village_1()
    
    elif "3" in choice1 or "ready" in choice1 or "all set" in choice1:
        print("\nGreat! Let's go!")
        input("<Press enter to continue>\n")
        village_2()
    elif "4" in choice1 or "bail" in choice1 or "bail pit" in choice1:
        print("\nWhat a loser!")
        fail()
    else:
        print("Invalid command. Please try again.")
        input("<Press enter to continue>\n")
        The_base()
        
def village_2():
    print("""
          You've arrived to a village, so far everything is alright, the village is
          calm, maybe too calm, you and your squad stop on a safe zone, standby for 
          further orders, and more importantly, avoid any provocative sound, you
          wanna use the bathroom. you go inside an abandoned house. While using the
          bathroom, a guy attacks you. He is giving you a very hard time.
          What do you wanna do
          1) Shoot him.
          2) Knock him out.
    """)
    
    choice2 = input("> ")

    if "1" in choice2 or "shoot him" in choice2 or "shoot" in choice2:
        print("""
        Shots have been heard, It is about to get really messy,
        the militia has engaged in the fight, this has delayed your 
        arrival to the rendez-vous point and the leader has escaped
        """)
        fail()
    
    elif "2" in choice2 or "ko" in choice2 or "knock him out" in choice2:
        print("""
        You are trying to knock him out, however he slashes you
        with a knife, he tries to finish you off but your friend comes
        to your aid, he manages to kill the terrorist.
        """)
        input("<Press enter to continue>\n")
        downtown()
        
    else:
        print("Invalid command. Please try again.")
        input("<Press enter to continue>\n")
        village_2()
        
def village_1():   
    print(""" 
          You've arrived to a village, so far everything is alright, the 
          village is calm, maybe too calm, you and your squad stop on a safe
          zone, standby for further orders, and more importantly, avoid any 
          provocative sound. You have just been told to rush to downtown to 
          give reinforcement to your comrades
          """)
    input("<Press enter to continue>\n")
    downtown()
    
def downtown():
    print("""
          All hell is breaking loose, this area has become a warzone, you instantly
          engage on the fight, you take cover, one of the recon team member comes and
          gives you some intel about the leader's location which is the hospital in
          downtown and a chopper is supposed to pick him up and a hostage from the roof
          You ask your captain the permission to go inside but he doesn't allow you
          saying that the intervention squad is gonna take care of it, what should 
          you do:
          1) Obey
          2) Disobey
            """)
        
    choice3 = input("> ")
        
    if "1" in choice3 or "obey" in choice3: 
        print("""
              You obeyed the order, sometimes you need to do the right
              thing even if it means going against the orders, intervention
              squad didn't get the job done, mission failed
              """)
        fail()
    
    elif "2" in choice3 or "ko" in choice3 or "knock him out" in choice3:
        print("""
              You rush to the hospital ignoring your captain's orders.
              """)
        input("<Press enter to continue>\n")
        hospital()
        
    else:
        print("Invalid command. Please try again.")
        input("<Press enter to continue>\n")
        downtown()
        
def hospital():
    print("""
          You just infiltrated the hospital, you meet two members of the special 
          forces, you tell them that you're an ally, but since they were not
          expecting any friends they ask you the password, be careful, they 
          might ask you more than one password
          """)
    
    password_list = ['HEAVY...',
                     'WHISKY...',
                     'ECHO... ']
    passwords = 0
    
    while passwords < len(password_list):
        password = random.choice(password_list)
        input("<Press enter for your password test>\n")
        print(password)
        print(" ")
        
        if password == password_list[0]:
            print("""Finish the second part:
                        1) Rain
                        2) Snow""")
            pass1 = input("> ")
            if "1" in pass1 or "Rain" in pass1:
                print("""good answer, now next password""")
                passwords -=1
                
            else: 
                print ("""Wrong answer, you get shot, Mission failed""")
                fail()
            
        
        elif password == password_list[1]:
             print("""Finish the second part:
                     1) Motel
                     2) Hotel""")
             pass2 = input("> ")
             if "2" in pass2 or "Hotel" in pass2:
                print("""good answer, now next password""")
                passwords -=1
             else:
                print ("""Wrong answer, you get shot, Mission failed""")
                fail()
                
            
        elif password == password_list[2]:    
             print("""Finish the second part:
                    1) Dot
                    2) Pot""")
             pass3 = input("> ")
             if "1" in pass3 or "Dot" in pass3:
                print("""good answer, good to have you with us brother!""")
                passwords -=1
                hospital2()
             else: 
                print ("""Wrong answer, you get shot, Mission failed""")
                fail()
                
                
                break
                   
    
def hospital2():    
    input("<Press enter to continue>\n")
    print("""
          \nYou see two terrorist, what should you do?
          1) take them out
          2) avoid them
          """)
    
    choice4 = input("> ")
    
    if "1" in choice4 or "take them out" in choice4: 
            print("""
                  \nYou took them out, now you're advancing to the first floor,
                  you hear the chopper, you start running up the stairs, it is 
                  weird, there are no guard, you made it to the roof and the
                  chopper was just a diversion, the leader escaped, Mission failed
                  """)
            fail()
    
    elif "2" in choice4 or "avoid" in choice4 or "avoid them" in choice4:
            print("""
                  \nYou hear them talking about their leader's plan and the
                  fact that the entire chopper is a diversion to allow their leader
                  escape through the hospital's backyard.
                  """)
            input("<Press enter to continue>\n")
            backyard()
        
    else:
            print("Invalid command. Please try again.")
            input("<Press enter to continue>\n")
            hospital2()
    
def backyard():  
    print("""
          You see the leader, you point your gun towards him and ask hime to
          stop. However, he has a hostage, what should you do?
          1) Shoot
          2) don't shoot
          """)
    
    choice5 = input("> ")
    if "1" in choice5 or "shoot" in choice5: 
            print("""
                  Nice shot, you shot his arm and saved the hostage, 
                  the terrorists leader has been apprehended, Mission complete
                  """)
            success()
            
            
    elif "2" in choice5 or "no" in choice5 or "don't shoot" in choice5:
            print("""
                  He shot the hostage! you also shoot and kill him, 
                  Bad ending
                  """)
            fail()
    else:
            print("Invalid command. Please try again.")
            input("<Press enter to continue>\n")
            backyard()        
def success():
    print("""
          You have completed your mission soldier! Great job!
          """)
    input("<Press enter to exit, you hero!>\n")
    exit(0)
    
def fail():
    print('\nYou have failed in your mission soldier.')
    input('<Game Over>')
    exit(0)

start()         
    
    
    
    