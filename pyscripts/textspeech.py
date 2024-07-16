from pygame import mixer
from gtts import gTTS
#import os


def main():
    string = input("Pone el texto a traducir: ")
    tts = gTTS(string)
    out = "audio1"
    os.chdir(r"./audios")
    things = list(os.listdir())
    for aud in things:
        if int(out[-1]) <= int(aud[-4]):
            del out[-1]
            out = out+str(int(aud[-4]) + 1)
            tts.save(out+".mp3")
        else:
            tts.save(out+".mp3")
    mixer.init()
    mixer.music.load('output2.mp3')
    mixer.music.play()
                      
if __name__ == "__main__":
    main()


























