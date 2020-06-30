import pyautogui
import time
import emoji
import pyperclip


def keepPrintingMessages(times, comments):
    time.sleep(5)
    for i in range(times):
        pyautogui.typewrite(comments[i % len(comments)])
        pyautogui.typewrite("\n")
        time.sleep(1)


def keepTypingEmojis(times, emo, pyramidSize):
    time.sleep(5)
    n = 1
    for i in range(times):
        for j in range(n):
            pyperclip.copy(emoji.emojize(emo))
            pyautogui.hotkey("ctrl", "v")

        pyautogui.typewrite("\n")
        n = n+1
        if n > pyramidSize:
            n = 1
        time.sleep(1.5)
        print(i)


################### Input messages here #################################
# write your comments/messages here
comments = ["Hi", "hey beautiful <3 :*", "ki khobor? 😒😒😒😒😒😒", "amar sathe date e jaba?",
            "kotha bolo na keno? :'( ", "ami ugly bole? T_T", "tomake treat dibo", "ami tution kore 50k salary pai"]

# paste your emoji here
emo = emoji.demojize("😒")
# print(type(emo))
# print(emo)
# pyautogui.alert(emoji.emojize(emo))

keepTypingEmojis(100, emo, 4)
