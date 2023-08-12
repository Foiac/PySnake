import speech_recognition as sr

class speech:

    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def listener(self):
        with self.mic as fonte:
            self.r.adjust_for_ambient_noise(fonte)
            print("Fale alguma coisa")
            audio = self.r.listen(fonte)
            print("Enviando para reconhecimento")
            try:
                text = self.r.recognize_google(audio, language="pt-BR")
                print("Você disse: {}".format(text))

            except:
                print("Não entendi o que você disse")
