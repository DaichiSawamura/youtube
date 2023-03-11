from video_class import *
import datetime
import isodate


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
                                                            maxResults=50).execute()
        self.playlist_video = youtube.playlistItems().list(playlistId=playlist_id,
                                                                part='contentDetails').execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_video['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        response = youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()
        for video in response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        videos = {}
        for i in range(len(self.video_ids)):
            videos[int(self.video_response['items'][i]['statistics']['likeCount'])] = self.video_ids[i]

        return f"https://www.youtube.com/watch?v={videos[max(videos)]}"


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.title)
print(pl.url)

duration1 = pl.total_duration
print(duration1)
print(type(duration1))
print(duration1.total_seconds())
print(pl.show_best_video())

