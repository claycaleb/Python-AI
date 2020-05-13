import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import credentials

def recognize_speech_from_mic(recognizer, microphone):

    authenticator = IAMAuthenticator(credentials.IBM_KEY)
    speech_to_text = SpeechToTextV1(authenticator = authenticator)

    speech_to_text.set_service_url(credentials.IBM_URL)

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    speech_recognition_results = speech_to_text.recognize(audio = audio.get_wav_data(), content_type = 'audio/wav').get_result()
    transcript = speech_recognition_results['results'][0]['alternatives'][0]['transcript']

    return transcript

