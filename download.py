import os
import sys


path = os.path.dirname(os.path.realpath(__file__)) + '\lib'
storage = path + '\storage'


'''
Multi OS prompt cleaner
'''
def clear():
  os.system('cls' if os.name=='nt' else 'clear')


'''
Show default 'header' for visual functions
'''
def header():
  clear()
  print("----------------------")
  print("Master video downloader")
  print("----------------------")


'''
Process the choice
'''
def process(choice):
  header()

  # exit
  if choice == 0:
    sys.exit(0)

  url = input("URL(s): ")
  extraPath = input("Extra folder (empty for none): ")
  downloader = path + '\youtube-dl' + ('.exe' if os.name=='nt' else '.sh')

  if extraPath:
    extraPath += '/'

  if choice == 1: # Video
    os.system("{0} -o \"{1}\single\{2}%(title)s-%(id)s.%(ext)s\" {3}".format(downloader, storage, extraPath, url))

  elif choice == 2: # Playlist
    os.system("{0} --yes-playlist -o \"{1}\playlist\{2}%(playlist)s\%(playlist_index)s - %(title)s.%(ext)s\" {3}".format(downloader, storage, extraPath, url))

  elif choice == 3: # MP3
    os.system("{0} --extract-audio --audio-format mp3 -o \"{1}\mp3\{2}%(title)s-%(id)s.%(ext)s\" {3}".format(downloader, storage, extraPath, url))


'''
Show menu options
'''
def menu():
  header()
  print('Choices:\n1 - Video\n2 - Playlist\n3 - To MP3\n0 - Quit')

  choice = int(input("Want: "))

  if not (-1 < choice < 5):
    input('Invalid choice\n')
    menu()

  process(choice)



menu()