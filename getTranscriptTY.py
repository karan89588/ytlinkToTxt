from youtube_transcript_api import YouTubeTranscriptApi as yta


def getResp(video_id):
    data = yta.get_transcript(video_id)
    transcript = ""
    for value in data:
        for key, val in value.items():
            if key == "text":
                transcript += val
        l = transcript.splitlines()
        source = " ".join(l)
    return source
