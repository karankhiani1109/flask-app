import sys
from flask import render_template, redirect, url_for, request, json, current_app
from models.Video import Video
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import threading
import atexit

POOL_TIME = 10 #Seconds
api_response = {}
data_lock = threading.Lock()
your_thread = threading.Thread()
thread_count = 0
db = SQLAlchemy()

def index():

    # api_response = youtube_api_call()
    # validate_and_insert_in_db(api_response)
    initialize_threading()
    atexit.register(interrupt)
    return "200"
    # response = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyB6_8ULZDIhVMGEogqAne_PNhZSk7TpgR0&part=snippet&q=cricket&fields=items(id,snippet)").json()
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "/static", "data.json")
    # response = json.load(open(json_url))
    # for each in response['items'][0].items():
    #     print("okk")
    # return render_template('index2.html', response=response)

def initialize_threading():
    global your_thread
    your_thread = threading.Timer(0, call_api_and_store, args=(current_app.app_context(),))
    your_thread.start()

def call_api_and_store(app_context):
    app_context.push()
    global api_response
    global thread_count
    global data_lock
    print("Thread : starting $i", thread_count)
    thread_count += 1
    with data_lock:
        api_response = youtube_api_call()
        validate_and_insert_in_db(api_response)
    if thread_count < 3:
        your_thread = threading.Timer(POOL_TIME, call_api_and_store, args=(current_app.app_context(),))
        your_thread.start()   

def interrupt():
    global your_thread
    your_thread.cancel()

def youtube_api_call():
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part' : 'snippet',
        'q' : 'hmm',
        'fields' : 'items(id,snippet)',
        'key' : "AIzaSyB6_8ULZDIhVMGEogqAne_PNhZSk7TpgR0"
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
                thumbnails = value['default']['url']
        if video_id is not None:
            video_details = Video.query.filter_by(video_id=video_id).first()
            if video_details is None:
                insert_data = Video(video_id=video_id, title=title, description=description, publish_datetime=datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ"), thumbnail_url=thumbnails)
                db.session.add(insert_data)
                db.session.commit()
    print("Thread : ending")
    