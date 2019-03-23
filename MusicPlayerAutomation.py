import pyautogui, time
import pyttsx3


# methods: (Start)
# Speech Syntheizer method configuring the voice output of the program
def output(text):
	engine = pyttsx3.init()
	rate = engine.getProperty("rate")
	engine.setProperty(engine, rate-50)
	engine.say(text)
	engine.runAndWait()
	engine.stop()

# Start Method Opening the VLC media player
def start():
	vlcIcon = pyautogui.locateCenterOnScreen("vlcIcon.PNG")
	if vlcIcon:
		pyautogui.click(vlcIcon)
	else:
		usrInput = input("The Media player is already open! do you want me to close it?: ")
		output("The Media player is already open! do you want me to close it?")
		if usrInput.lower() == "yes":
			stop()
			
# Stopping method Closing 
def stop():
	vlcIcon = pyautogui.locateCenterOnScreen("playingVlcIcon.PNG")
	if vlcIcon:
		pyautogui.click(vlcIcon)
	else:
		output("The Media player is already closed! do you want me to open it?")
		usrInput = input("The Media player is already closed! do you want me to open it?: ")
		if usrInput.lower() == "yes":
			start()


def back():	
	backbutton = pyautogui.locateCenterOnScreen("BackButton.PNG")
	if backbutton:
		pyautogui.click(backbutton)
	else:
		pyautogui.click(pyautogui.moveTo(212, 755))
		time.sleep(1)
		pyautogui.click(pyautogui.locateCenterOnScreen("BackButton.PNG")) 

def forward():
	forwardbutton = pyautogui.locateCenterOnScreen("ForwardButton.PNG")
	if forwardbutton:
		pyautogui.click(forwardbutton)
	else:
		pyautogui.click(pyautogui.moveTo(212, 755))
		time.sleep(1)
		pyautogui.click(pyautogui.locateCenterOnScreen("ForwardButton.PNG")) 


def pause():
	pausebutton = pyautogui.locateCenterOnScreen("PausedButton.PNG")
	if pausebutton:
		pyautogui.click(pausebutton)
	else:
		pyautogui.click(pyautogui.moveTo(212, 755))
		time.sleep(1)
		pyautogui.click(pyautogui.locateCenterOnScreen("PausedButton.PNG"))


def play():
	playbutton = pyautogui.locateCenterOnScreen("PlayButton.PNG")
	if playbutton:
		pyautogui.click(playbutton)
	else:
		pyautogui.click(pyautogui.moveTo(212, 755))
		time.sleep(1)
		pyautogui.click(pyautogui.locateCenterOnScreen("PlayButton.PNG"))
#methods (End)


# main program Start
def main():
	dicto = {
		"start": start,
		"stop": stop,
		"play": play,
		"pause": pause,
		"back": back,
		"forward": forward
	}


	output("What would you like me to do: ")
	# Say the function name one word i.e the function name like pause
	usrInput = input("What would you like me to do: ")
	while usrInput.lower() != "close":
		found = False
		for x in dicto:
			if usrInput.lower() == x:
				dicto[x]()
				found = True

		if found == False:
			output("I cannot operate this function")

		output("Anything else: ")

		usrInput = input("Anything else: ")

if __name__ == '__main__':
	main()
# Main Program End
