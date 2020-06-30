import pyautogui
import time
import emoji
import pyperclip


def keepTypingMessages(times, comments):
    '''
    This function keeps typing the strings in comments list.
    Waits for 5 seconds so that the user can place his cursor in position.
    Total messages typed on screen will be equals to times variable.
    After that it will stop.
    '''
    time.sleep(5)
    for i in range(times):
        pyautogui.typewrite(comments[i % len(comments)])
        pyautogui.typewrite("\n")
        print(i)
        time.sleep(1)


def keepTypingEmojis(times, emo, pyramidSize):
    '''
    This function keeps typing the and making emoji pyramid with the passed emoji in emo variable.
    Waits for 5 seconds so that the user can place his cursor in position.
    Total pyramids created on screen will be equals to times variable.
    After that it will stop.
    '''
    time.sleep(5)
    n = 1
    for i in range(times):
        for j in range(n):
            pyperclip.copy(emoji.emojize(emo))
            pyautogui.hotkey("ctrl", "v")

        time.sleep(0.5)
        pyautogui.typewrite("\n")
        n = n+1
        if n > pyramidSize:
            n = 1
        time.sleep(1.5)
        print(i)


################### Input messages here #################################
# write your comments/messages here
comments = ["Hi", "hey beautiful <3 :*", "ki khobor?", "amar sathe date e jaba?",
            "kotha bolo na keno? :'( ", "ami ugly bole? T_T", "tomake treat dibo", "ki holo jaba na?"]

# paste your emoji here
emo = emoji.demojize("😒")


################### Call functions from here ############################
# Just call a function as shown below and tweak the parameters as you wish to have
# keepTypingMessages(100, comments)
# keepTypingEmojis(100, emo, 4)
