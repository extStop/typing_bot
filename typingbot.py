"""
File: typingbot.py

A short program that is capable of completing
typing.com modules
"""


import time, pyautogui, os, re
from pathlib import Path
from selenium import webdriver

pattern = re.compile("([\d]+)/([\d]+)")

path = Path(os.path.dirname(os.path.realpath(__file__)))
chromePath = os.path.join(path, "chromedriver.exe")
print("Starting up web browser...")
browser = webdriver.Chrome(executable_path=chromePath)

# Log into typing.com
browser.get("https://www.typing.com/student/login")
time.sleep(2)
pyautogui.typewrite("pmhs_account_18")
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("keyboarding22")
pyautogui.press("enter")

# Allow the user to navigate to the problem section
input("Navigate to the section and hit enter...")
time.sleep(2)
pyautogui.press("enter")

while True:

    time.sleep(1)

    while True:

        count = 0
        while len(browser.find_elements_by_class_name("js-continue-button")) == 0:
            letters = browser.find_elements_by_class_name("screenBasic-letter")
            finishedLetters = browser.find_elements_by_class_name("is-right")
            letters = [l for l in letters if not l in finishedLetters]
            letters = "".join([l.text for l in letters])
            letters.replace("\n", " ").split("   ")
            letters = letters.replace("⏎", "\n")
            pyautogui.typewrite(letters, interval=.05)
            count += 1

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
            pyautogui.press("enter")
            time.sleep(1)

    if input("Again? ").lower() == "n":
        break
        
browser.quit()
print("Done")
