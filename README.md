# Typing.com Bot
A simple program that automates the completion of individual typing.com modules.

# Required Dependencies
Before you can run the Typing Bot, you must first install selenium.
```bash
pip install selenium
```

# Compatible Drivers
This program is only designed to work in the Chrome web browser.  Changes can be made to the python script to allow other browsers, but this is left as an exercise for the user.  A version of the Chrome Driver has been provided, but before the program will run successfully you will most likely need to download a replacement that compatible with your current version of Chrome.  You can download drivers from this link: https://chromedriver.chromium.org/downloads.  Once downloaded, unzip the file and move the driver into the typing_bot directory.

# Running the Program
```bash
py typingbot.py
```

# Using the Program
When run, the program will launch a new Chrome window.  It will then use the provided credentials to access your typing.com account.  Once signed into your account, control is returned to the user.  The terminal will display a message saying, "Navigate to the section and hit enter..."  Follow these directions and make your way to the lesson you want automated.  Once there, press enter in the terminal.  The program should automatically and seamlessly complete the provided module. The user has full control of their machine while the bot runs in the background.

NOTE:  The bot will type in bursts.  It takes some time to process the keys that still need to be typed.  The length of the wait is dependent on the exercise and the loading speed of your browser.

Once the lesson is completed, the terminal will prompt the user with "Again?"  Any answer but an "N" will cause the program to prepare for another lesson.  If you desire to complete another lesson, first navigate to said lesson, then hit enter in the terminal.

# Providing Your Credentials
Supply your username and password in the credentials.txt file on their respective lines.
