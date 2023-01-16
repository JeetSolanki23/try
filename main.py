from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/connect_to_ai', methods=['POST'])
def connect_to_ai():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    user_input = r.recognize_google(audio)
    engine = pyttsx3.init()
    engine.say("You said: " + user_input)
    engine.runAndWait()
    return "Connected to AI. You said: " + user_input

if __name__ == '__main__':
    app.run()
