from google.cloud import storage
import re

storage_client = storage.Client()

def get_blob_items():
    bucket = storage_client.get_bucket('pit_transcriptions')
    raw_blobs = bucket.list_blobs(prefix='pablo/')
    only_iterables = list(
            filter(lambda x: len(re.findall('\d+', x.name)) > 0,
                raw_blobs))
    blobs = sorted(only_iterables, key=lambda x: int(re.findall('\d+',
        x.name)[0]))
    return blobs


if __name__ == "__main__":
    print(get_blob_items())
