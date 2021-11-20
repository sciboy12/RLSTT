# RLSTT - Speech-to-text/quick chat for Rocket League via Kaldi
## Setup

### Requirements
```
pywin32
pypiwin32
dragonfly2
pyautogui
dragonfly2[kaldi]
```
Download a model from [daanzu/kaldi-active-grammar](https://github.com/daanzu/kaldi-active-grammar/), and extract it to RLSTT/kaldi_model/

## Configuration*
`EnablePTT`: Enables Push-To-Talk

`EnableDictation`: Enables dictation via text chat

`AutoSend`: (dictate only) Automatically press Enter after message is written

*All options are found towards the top of main.py

## TODO
* Autodetect in-game quick chat settings, if possible
* Implement/Test Linux support (may already work due to usage of kaldi)
* Add team chat support to dictation
