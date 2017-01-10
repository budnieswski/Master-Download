from __future__ import unicode_literals
import youtube_dl
import sys

class CustomLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def CustomHook(d):
    if d['status'] == 'downloading':
        text = '[download] {0} at {1}KiB/s ETA {2}'
        print(text.format(d['_percent_str'], d['_speed_str'], d['_eta_str']), end='\r', flush=True)

    if d['status'] == 'error':
        print('Error ...')

    if d['status'] == 'finished':
        print('\nDone downloading, now converting ...', end='\r')



ydl_opts = {
    'format': 'bestaudio/best',
    'logger': CustomLogger(),
    'progress_hooks': [CustomHook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([
        'https://www.youtube.com/watch?v=XlTWdlVkm88', # 2min
        'https://www.youtube.com/watch?v=Tkk2ZwXRoA4', # 1hr
        'http://www.youtube.com/watch?v=BaW_jenozKc', # test
    ])
