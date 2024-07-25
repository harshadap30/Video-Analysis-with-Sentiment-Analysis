from flask import Flask, request, render_template, jsonify
from moviepy.editor import VideoFileClip
import whisper_timestamped as whisper
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

app = Flask(__name__)

nltk.download('vader_lexicon')

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def speech_to_text_with_timestamps(audio_path, language="en"):
    audio = whisper.load_audio(audio_path)
    model = whisper.load_model("medium", device="cpu")
    result = whisper.transcribe(model, audio, language=language)
    return result

# def create_text_from_transcription(transcription_data):
#     # Example of handling different formats
#     print(transcription_data)
#     if isinstance(transcription_data, dict) and "transcript" in transcription_data:
#         return " ".join([item["word"] for item in transcription_data["transcript"]])
#     elif isinstance(transcription_data, list):
#         return " ".join([item for item in transcription_data])
#     else:
#         return "Error: Unexpected transcription data format"

def create_text_from_transcription(transcription_data):
    # Example of handling different formats
    print(transcription_data)
    
    if isinstance(transcription_data, dict):
        # Check if transcription_data has a 'transcript' key
        if "transcript" in transcription_data:
            return " ".join([item["word"] for item in transcription_data["transcript"]])
        
        # Check if transcription_data has a 'text' key and 'segments' key
        elif "text" in transcription_data and "segments" in transcription_data:
            # Extract words from the segments
            return " ".join([word["text"] for segment in transcription_data["segments"] for word in segment["words"]])
    
    elif isinstance(transcription_data, list):
        return " ".join([item for item in transcription_data])
    
    else:
        return "Error: Unexpected transcription data format"



def sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_video():
    video_file = request.files['video']
    language = request.form.get('language', 'en')
    video_path = f"./videos/{video_file.filename}"
    audio_path = f"./audios/{video_file.filename}.wav"
    
    if not os.path.exists('./videos'):
        os.makedirs('./videos')
    if not os.path.exists('./audios'):
        os.makedirs('./audios')
    
    # Save video file
    video_file.save(video_path)
    
    # Extract audio and transcribe
    extract_audio(video_path, audio_path)
    transcription_data = speech_to_text_with_timestamps(audio_path, language=language)
    transcribed_text = create_text_from_transcription(transcription_data)
    
    return render_template('result.html', transcript=transcription_data, text=transcribed_text)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    text = request.form['text']
    sentiment_scores = sentiment_analysis(text)
    return render_template('result.html', sentiment=sentiment_scores, text=text)

if __name__ == '__main__':
    app.run(debug=True)
