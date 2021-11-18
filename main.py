import dragonfly
import pyautogui

EnablePTT = False
EnableDictation = True
AutoSend = False

def Write(msg, enter = False):
    pyautogui.write(msg, interval = 0.1)

def WriteMessage(msg, *enter):
    if EnablePTT and keyboard.is_pressed('o'):
        Write(msg, *enter)
    else:
        Write(msg, *enter)

def WriteText(msg):
    if EnableDictation:
        pyautogui.press('enter')
        WriteMessage(msg, *enter)
        
    if AutoSend:
        pyautogui.press('enter')

# List of messages/commands
class MappingRule(dragonfly.MappingRule):
    mapping = {
            # Imformational
            "i got it":             dragonfly.Function(WriteMessage, msg="11"),
            "incoming":             dragonfly.Function(WriteMessage, msg="12"),
            "go for it":            dragonfly.Function(WriteMessage, msg="13"),
            "defending":            dragonfly.Function(WriteMessage, msg="14"),
            
            # Compliments
            "nice shot":            dragonfly.Function(WriteMessage, msg="21"),
            "what a save":          dragonfly.Function(WriteMessage, msg="22"),
            "thanks":               dragonfly.Function(WriteMessage, msg="23"),
            "great pass":           dragonfly.Function(WriteMessage, msg="24"),

            # Reactions
            "calculated":           dragonfly.Function(WriteMessage, msg="31"),
            "what a play":          dragonfly.Function(WriteMessage, msg="32"),
            "wow":                  dragonfly.Function(WriteMessage, msg="33"),
            "close one":            dragonfly.Function(WriteMessage, msg="34"),

            # Apologies
            "dang|darn|crap|shit":  dragonfly.Function(WriteMessage, msg="41"),
            "no problem":           dragonfly.Function(WriteMessage, msg="42"),
            "whoops":               dragonfly.Function(WriteMessage, msg="43"),
            "sorry":                dragonfly.Function(WriteMessage, msg="44"),
            
            # Post game
            "good game|g g":        dragonfly.Function(WriteMessage, msg="11"),
            "well played":          dragonfly.Function(WriteMessage, msg="12"),
            "that was fun":         dragonfly.Function(WriteMessage, msg="13"),
            "what a game":          dragonfly.Function(WriteMessage, msg="14"),

            # Text chat
            "send <msg>":       dragonfly.Function(lambda msg: WriteText(msg))
            }

    extras = [ dragonfly.Dictation("msg") ]
    
# Init Kaldi engine
engine = dragonfly.get_engine("kaldi",
    model_dir='kaldi_model',
    # input_device_index=None,  # set to an int to choose a non-default microphone
)

# Call connect() now that the engine configuration is set.
engine.connect()

# Voice command rule combining spoken form and recognition processing.
grammar = dragonfly.Grammar('grammar') # Create a grammar to contain the command rules 

# Add the command rule to the grammar.
grammar.add_rule(MappingRule())
grammar.load()

# Enter recognition loop
print('Ready')
engine.do_recognition()
