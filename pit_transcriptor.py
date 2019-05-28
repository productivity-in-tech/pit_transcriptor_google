from cloud_storage_iterator import get_blob_items

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from google.cloud.storage import Blob

from pathlib import Path
import os
import io
import sys


speech_client = speech.SpeechClient()
# filename = Path(sys.argv[1])

# for loading from the Google Storage URI
GOOGLE_STORAGE_URI = os.environ['GOOGLE_STORAGE_URI']

file_types = {
        '.flac': enums.RecognitionConfig.AudioEncoding.FLAC,
        '.wav': enums.RecognitionConfig.AudioEncoding.LINEAR16,
    }

def get_audio_file(uri):
    """takes a uri and creates a transcript for it"""
    audio_type = types.RecognitionAudio(uri=uri)
    config = types.RecognitionConfig(
            encoding = file_types['.flac'],
            language_code='en-GB',
            )
    operation = speech_client.long_running_recognize(config, audio_type)
    response = operation.result()
    results = [result.alternatives[0].transcript for result in response.results]
    script_index = uri.split(' ')[-1].strip('.flac')

    if int(script_index) % 2 == 0:
        speaker = 'Speaker_1'
    else:
        speaker = 'Speaker_2'

    transcript = speaker + '\n' + '\n'.join(results)
    return transcript

def main():
    transcript_file_list = []
    for blob in get_blob_items():
        uri = f'{GOOGLE_STORAGE_URI}/{blob.name}'
        print(f'getting transcript for {uri}')
        script = get_audio_file(uri)
        transcript_file_list.append(script)

    with open('transcript.txt', 'w') as transcript_file:
        transcript_file.writelines(transcript_file_list)

if __name__ == "__main__":
   main()
