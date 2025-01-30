import pandas as pd
from youtube_comment_downloader import *
import json
import time

youtubeId = input("Masukkan Youtube ID: ")
name = input("Berikan Nama Untuk File Hasil Download: ")

print('Downloading Youtube comments for', youtubeId)
downloader = YoutubeCommentDownloader()
comments = list(downloader.get_comments(youtubeId))
print(len(comments))

with open(f"{name}.json", 'w') as f:
    for comment in comments:
        json.dump(comment, f)
        f.write('\n')

df = pd.read_json(f"{name}.json", lines=True)
df.to_csv(f"{name}.csv", index=False)

print('\n[{:.2f} seconds] Done!'.format(time.time() - start_time))
# y08AZxNlxnc