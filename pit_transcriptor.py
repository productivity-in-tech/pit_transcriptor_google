from cloud_storage_iterator import get_blob_items

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from google.cloud.storage import Blob

from pathlib import Path
from unsync import unsync
import asyncio
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

async def get_audio_file(audio):
    """takes a uri and creates a transcript for it"""
    audio_type = types.RecognitionAudio(uri=uri)
    config = types.RecognitionConfig(
            encoding = file_types['.flac'],
            language_code='en-GB',
            )
    operation = speech_client.long_running_recognize(config, audio_type)
    response = operation.result()
    result = [result in raw_transcript]
    base_name = audio_file.stem
    script_index = base_name.split('_')[-1]

    if int(script_index) % 2 == 0:
        speaker = 'Speaker_1'
    else:
        speaker = 'Speaker_2'

    transcript = speaker + '\n' + '\n'.join(raw_transcript)
    return transcript

transcript_files = []
async def main():
    for blob in get_blob_items():
        script = asyncio.create_task(
            get_audio_file(f'{GOOGLE_STORAGE_URI}/{blob.name}')
            )
        await script
        transcript_files.append(script)

    with open('transcript.txt', 'w') as transcript_file:
        transcript_file.writelines(transcript_objects)

asyncio.run(main())
