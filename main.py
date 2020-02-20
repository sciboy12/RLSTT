import pyautogui
import time
import pythoncom
from dragonfly import Grammar, CompoundRule
import keyboard

enable_ptt = True

# List of messages
# This may be replaced by use of the game's config file later, if possible
# use all lowercase when editing
messages = [
    'i got it',
    'incoming',
    'go for it',
    'defending',
    'nice shot',
    'what a save',
    'thanks',
    'great pass',
    'calculated',
    'whew|phew',
    'wow',
    'close one',
    'heck',
    'no problem',
    'whoops',
    'sorry'
    'good game|gg',
    'well played',
    'that was fun',
    'what a game'
    ]

# Chat keypress mapping
c0 = 11 #Informational, Message 1
c1 = 12 #Informational, Message 2
c2 = 13 #Informational, Message 3
c3 = 14 #Informational, Message 4

c4 = 21 #Compliments, Message 1
c5 = 22 #Compliments, Message 2
c6 = 23 #Compliments, Message 3
c7 = 24 #Compliments, Message 4

c8 = 31 #Reactions, Message 1
c9 = 32 #Reactions, Message 2
c10 = 33 #Reactions, Message 3
c11 = 34 #Reactions, Message 4

c12 = 11 #Post-game, Message 1
c13 = 12 #Post-game, Message 2
c14 = 13 #Post-game, Message 3
c15 = 14 #Post-game, Message 4

# Map list above to a single value
#c = c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15

# Voice command rule combining spoken form and recognition processing.
class r0(CompoundRule):
    spec = messages[0]  # Informational, Message 1
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True:
            pyautogui.write(str(c0), interval=0.1)

class r1(CompoundRule):
    spec = messages[1]  # Informational, Message 2
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True:
            pyautogui.write(str(c1), interval=0.1)

class r2(CompoundRule):
    spec = messages[2]  # Informational, Message 3
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True:
            pyautogui.write(str(c2), interval=0.1)

class r3(CompoundRule):
    spec = messages[3]  # Informational, Message 4
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c3), interval=0.1)

class r4(CompoundRule):
    spec = messages[4]  #Compliments, Message 1
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c4), interval=0.1)

class r5(CompoundRule):
    spec = messages[5]  #Compliments, Message 2
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c5), interval=0.1)

class r6(CompoundRule):
    spec = messages[6]  #Compliments, Message 3
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c6), interval=0.1)

class r7(CompoundRule):
    spec = messages[7]  #Compliments, Message 4
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c7), interval=0.1)

class r8(CompoundRule):
    spec = messages[8]   #Reactions, Message 1
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c8), interval=0.1)

class r9(CompoundRule):
    spec = messages[9]   #Reactions, Message 2
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c9), interval=0.1)

class r10(CompoundRule):
    spec = messages[10]  #Reactions, Message 3
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c10), interval=0.1)

class r11(CompoundRule):
    spec = messages[11]  #Reactions, Message 4
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c11), interval=0.1)

class r12(CompoundRule):
    spec = messages[12] # Post-Game, Message 1
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c12), interval=0.1)

class r13(CompoundRule):
    spec = messages[13] # Post-Game, Message 2
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c13), interval=0.1)

class r14(CompoundRule):
    spec = messages[14] # Post-Game, Message 3
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c14), interval=0.1)

class r15(CompoundRule):
    spec = messages[15] # Post-Game, Message 4
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        if ptt == True: # Check if the PTT hotkey is being held
            pyautogui.write(str(c15), interval=0.1)

grammar = Grammar('grammar')    # Create a grammar to contain the command rule.
# Add the command rule to the grammar.
# Informational
grammar.add_rule(r0())
grammar.add_rule(r1())
grammar.add_rule(r2())
grammar.add_rule(r3())
grammar.add_rule(r4())
grammar.add_rule(r5())
grammar.add_rule(r6())
grammar.add_rule(r7())
grammar.add_rule(r8())
grammar.add_rule(r9())
grammar.add_rule(r10())
grammar.add_rule(r11())
grammar.add_rule(r12())
grammar.add_rule(r13())
grammar.add_rule(r14())
grammar.add_rule(r15())
grammar.load()
print('Ready')
global ptt

while True:
    if enable_ptt: ptt = keyboard.is_pressed('l')
    else: ptt = True
    pythoncom.PumpWaitingMessages()
    time.sleep(0.1)
