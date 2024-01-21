'''
import time 
import screen_brightness_control as sbc
import random

votes=['BROWSE','DEBUG', 'PLAY', 'READ', 'WRITE', 'WATCH']
majority_vote= votes[random.randint(0,5)]
print(majority_vote)

def BROWSE_mod():
    {
    print("called browse")
}
def READ_mod():
    {
    print("called read")
}
def PLAY_mod():
    {
    print("called play")
}
def DEBUG_mod():
    {
    print("called debug")
}
def WRITE_mod():
    {
    print("called write")
}
def WATCH_mod():
    {
    print("called watch")
}
    
#more readable and maintainable
function_dict={
    'BROWSE': BROWSE_mod,
    'DEBUG': DEBUG_mod,
    'READ': READ_mod,
    'PLAY': PLAY_mod,
    'WATCH': WATCH_mod,
    'WRITE': WRITE_mod
}

if majority_vote in function_dict:
    function_dict[majority_vote]()
'''

import datetime 
import screen_brightness_control as sbc
import random

global majority_vote

brightness = sbc.get_brightness()
primary = sbc.get_brightness(display=0)

print("Current Brightness:  ", brightness)
print("Current Primary display brightness: ",primary)

now=datetime.datetime.now().time()

morning_start=datetime.time(7,0)
evening_start=datetime.time(19,0)

class ActivityDecider:
    
    @classmethod
    def activity_tap(cls):
        global majority_vote
        votes = ['BROWSE', 'DEBUG', 'PLAY', 'READ', 'WRITE', 'WATCH']
        majority_vote = votes[random.randint(0, 5)]
        print(majority_vote)
    
    @classmethod    
    def BROWSE(cls):
        print("called browse")
        if morning_start<=now<evening_start:
            sbc.set_brightness(70)
            sbc.set_brightness(70, display=0)
        else:
            sbc.set_brightness(50)
            sbc.set_brightness(50, display=0)
        
    @classmethod
    def READ(cls):
        print("called read")
        if morning_start<=now<evening_start:
            sbc.set_brightness(55)
            sbc.set_brightness(55, display=0)
        else:
            sbc.set_brightness(35)
            sbc.set_brightness(35, display=0)
    
    @classmethod
    def PLAY(cls):
        print("called play")
        if morning_start<=now<evening_start:
            sbc.set_brightness(100)
            sbc.set_brightness(100, display=0)
        else:
            sbc.set_brightness(80)
            sbc.set_brightness(80, display=0)
        
        
    @classmethod
    def DEBUG(cls):
        print("called debug")
        if morning_start<=now<evening_start:
            sbc.set_brightness(45)
            sbc.set_brightness(45, display=0)
        else:
            sbc.set_brightness(30)
            sbc.set_brightness(30, display=0)
        
        
    @classmethod
    def WRITE(cls):
        print("called write")
        if morning_start<=now<evening_start:
            sbc.set_brightness(50)
            sbc.set_brightness(50, display=0)
        else:
            sbc.set_brightness(40)
            sbc.set_brightness(40, display=0)
        
    
    @classmethod
    def WATCH(cls):
        print("called watch")
        if morning_start<=now<evening_start:
            sbc.set_brightness(100)
            sbc.set_brightness(100, display=0)
        else:
            sbc.set_brightness(80)
            sbc.set_brightness(80, display=0)



ActivityDecider.activity_tap()
getattr(ActivityDecider, majority_vote)()



for monitor in sbc.list_monitors():
    print(monitor, ':', sbc.get_brightness(display=monitor), '%')

