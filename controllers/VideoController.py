import sys
from flask import render_template, redirect, url_for, request, json, current_app, jsonify
from models.Video import Video
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime
db = SQLAlchemy()

def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['PER_PAGE_LIMIT']

    paginated_videos = get_all_videos(page=page, per_page=per_page)
    return render_template('index.html', pagination=paginated_videos)

def filter_submit():
    page = 1
    search_value=request.form['search_query']
    per_page = current_app.config['PER_PAGE_LIMIT']
    if search_value is not None:
        paginated_videos = get_filtered_videos(search_value=search_value, page=page, per_page=per_page)
    else:
        paginated_videos = get_all_videos(page=page, per_page=per_page)
    
    if paginated_videos.pages != 0:
        video_details_view = render_template('video_details.html', pagination=paginated_videos)
        page_number_view = render_template('page_numbers.html', pagination=paginated_videos)
        data = {'success': True, 'page_number_view': page_number_view, 'video_details_view':video_details_view, 'search_value':search_value, 'total_results':paginated_videos.total}
    else:
        data = {'success': True, 'page_number_view': '', 'video_details_view':'', 'search_value':'', 'total_results':paginated_videos.total}
    return jsonify(data)

def get_all_videos(page=0, per_page=5):
    query = Video.query.order_by(Video.publish_datetime.desc()).paginate(page=page, per_page = per_page, error_out=True)
    return query

def get_filtered_videos(search_value, page=0, per_page=5):
    search = "%{}%".format(search_value)
    query = Video.query.filter(Video.title.like(search)).order_by(Video.publish_datetime.desc()).paginate(page=page, per_page = per_page, error_out=True)
    return query
    