from pynput.keyboard import Key, Controller, KeyCode
from MusicPlayerAutomation import output
import speech_recognition as sr


keyboard = Controller()
# Methods(Start)
def virtualCode(code):
	kc = KeyCode()
	vc = kc.from_vk(code)
	return vc

def pressButton(code):
	keyboard.press(virtualCode(code))
	keyboard.release(virtualCode(code))

def usrInput():
	recog = sr.Recognizer()
	with sr.Microphone() as source:
		audio = recog.listen(source)
		text_of_audio = recog.recognize_google(audio)
		return text_of_audio
		# return recog.recognize_google(recog.listen(source))
# Method(End)
def main():
	#Main Program  
	keycodes = {
		"playPause" : 179,
		"forward" : 176,
		"back" : 177
	}

	stop = False
	output("What would you like to do: ")
	while not stop:
		userInput = usrInput()
		typedInput = input("Type stop to 'stop' the program: ")
		for keycode in keycodes:
			if userInput.lower() == "play" or userInput.lower() == "pause":
				pressButton(keycodes["playPause"])
			elif userInput.lower() == keycode:
				pressButton(keycodes[keycode])
		output("Anything else: ")
		if userInput.lower() == "stop" or typedInput.lower() == "stop":
			stop = True
			output("The Program has stopped working!")

if __name__ == '__main__':
	main()