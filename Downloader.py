import os
import sys

class Downloader():
    path_app = os.path.dirname(os.path.realpath(__file__))
    path_lib = path_app + '/lib'
    path_store = path_app + '/storage'


    def start(self):
        self.header()
        self.menu()


    def clear(self):
        """Multi OS prompt cleaner"""
        os.system('cls' if os.name=='nt' else 'clear')


    def header(self):
        """Show default 'header' for visual functions """
        self.clear()
        print("----------------------")
        print("Master video downloader")
        print("----------------------")


    def process(self, choice):
        """Process the choice
        
        [description]
        
        Arguments:
            choice {[type]} -- [description]
        """
        self.header()

        # exit
        if choice == 0:
        sys.exit(0)

        url         = input("URL(s): ")
        path_extra  = input("Extra folder (empty for none): ")
        downloader  = self.path_lib + '/youtube-dl' + ('.exe' if os.name=='nt' else '')

        result = self.execute(choice, downloader, path_extra, url)


    def execute(self, choice, downloader, path_extra, url):
        """Youtube-dl processing

        Arguments:
        choice {integer} -- [description]
        downloader {string} -- [description]
        path_extra {string} -- [description]
        url {string} -- [description]

        Returns:
        [type] -- [description]
        """
        downloader += ' --quiet --no-warnings'
        str_downloader = ''

        if path_extra:
        path_extra += '/'

        if choice == 1: # Video
        str_downloader = "{0} -o \"{1}/single/{2}%(title)s-%(id)s.%(ext)s\" {3}"

        elif choice == 2: # Playlist
        str_downloader = "{0} --yes-playlist -o \"{1}/playlist/{2}%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s\" {3}"

        elif choice == 3: # MP3
        str_downloader = "{0} --extract-audio --audio-format mp3 -o \"{1}/mp3/{2}%(title)s-%(id)s.%(ext)s\" {3}"

        # Executing Youtube-dl
        return os.system(str_downloader.format(downloader, self.path_store, path_extra, url))


    def menu(self):
        """Show menu options || dispatch to processing"""
        print('Choices:\n1 - Video\n2 - Playlist\n3 - To MP3\n0 - Quit')

        choice = int(input("Want: "))

        if not (-1 < choice < 5):
        input('Invalid choice\n')
        self.start()

        self.process(choice)