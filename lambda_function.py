import sys
import json
import ffmpeg
import time
from json import loads
from pytubefix import YouTube
from pytubefix.cli import on_progress


def handler(event, context):    

    print(event)
    #json_data = json.loads(event)
    
    try:
        yt = YouTube(event['url'], on_progress_callback=on_progress)

        video_stream = yt.streams.filter(progressive=False, file_extension='mp4', only_video=True).first()

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(progressive=False, file_extension='mp4', only_audio=True).first()

        #get timestamp to append to file. This can be changed to projectid and timestamp later on
        timestamp = str(int(time.time()))
        video_path = '/app/downloads/video-' + timestamp + '.mp4'
        audio_path = '/app/downloads/audio-' + timestamp + '.mp4'
        output_path = '/app/downloads/final-' + timestamp + '.mp4'

        # Download the video and audio streams        
        video_stream.download(output_path='/app/downloads', filename='video-' + timestamp + '.mp4')        
        audio_stream.download(output_path='/app/downloads', filename='audio-' + timestamp + '.mp4')        

       
        input_video = ffmpeg.input(video_path)
        input_audio = ffmpeg.input(audio_path)
        ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output_path).run()

        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }
    except Exception as e:
        return {
            'statusCode': 404,
            'body': json.dumps(str(e))
        }
    


    