from pynput import keyboard
from playsound import playsound
import asyncio,os,sys
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
letterToAudio = {
    'a': resource_path(os.path.join('sound', 'a.mp3'))
}
async def ps(audio):
    playsound(sound=audio,block=False)
def onRelease(key):
    if key == keyboard.Key.enter:
        audio = letterToAudio['a']
        print(audio)

        asyncio.run(ps(audio=audio))
listener = keyboard.Listener(on_release=onRelease)
listener.start()
listener.join()