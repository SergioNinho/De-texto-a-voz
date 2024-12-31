# De-texto-a-voz
Proyecto Texto a Audio con gTTS y Reproducción con Pyglet Este proyecto convierte texto a voz utilizando la biblioteca gTTS (Google Text-to-Speech) y reproduce el audio utilizando pyglet.
## Requisitos
Python 3.7+

## Bibliotecas:

gtts

io

pyglet

## Instalación
Clona este repositorio.

Instala las bibliotecas necesarias utilizando pip:
```
pip install gtts pyglet
```
## Uso
Para convertir texto a voz y reproducir el audio, puedes utilizar el siguiente código.

## Ejemplo de uso
```
from gtts import gTTS
from io import BytesIO
import pyglet

# Convertir texto a voz y guardar como archivo MP3
tts = gTTS(text="hola mundo, como están", lang="es")
tts.save("audio.mp3")

# Convertir texto a voz y guardar en un objeto BytesIO
mp3_fp = BytesIO()
tts = gTTS("hola mundo, como están", "es")
tts.write_to_fp(mp3_fp)

# Reproducir el archivo MP3 usando pyglet
music = pyglet.resource.media("audio.mp3")
music.play()
```
## Contribución
Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y abre un Pull Request con tus cambios.

## Licencia
Este proyecto está bajo la licencia MIT.
