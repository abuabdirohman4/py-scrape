import pandas as pd
from youtube_comment_downloader import *
import json

youtubeId = input("Masukkan Youtube ID: ")
name = input("Berikan Nama Untuk File Hasil Download: ")

downloader = YoutubeCommentDownloader()
comments = downloader.get_comments(youtubeId)
with open(f"{name}.json", 'w') as f:
    for comment in comments:
        json.dump(comment, f)
        f.write('\n')

df = pd.read_json(f"{name}.json", lines=True)
df.to_csv(f"{name}.csv", index=False)