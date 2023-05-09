import pandas as pd
from youtube_comment_downloader import *
import json
# import emoji

name = 'comments'
downloader = YoutubeCommentDownloader()
# comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=ScMzIvxBSi4')
# comments = downloader.get_comments_from_url(
#     'https://www.youtube.com/watch?v=KzN9GFuiHLw')
comments = downloader.get_comments('KzN9GFuiHLw')
with open(f"{name}.json", 'w') as f:
    for comment in comments:
        # comment['text'] = emoji.demojize(comment['text'], delimiters=('', ''))
        json.dump(comment, f)
        f.write('\n')

# Baca file input dan muat ke dalam DataFrame
df = pd.read_json(f"{name}.json", lines=True)
# Tulis DataFrame ke dalam file CSV
df.to_csv(f"{name}.csv", index=False)
