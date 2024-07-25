# Video Transcription and Sentiment Analysis

This project provides a Flask application for video transcription and sentiment analysis. It includes both a web UI and API endpoints that can be tested using Postman.

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. You also need to install the required Python libraries.

bash
pip install -r requirements.txt


#Running the Flask Application
Start the Flask Application:

bash
Copy code
python app.py
Open the Web UI:

Navigate to http://127.0.0.1:5000/ in your web browser.

#Steps for Sentiment Analysis on web browser

1. upload a short video(1-5 minutes)
2. Select Language of your choice
3. WAIT!!!! (this process might take 2-4 minutes depending on your system)
4. Result transcript is generated
5. Click on Analyze Sentiment
6. You will redirected to Sentiment Analysis Result 

#Using Postman
You can use Postman to interact with the API endpoints. Here’s how:

1. Transcribe Video
Endpoint: POST http://127.0.0.1:5000/transcribe
Description: Upload a video file and get the transcribed text with timestamps.
Headers:
Content-Type: multipart/form-data
Body (form-data):
video: [Choose file] (Select the video file to upload)
language: [Optional] (Specify language code, e.g., fr for French)
Example cURL Command:

bash
Copy code
curl -X POST -F "video=@path/to/your/video.mp4" -F "language=fr" http://127.0.0.1:5000/transcribe



To provide clear instructions on how to use Postman with the endpoints provided by your Flask application, you should include detailed documentation in your repository. Here's how you can structure this documentation effectively:

Repository Structure
Make sure your repository has the following structure:

arduino
Copy code
project/
├── app.py
├── automated_transcription_and_sentiment_analysis.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── styles.css
├── README.md
└── requirements.txt
README.md
Here’s a sample README.md file that includes instructions for both using Postman and running the application:

markdown
Copy code
# Video Transcription and Sentiment Analysis

This project provides a Flask application for video transcription and sentiment analysis. It includes both a web UI and API endpoints that can be tested using Postman.

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. You also need to install the required Python libraries.

bash
pip install -r requirements.txt
Running the Flask Application
Start the Flask Application:

bash
Copy code
python app.py
Open the Web UI:

Navigate to http://127.0.0.1:5000/ in your web browser.
Using Postman
You can use Postman to interact with the API endpoints. Here’s how:

1. Transcribe Video
Endpoint: POST http://127.0.0.1:5000/transcribe
Description: Upload a video file and get the transcribed text with timestamps.
Headers:
Content-Type: multipart/form-data
Body (form-data):
video: [Choose file] (Select the video file to upload)
language: [Optional] (Specify language code, e.g., fr for French)
Example cURL Command:

bash
Copy code
curl -X POST -F "video=@path/to/your/video.mp4" -F "language=fr" http://127.0.0.1:5000/transcribe
Response:

json
Copy code
{
  "transcript": [
    {
      "word": "Hello",
      "start_time": 0.0,
      "end_time": 1.0
    },
    ...
  ],
  "text": "Hello world"
}
