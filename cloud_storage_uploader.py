from google.cloud import storage
from pathlib import Path

storage_client = storage.Client()
bucket = storage_client.get_bucket('pit_transcriptions')

path = Path('./transcript_pablo/flac')
prefix = 'pablo'
for p in path.iterdir():
    dest_name = (p.name)
    dest_blob = bucket.blob(f'{prefix}/{dest_name}')
    dest_blob.upload_from_filename(str(p))
