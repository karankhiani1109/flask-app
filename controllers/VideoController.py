import sys
from flask import render_template, redirect, url_for, request, json, current_app
from models.Video import Video
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime
# config.from_object('config')
db = SQLAlchemy()

def index():
    # return "200"
    # search_url = "https://www.googleapis.com/youtube/v3/search"
    # params = {
    #     'part' : 'snippet',
    #     'q' : 'cricket',
    #     'fields' : 'items(id,snippet)',
    #     'key' : current_app.config["YOU_TUBE_DATA_API_KEY"]
    # }
    # response = requests.get(search_url, params)
    # json_url = os.path.join(SITE_ROOT, "static/data", "data.json")
    response = json.load(open('static/data.json'))
    for videos in response['items']:
        if 'videoId' not in videos['id']:
            continue
        video_id = videos['id']['videoId']
        print(video_id)
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
    return "200"
    # response = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyB6_8ULZDIhVMGEogqAne_PNhZSk7TpgR0&part=snippet&q=cricket&fields=items(id,snippet)").json()
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "/static", "data.json")
    # response = json.load(open(json_url))
    # for each in response['items'][0].items():
    #     print("okk")
    # return render_template('index2.html', response=response)
