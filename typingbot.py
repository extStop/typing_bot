"""
File: typingbot.py

A short program that is capable of completing
typing.com modules
"""


import time, os, re
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


        
pattern = re.compile("([\d]+)/([\d]+)")
filePattern = re.compile("Username:[ ]?(.+)\nPassword:[ ]?(.+)")

path = Path(os.path.dirname(os.path.realpath(__file__)))
chromePath = os.path.join(path, "chromedriver.exe")
print("Starting up web browser...")
browser = webdriver.Chrome(executable_path=chromePath)

actions = ActionChains(browser)

with open("credentials.txt", "r") as file:
    m = re.match(filePattern, file.read())
    username = m.group(1)
    password = m.group(2)

# Log into typing.com
browser.get("https://www.typing.com/student/login")

# Enter username
nameField = browser.find_element_by_id("form-ele-username")
nameField.send_keys(username)
actions.send_keys(Keys.ENTER)
actions.perform()

# Inject a brief waiting period
time.sleep(.5)

# Enter password
passField = browser.find_element_by_id("form-ele-password")
passField.send_keys(password)
actions.send_keys(Keys.ENTER)
actions.perform()

# Allow the user to navigate to the problem section
input("Navigate to the section and hit enter...")
actions.send_keys(Keys.ENTER)
actions.perform()

def sendWithDelay(letters, wpm=0):
    if wpm:
        kpm = wpm * 5
        kps = kpm / 60
        for l in letters:
            actions.send_keys(l)
            actions.perform()
            time.sleep(kps)
    else:
        actions.send_keys(letters)
        actions.perform()

while True:

    while True:

        # While there is no continue button
        while len(browser.find_elements_by_class_name("js-continue-button")) == 0:

            # Get the letters
            letters = browser.find_elements_by_class_name("screenBasic-letter")
            finishedLetters = set(browser.find_elements_by_class_name("is-right"))
            letters = "".join([l.text for l in letters if not l in finishedLetters])
            letters.replace("\n", " ").split("   ")
            letters = letters.replace("⏎", "\n")

            # Type the letters
            sendWithDelay(letters, wpm=70)

        progress = browser.find_elements_by_class_name("split-cell")
        if len(progress) >= 9:
            num = progress[9].text
            m = re.match(pattern, num)
            active = browser.find_elements_by_class_name("is-active")[0].text
            if (not m) or (active==m.group(2)):
                break

        # Handle cases with pop ups
        continueButton = browser.find_elements_by_class_name("js-continue-button")
        if len(continueButton) > 0:
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(.5)

    if input("Again? ").lower() == "n":
        break
        
browser.quit()
print("Done")
