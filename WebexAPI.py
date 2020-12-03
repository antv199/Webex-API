import pyautogui, time, pyperclip, random

respones=["Καλημέρα!", "καλημέρα", "γειά σας"]
SkinMode="Dark" #Dark and Light

def Join(url):
    JoinButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/JoinMeeting.png', grayscale=True, confidence=0.7)
    if JoinButton:
        click(JoinButton,1)

def Leave():
    LeaveButton=pyautogui.locateCenterOnScreen('resources/ExitMeeting.png', grayscale=True, confidence=0.9)
    if LeaveButton:
        click(LeaveButton,1)
        time.sleep(1)
        LeaveButton=pyautogui.locateCenterOnScreen('resources/ConfirmLeave.png', grayscale=True, confidence=0.9)
        if LeaveButton:
            click(LeaveButton,1)

def click(OBJ,nclicks):
    pyautogui.moveTo(OBJ)
    pyautogui.click(OBJ, clicks=nclicks)

def Type(obj,msg):
        click(obj,1)
        pyperclip.copy(msg)
        pyautogui.hotkey("ctrl", "v")
        #pyautogui.press("enter")


def GetWaitStatus():
    status=0
    WaitStatus=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/WaitingForHost.png', grayscale=True, confidence=0.9)

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

def Microphone(mute: bool) -> int:
    res=0 #0 Failed, 1 Success, 2 Mic is locked by host, 3 Already muted

    if mute:
        MicButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/MuteButton.png', grayscale=True, confidence=0.9)
        if not MicButton: #If it isn't 
            MicButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/MuteButton.png', grayscale=True, confidence=0.9)
            if MicButton:
                res=2
                


def Video():
    VideoButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/StopVideoButton.png', grayscale=True, confidence=0.9)
    if VideoButton:
        click(VideoButton,1)

EnterMessage=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/EnterMessage.png', grayscale=True, confidence=1)
ChatCollapsed=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/ChatCollapsed.png', grayscale=True, confidence=0.9)
if not EnterMessage:
    print("Opening Chat")
    if not ChatCollapsed:
        ChatButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/ChatButton.png', grayscale=True, confidence=0.9)
        if ChatButton:
            click(ChatButton,1)
            time.sleep(1)
    else:
        click(ChatCollapsed,2)

    EnterMessage=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/EnterMessage.png', grayscale=True, confidence=0.9)
    Type(EnterMessage, respones[int(random.uniform(0,2))])
elif ChatCollapsed:
    click(ChatCollapsed,2)
    Type(EnterMessage, respones[random.uniform(0,2)])
else:
    Type(EnterMessage, respones[random.uniform(0,2)])

def Hand(Raise):
    Me=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/Me.png', grayscale=True, confidence=0.9)
    
    if Raise:
        click(Me,1)
        HandR=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/RaiseHand.png', grayscale=True, confidence=0.9)
        click(HandR,1)
    else:
        HandR=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/HandRaisedSelected.png', grayscale=True, confidence=0.9)
        if not HandR:
            HandR=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/HandRaisedUnselected.png', grayscale=True, confidence=0.9)
        if not HandR: #Again...
            print("Maybe the hand wasn't risen in the first place?!")