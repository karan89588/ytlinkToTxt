from youtube_transcript_api import YouTubeTranscriptApi as yta


def getResp(video_id):
    l=''
    try:
      l=YouTubeTranscriptApi.list_transcripts(video_id)
      #print('yes')
      list_lang=[transcript.language_code for transcript in l]
      lang='en'
      target_lang='en'
      text=''
      if lang not in list_lang:
        target_lang=list_lang[0]
        transcript=l.find_transcript([list_lang[0]])
        translated_transcript=transcript.translate(lang)
        text_list=translated_transcript.fetch()
        text_list_1=[t['text'] for t in text_list]
        text=' '.join(text_list_1)
      else:
        transcript=l.find_transcript([lang])
        text_list=transcript.fetch()
        text_list_1=[t['text'] for t in text_list]
        text=' '.join(text_list_1)
      #print('target_lang ',target_lang)
      #print('text ',text)
    except:
      print('OOps!!! Either link is incorrect or transcript is disable.')
      return ('na','na')
    return (text,target_lang)
