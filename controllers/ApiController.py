import sys
from flask import render_template, redirect, url_for, request, json, current_app
from models.Video import Video
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import threading
import atexit

POOL_TIME = 10 #Seconds
THREAD_LIMIT = 3
api_response = {}
data_lock = threading.Lock()
your_thread = threading.Thread()
thread_count = 0
db = SQLAlchemy()

def index():
    initialize_threading()
    atexit.register(interrupt)
    return render_template('api.html')

def initialize_threading():
    global your_thread
    your_thread = threading.Timer(0, call_api_and_store, args=(current_app.app_context(),)) #Starts the initial threadding with 0 secs
    your_thread.start()

def call_api_and_store(app_context):
    app_context.push()
    global api_response
    global thread_count
    global data_lock
    # print("Thread : starting $i", thread_count)
    thread_count += 1
    with data_lock:
        api_response = youtube_api_call()
        validate_and_insert_in_db(api_response)
    if thread_count < THREAD_LIMIT: #Limits thread counts
        your_thread = threading.Timer(POOL_TIME, call_api_and_store, args=(current_app.app_context(),))
        your_thread.start()   

def interrupt():
    global your_thread
    your_thread.cancel()

def youtube_api_call():
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part' : 'snippet',
        'q' : 'football',
        'fields' : 'items(id,snippet)',
        'type' : 'video',
        'order': 'date',
        'publishedAfter': datetime.now().strftime("%Y-%m-%dT%H:00:00Z"),
        'key' : current_app.config["YOU_TUBE_DATA_API_KEY"]
    }
    response = requests.get(search_url, params)
    return response.json()

def validate_and_insert_in_db(response):
    # response = json.load(open('static/data.json'))
    for videos in response['items']:
        if 'videoId' not in videos['id']:
            continue
        video_id = videos['id']['videoId']
        for key,value in videos['snippet'].items():
            if key == 'publishedAt':
                published_at = value
            elif key == 'title':
                title = value
            elif key == 'description':
                description = value
            elif key == 'thumbnails':
                thumbnails = value['high']['url']
        if video_id is not None:
            video_details = Video.query.filter_by(video_id=video_id).first()
            if video_details is None:
                insert_data = Video(video_id=video_id, title=title, description=description, publish_datetime=datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ"), thumbnail_url=thumbnails)
                db.session.add(insert_data)
                db.session.commit()
    # print("Thread : ending")
    