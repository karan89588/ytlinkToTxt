import openai


def getText(filename):
    openai.api_key = "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"
    audio_path = filename
    audio_file = open(audio_path, "rb")
    print(audio_file)
    response = openai.Audio.transcribe("whisper-1", audio_file)
    return response.text


if __name__ == "__main__":
    print(getText("../292-colonial-williamsburg.mp3"))
