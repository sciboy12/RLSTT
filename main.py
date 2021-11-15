import dragonfly
import pyautogui

enable_ptt = False

def SendMessage(msg):
    if enable_ptt and keyboard.is_pressed('o'):
        pyautogui.write(msg, interval = 0.1)
    else:
        pyautogui.write(msg, interval = 0.1)

# List of messages/commands
class MappingRule(dragonfly.MappingRule):
    mapping = {
            # Imformational
            "i got it":             dragonfly.Function(SendMessage, msg="11"),
            "incoming":             dragonfly.Function(SendMessage, msg="12"),
            "go for it":            dragonfly.Function(SendMessage, msg="13"),
            "defending":            dragonfly.Function(SendMessage, msg="14"),
            
            # Compliments
            "nice shot":            dragonfly.Function(SendMessage, msg="21"),
            "what a save":          dragonfly.Function(SendMessage, msg="22"),
            "thanks":               dragonfly.Function(SendMessage, msg="23"),
            "great pass":           dragonfly.Function(SendMessage, msg="24"),

            # Reactions
            "calculated":           dragonfly.Function(SendMessage, msg="31"),
            "what a play":          dragonfly.Function(SendMessage, msg="32"),
            "wow":                  dragonfly.Function(SendMessage, msg="33"),
            "close one":            dragonfly.Function(SendMessage, msg="34"),

            # Apologies
            "dang|darn|crap|shit":  dragonfly.Function(SendMessage, msg="41"),
            "no problem":           dragonfly.Function(SendMessage, msg="42"),
            "whoops":               dragonfly.Function(SendMessage, msg="43"),
            "sorry":                dragonfly.Function(SendMessage, msg="44"),
            
            # Post game
            "good game|g g":        dragonfly.Function(SendMessage, msg="11"),
            "well played":          dragonfly.Function(SendMessage, msg="12"),
            "that was fun":         dragonfly.Function(SendMessage, msg="13"),
            "what a game":          dragonfly.Function(SendMessage, msg="14")
            }

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
