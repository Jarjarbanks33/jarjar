import pyautogui, time
time.sleep(5)
f = open("words", 'r')
while True:
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
