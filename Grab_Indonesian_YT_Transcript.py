from youtube_transcript_api import YouTubeTranscriptApi

# Replace 'video_id' with the actual ID of the YouTube video
video_id = 'ws0z2cLovIA'

try:
    # Fetching the Indonesian transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['id'])

    # Printing the transcript
    for entry in transcript:
        print(entry['text'])
except Exception as e:
    print(f"An error occurred: {e}")
