# LED Sign project

Usage python led_print -m <messaage>

Options:
-e emulator/sign
-s scroll
-g applet (used with emulator)
-m message to display

DONE:
- Hardware integration
- Emulator for testing
    - Supports console and applet
- ASCII support
- Scrolling (optional)

IN_PROGRESS
- Adding comments to files
    - currently in base_handler.py

TODO: 
- Package sign and mount
- Write server for rpi that listens to input from outside sources
- Android app to select mode e.g. time and date, custom input, etc.
