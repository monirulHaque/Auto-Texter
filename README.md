# Auto-Texter

A simple python automation program to auto type and send messages and emojis.

# Demo

![keepTypingMessages() function Demo](demo/comments.gif)

![keepTypingEmojis() function Demo](demo/emojis.gif)

# Requirements

Install requirements via command

```
pip install pyautogui
pip install emoji
pip install pyperclip
```

# How to use

1. change the `comments` list variable or paste your emoji in `emo` variable where ther is an emoji placed beforehand.
2. Call your desired function with proper parameters as shown below:

```
keepTypingMessages(no. of messages you want to type, comments list or "comments" variable)
```

```
keepTypingEmojis(no. of pyramids you want to type, demojized emoji string or "emo" variable , size of the pyramid):
```

3. Keep Facebook or wherever you want to auto type open.
4. Run the script.
5. Take your cursor in the text field you want to type within 5 seconds.
6. Keep the program open until it stops. Cheers!
