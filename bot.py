import pyautogui, time, pyperclip

def click(OBJ,nclicks):
    pyautogui.moveTo(OBJ)
    pyautogui.click(OBJ, clicks=nclicks)

def Type(obj,msg):
        click(obj,1)
        pyperclip.copy(msg)
        #pyautogui.hotkey("ctrl", "v")
        #pyautogui.press("enter")

def GetWaitStatus():
    WaitStatus=pyautogui.locateCenterOnScreen('resources/WaitingForHost.png', grayscale=True, confidence=0.9)
    status=0

    if WaitStatus:
        print("Host didn't join yet")
        status=1
    if not WaitStatus:
        WaitStatus=pyautogui.locateCenterOnScreen('resources/WaitForHostAdmission.png', grayscale=True, confidence=0.9)
        if WaitStatus:
            print("Waiting to be accepted...")
            status=2
    else:
        print("Either you are already in, or you are just not in yet.")
        status=0
    
    return status

JoinButton=pyautogui.locateCenterOnScreen('resources/JoinMeeting.png', grayscale=True, confidence=0.7)
if JoinButton:
    click(JoinButton,1)

WaitingStatus=GetWaitStatus()

while (WaitingStatus==1 or WaitingStatus==2):
    WaitingStatus=GetWaitStatus()

time.sleep(3)
MicButton=pyautogui.locateCenterOnScreen('resources/MuteButton.png', grayscale=True, confidence=0.9)
VideoButton=pyautogui.locateCenterOnScreen('resources/StopVideoButton.png', grayscale=True, confidence=0.9)

if MicButton:
    click(MicButton,1)
if VideoButton:
    click(VideoButton,1)

EnterMessage=pyautogui.locateCenterOnScreen('resources/EnterMessage.png', grayscale=True, confidence=1)
ChatCollapsed=pyautogui.locateCenterOnScreen('resources/ChatCollapsed.png', grayscale=True, confidence=0.9)
if not EnterMessage:
    print("Opening Chat")
    if not ChatCollapsed:
        ChatButton=pyautogui.locateCenterOnScreen('resources/ChatButton.png', grayscale=True, confidence=0.9)
        if ChatButton:
            click(ChatButton,1)
            time.sleep(1)
    else:
        click(ChatCollapsed,2)

    EnterMessage=pyautogui.locateCenterOnScreen('resources/EnterMessage.png', grayscale=True, confidence=0.9)
    Type(EnterMessage, "Καλημέρα!")
elif ChatCollapsed:
    click(ChatCollapsed,2)
    Type(EnterMessage, "Καλημέρα!")
else:
    Type(EnterMessage, "Καλημέρα!")

def Hand(Raise):
    Me=pyautogui.locateCenterOnScreen('resources/Me.png', grayscale=True, confidence=0.9)
    
    if Raise:
        click(Me,1)
        HandR=pyautogui.locateCenterOnScreen('resources/RaiseHand.png', grayscale=True, confidence=0.9)
        click(HandR,1)
    else:
        HandR=pyautogui.locateCenterOnScreen('resources/HandRaisedSelected.png', grayscale=True, confidence=0.9)
        if not HandR:
            HandR=pyautogui.locateCenterOnScreen('resources/HandRaisedUnselected.png', grayscale=True, confidence=0.9)
        if not HandR: #Again...
            print("Maybe the hand wasn't risen in the first place?!")