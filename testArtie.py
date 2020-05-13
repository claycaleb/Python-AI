import speech_recognition as sr
from recognize_speech import recognize_speech_from_mic
from artie import artie_says

def main():

    r = sr.Recognizer()
    mic = sr.Microphone()

    artie_says("Say something!")

    transcript = recognize_speech_from_mic(r, mic)

    print(transcript)

    artie_says(f'I think you said {transcript}.')


if __name__ == "__main__":
    main()