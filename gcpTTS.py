from google.cloud import texttospeech
import os
import io

# setting google CREDENTIALS
# place your own GCP path.
PATH = "E:\Python_Pycharm"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(PATH, 'audiobook_GCP.json')


class Gcp_ttp:
    @classmethod
    def text_to_speech(cls, text):
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-IN",
            name="en-IN-Standard-D",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
        voice1 = texttospeech.VoiceSelectionParams(
            language_code="en-in",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
            name="en-IN-Standard-B"

        )
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        response = client.synthesize_speech(request={"input": input_text, "voice": voice1, "audio_config": audio_config})
        FILEPATH = "audiofiles/"
        with open(FILEPATH + "output.mp3", "wb") as audiofile:
            audiofile.write(response.audio_content)
