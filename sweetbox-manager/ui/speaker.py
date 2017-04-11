import pyttsx

engine = None


def init():
    pass


def finished_speaking(name, completed):
    print 'finished speaking...'


engine = pyttsx.init()
engine.connect('finished-utterance', finished_speaking)


def say(text):
    engine.say(text)
    engine.runAndWait()


say("hue hue hue. Hello world!")


voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()
