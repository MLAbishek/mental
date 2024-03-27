import transformers
import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
with sr.Microphone() as source2:
    print("Hi welcome to our app")
    r.adjust_for_ambient_noise(source2,duration=2)
    print('speak now')
    audio2=r.listen(source2)
    text=r.recognize_google(audio2)
    text=text.lower()
    print(text)
classifier=transformers.pipeline('sentiment-analysis')
ans=classifier.predict(text)
mood=ans[0]
mood=mood['label'].lower()
if mood=='negative':
    print('User has mental issues')
else:
    print("user is okay")