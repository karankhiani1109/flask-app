from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()
class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(1024))
    description = db.Column(db.String(2048))
    publish_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    thumbnail_url = db.Column(db.String(2048))
    created_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'publish_datetime': self.publish_datetime,
            'thumbnail_url': self.thumbnail_url
        }