import os
from googleapiclient.discovery import build
import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:

    def __init__(self, id):
        self.__id = id
        self.info = []
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

    def print_info(self):
        channel_id = self.__id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service(self):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, name):
        file = open(name, "w+")
        channel_id = self.__id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return file.write(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_info(self):
        info = []
        channel_id = self.__id
        info.append(youtube.channels().list(id=channel_id, part='snippet,statistics').execute())
        for i in info:
            for y in i['items']:
                self.title = y['snippet']['title']
                self.description = y['snippet']["description"]
                self.subscriber_count = y['statistics']["subscriberCount"]
                self.video_count = y['statistics']["videoCount"]
                self.view_count = y['statistics']["viewCount"]
        self.url = f'https://www.youtube.com/channel/{self.__id}'

    @property
    def get_id(self):
        return self.__id


chn1 = Channel("UC2Ru64PHqW4FxoP0xhQRvJg")
chn1.get_info()
print(chn1.title)
print(chn1.video_count)
print(chn1.url)
print(chn1.get_service())
chn1.to_json('chn1.json')
