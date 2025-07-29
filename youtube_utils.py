from googleapiclient.discovery import build

# Replace with your actual API key
API_KEY = 'AIzaSyDDpZGK5JAXQkHUM05_Uw3TGMEHQHmGOLs'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_channel_stats_by_name(youtuber_name):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    # Step 1: Search for channel by name
    search_response = youtube.search().list(
        q=youtuber_name,
        part='snippet',
        type='channel',
        maxResults=1
    ).execute()

    if not search_response['items']:
        return None  # No channel found

    channel_id = search_response['items'][0]['snippet']['channelId']
    channel_title = search_response['items'][0]['snippet']['title']

    # Step 2: Fetch stats using channel ID
    stats_response = youtube.channels().list(
        part='statistics,snippet',
        id=channel_id
    ).execute()

    stats = stats_response['items'][0]['statistics']
    snippet = stats_response['items'][0]['snippet']

    return {
        'channel_id': channel_id,
        'channel_title': channel_title,
        'subscribers': stats.get('subscriberCount'),
        'total_views': stats.get('viewCount'),
        'video_count': stats.get('videoCount'),
        'thumbnail': snippet.get('thumbnails', {}).get('default', {}).get('url'),
        'description': snippet.get('description')
    }
