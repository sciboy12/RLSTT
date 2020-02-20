# RLSTT - Voice-activated Quick-chat for Rocket League on Windows

## Installation

Download Python 3 from [Here](https://www.python.org/downloads/).

Browse to the download location, and run `setup.bat`.

Or, alternatively:

`
python3 -m pip install -r requirements.txt

`

To run, open `start.bat`.

## Configuration

To change the phrases that map to the quick chat commands, 

## Speech Training*

If you find that the recognition accuracy is low, you can train the service to your voice, by running Windows Speech Recognition from the Start Menu, and following the steps.

### TODO:
* Find a detection method that doesn't involve 12-16 callbacks
* Auto-detect in-game quick-chat settings, if possible
* Test setup.bat on a clean Python install