import pyautogui, time

def click(OBJ):
    pyautogui.moveTo(OBJ)
    pyautogui.click(OBJ)

JoinButton=pyautogui.locateCenterOnScreen('resources/JoinMeeting.png', grayscale=True, confidence=0.7)
if JoinButton:
    click(JoinButton)

time.sleep(3)
MicButton=pyautogui.locateCenterOnScreen('resources/MuteButton.png', grayscale=True, confidence=0.9)
VideoButton=pyautogui.locateCenterOnScreen('resources/StopVideoButton.png', grayscale=True, confidence=0.9)

if MicButton:
    click(MicButton)
if VideoButton:
    click(VideoButton)