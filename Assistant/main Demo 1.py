import win32com.client #this will make text to voice
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print(" Enter what you want to hear ")
    s= input()
    speaker.Speak(s)
    print("do you want to hear again? \n")
    print(" if yes press 1 \n if no press 2 \n")
    n=int(input())
    if n==1:
        continue
    elif n==2:
        break
        