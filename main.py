import time
import pythoncom
from dragonfly import Grammar, MappingRule, Key, Text, Function
import keyboard

enable_ptt = True

def SendMessage(msg):
    if keyboard.is_pressed('l'):
        keyboard.write(msg)
        
# List of messages/commands
class MappingRule(MappingRule):
    mapping = {
            "i got it":                 Function(SendMessage, msg="11"),
            "incoming":                 Function(SendMessage, msg="12"),
            "go for it":                Function(SendMessage, msg="13"),
            "defending":                Function(SendMessage, msg="14"),
            "nice shot":                Function(SendMessage, msg="21"),
            "what a save":              Function(SendMessage, msg="22"),
            "thanks":                   Function(SendMessage, msg="23"),
            "great pass":               Function(SendMessage, msg="24"),
            "calculated":               Function(SendMessage, msg="31"),
            "whew|phew":                Function(SendMessage, msg="32"),
            "wow":                      Function(SendMessage, msg="33"),
            "close one":                Function(SendMessage, msg="34"),
            "dang it|darn it":     Function(SendMessage, msg="41"),
            "no problem":               Function(SendMessage, msg="42"),
            "whoops|oops":              Function(SendMessage, msg="43"),
            "sorry":                    Function(SendMessage, msg="44"),
            "good game|G. G.":          Function(SendMessage, msg="11"),
            "well played":              Function(SendMessage, msg="12"),
            "that was fun":             Function(SendMessage, msg="13"),
            "what a game":              Function(SendMessage, msg="14")
            }

# Voice command rule combining spoken form and recognition processing.
grammar = Grammar('grammar') # Create a grammar to contain the command rules 

# Add the command rule to the grammar.
grammar.add_rule(MappingRule())
grammar.load()
print('Ready')

while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(0.1)
