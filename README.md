# Typing.com Bot
A simple program that automates the completion of individual typing.com modules.

# Required Dependencies
Before you can run the Typing Bot, you must first install pyautogui and selenium.
```bash
pip install pyautogui
```
```bash
pip install selenium
```

# Compatible Drivers
This program is only designed to work in the Chrome web browser.  Changes can be made to the python script to allow other browsers, but this is left as an exercise for the user.  For your convenience, a version of the chromedriver is provided, but it still may be necessary for you to download a newer version and replace it.

# Running the Program
```bash
py typingbot.py
```

# Using the Program
When run, the program will launch a new Chrome window.  It will then use the provided credentials to access your typing.com account.  Once signed into your account, control is returned to the user.  The terminal will display a message saying, "Navigate to the section and hit enter..."  Follow these directions and make your way to the lesson you want automated.  Once there, press enter in the terminal and quickly return focus to the browser.  The program should automatically and seemlessly complete the provided module.  

IMPORTANT - Once the bot starts automating the lesson, you cannot interact with your machine.  Doing so will cause the keystrokes to interact with other programs.

Once the lesson is completed, the terminal will prompt the user with "Again?"  Any answer but an "N" will cause the program to prepare for another lesson.  If you desire to complete another lesson, first navigate to said lesson, then hit enter in the terminal.

# Providing Your Credentials
Supply your username and password in the credentials.txt file on their respective lines.
