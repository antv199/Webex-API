import pyautogui, time, pyperclip, random, warnings

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

def Chat():
    def Type(obj,msg):
        click(obj,1)
        pyperclip.copy(msg)
        pyautogui.hotkey("ctrl", "v")
        #pyautogui.press("enter")
    
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

class Peripherals():
    def Microphone(enabled: bool) -> int:
        res=0 #0 Failed, 1 Success, 2 Mic is locked by host, 3 Action was already applied before

        if not enabled: #If user wants to mute
            MicButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/MuteButton.png', grayscale=False, confidence=0.9)
            if not MicButton: #If it isn't 
                MicButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/UnmuteButton.png', grayscale=False, confidence=0.9)
                if MicButton:
                    print("Already muted.")
                    res=3
                else:
                    print("User is muted and locked by host.")
                    res=2
            else:
                click(MicButton,1)
                print("Done")
                res=1

        else: #If we want to enable it
            MicButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/UnmuteButton.png', grayscale=False, confidence=0.8)
            if not MicButton:
                MicButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/MuteButton.png', grayscale=False, confidence=0.9)
                if MicButton:
                    print("Mic already enabled.")
                    res=3
                else:
                    print("User is muted and locked by host.")
                    res=2
            else:
                print("Opening Mic...")
                click(MicButton,1)
                res=1
        return res

    def Camera(enabled: bool) -> int:
        res=0
        if not enabled:
            VideoButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/StopVideoButton.png', grayscale=True, confidence=0.9)
            if VideoButton:
                print("Closing Video...")
                click(VideoButton,1)
                res=1
            else:
                print("Camera already closed.")
                res=3
        else:
            VideoButton=pyautogui.locateCenterOnScreen('resources/'+SkinMode+'Mode/StartVideoButton.png', grayscale=True, confidence=0.9)
            if VideoButton:
                print("Enabling Camera...")
                click(VideoButton, 1)
                res=1
            else:
                print("Camera already enabled.")
                res=3
        return res

def Hand(Raise: bool):
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