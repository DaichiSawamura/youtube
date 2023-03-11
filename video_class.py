import os
from googleapiclient.discovery import build
import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.info = youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        self.title = self.info['items'][0]['snippet']['title']
        self.like_count = self.info['items'][0]['statistics']["likeCount"]
        self.view_count = self.info['items'][0]['statistics']["viewCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_name = self.playlist['items'][0]['snippet']['title']

    def __str__(self):
        return f'{self.title} ({self.playlist_name})'
