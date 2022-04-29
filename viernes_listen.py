
import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        text = r.listen(source)    
        try:
            print('Reconociendo...')
            recognised_text = r.recognize_google(text,language="es-MX")
            return recognised_text       
        except sr.UnknownValueError:
            return 'Lo siento, no te entiendo, ¿podrías repetirlo?'
        except sr.RequestError as e:
            return 'Por el momento, no puedo procesar tu solicitud'
            
#listen()