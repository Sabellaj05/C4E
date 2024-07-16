from pygame import mixer
from gtts import gTTS
from googletrans import Translator

import os

def main():
    translator = Translator(refresh_token=False)
    #Texto
    textovich = input("Pone el texto a traducir: ")
    #Detectar el texto
    #Elegir el idioma a ponerle voz
    ip = int(input("Selecciona el idioma de esta lista por su numero: \n 1.Español\n 2.Ingles\n 3.Aleman\n 4.Mandarin\n\tNumero:  "))
    languages = {1: "es", 2: "en", 3: "de", 4: "zh-CN"}
    #Traducir el texto al idioma que queremos la voz
    texto_traducido = translator.translate(textovich, dest=languages[ip])
    print(texto_traducido)
    tts = gTTS(texto_traducido, lang=languages[ip])
    out = "audio1"
    os.chdir(r"C:\Users\Don\Documents\pyscripts\audios")
    things = list(os.listdir())
    if things:
        latest_file = max(things, key=lambda x: int(x.split('.')[0][5:]))
        latest_number = int(latest_file.split('.')[0][5:])
        out = "audio" + str(latest_number + 1)
    tts.save(out + ".mp3")
    mixer.init()
    try:
    	mixer.music.load(out + ".mp3")
    	mixer.music.play()
    except pygame.error as e:
    	print("Algo fallo AUXILIO:", str(e))
        

if __name__ == "__main__":
    main()







