from gtts import gTTS
from io import BytesIO
import pyglet
tts= gTTS(text="hola mundo, como están", lang="es")
tts.save("audio.mp3")
mp3_fp= BytesIO()
tts= gTTS("hola mundo,como estan", "es")
tts.write_to_fp(mp3_fp)

music=pyglet.resource.media("audio.mp3")
music.play()

