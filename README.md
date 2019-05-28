## PIT Transcriptor

PIT Transcriptor utilizes the google cloud platform (specifically [Google Speech to Text], and [Google Storage]) to create transcripts of long form audio.

Currently the process requires splitting audio into individual sections based on the where it returns a reliable split between speakers.

## Coming Eventually
* Support for Amazon Transcribe and other transcription tools
* Support for multichannel recognition
* Argument parsing via argparse
* The ability to upload files before processing them
* Asynchronous audio parsing

## Dependencies
* Google Cloud Platform account
* A JSON Credential (Google Cloud) with the path saved to your environments
* Python 3.5+ (Becuase of f'string and {such}')


[Google Speech to Text]: https://cloud.google.com/speech-to-text/docs/reference/libraries#client-libraries-usage-python
[Google Storage]: https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
