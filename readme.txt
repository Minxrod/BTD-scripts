This is a collection of small scripts designed for the Bloons Tower Defense games.

===Instructions===
All of these scripts are meant to run from the command line.
Expects Python to be installed. Requires Pillow and pynput.

To install pynput and Pillow:
> py -m pip install Pillow
> py -m pip install pynput

Example usage (BTD5/BMC should be opened already):
> py ability.py

===Script List===
ability.py - lets you use hotkeys for abilities. Intended to replicate BTD5 ability hotkeys in BMC, though technically could do more.

clicker.py - auto start round. Intended to substitute for auto-start in BTD5 Co-op mode.

More to be added as I make them.

===Known Issues===
ability.py
* can't add new abilities after selecting count. 
* can't move window
* dartlings will flick in the direction of the abilities.
  > this is because the script functions by quickly moving the mouse to ability, clicking, and moving back.

clicker.py
* requires window focus
* can't move window
* can't end script without closing command window or waiting for all rounds to be clicked

both
* untested in fullscreen