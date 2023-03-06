import os
from googleapiclient.discovery import build
import json

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:

    def __init__(self, id):
        self.__id = id
        self.info = youtube.channels().list(id=id, part='snippet,statistics').execute()
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']["description"]
        self.url = f'https://www.youtube.com/channel/{self.__id}'
        self.subscriber_count = self.info['items'][0]['statistics']["subscriberCount"]
        self.video_count = self.info['items'][0]['statistics']["videoCount"]
        self.view_count = self.info['items'][0]['statistics']["viewCount"]

    def print_info(self):
        channel_id = self.__id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service(self):
        return build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def to_json(cls, name):
        file = open(name, "w+")
        channel_id = cls.get_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return file.write(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def get_id(self):
        return self.__id

    def __str__(self):
        return f"Youtube-канал: {self.title}"

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count


# chn1 = Channel("UC2Ru64PHqW4FxoP0xhQRvJg")
# chn2 = Channel("UC8M5YVWQan_3Elm-URehz9w")
# print(chn1.title)
# print(chn1.print_info())
# print(chn1.video_count)
# print(chn1.url)
# print(chn1.get_service())
# chn1.to_json('chn1.json')
# print(chn1)
# print(chn2)
# print(chn1 > chn2)
# print(chn1 < chn2)
# print(chn1 + chn2)
