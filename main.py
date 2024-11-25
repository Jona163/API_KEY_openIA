#Librerias a ocupar 
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
import openai

# Cargar las variables de entorno
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

# Configuración del asistente
ASSISTANT_NAME = "JARVIS"

# Configurar el motor de texto a voz
engine = pyttsx3.init()

def speak_text(text):
    """Convierte texto a voz usando pyttsx3."""
    engine.say(text)
    engine.runAndWait()

# Inicializamos el reconocedor de voz
recognizer = sr.Recognizer()

def record_text():
    """Graba y reconoce el texto desde el micrófono."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Escuchando...")
        audio = recognizer.listen(source)
        
        try:
            # Convertimos el audio a texto usando reconocimiento de Google
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {text}")
            return text
        except sr.UnknownValueError:
            print("No se entendió el audio, intenta nuevamente.")
        except sr.RequestError as e:
            print(f"No se pudo solicitar los resultados; {e}")
        return None

def send_to_chatgpt(messages):
    """Envía un mensaje a ChatGPT y obtiene la respuesta."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.5
    )
    reply = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": reply})
    return reply

# Ciclo principal de interacción
def main():
    messages = []

    while True:
        text = record_text()
        if text:
            messages.append({"role": "user", "content": text})
            response = send_to_chatgpt(messages)

            # Personalizamos la respuesta del asistente
            response_with_name = f"{ASSISTANT_NAME} dice: {response}"
            speak_text(response_with_name)
            print(response_with_name)

if __name__ == "__main__":
    main()

