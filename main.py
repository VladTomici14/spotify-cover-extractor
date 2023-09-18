import cv2
import spotipy
import urllib.request
import numpy as np
from spotipy.oauth2 import SpotifyOAuth

from credentials import CREDENTIALS

class CoverExtractor:
    def __init__(self):
        self.spotify = spotipy.Spotify(oauth_manager=SpotifyOAuth(
            client_id=CREDENTIALS.SPOTIPY_CLIENT_ID,
            client_secret=CREDENTIALS.SPOTIPY_CLIENT_SECRET,
            redirect_uri=CREDENTIALS.SPOTIPY_REDIRECT_URI
        ))

    def url2Image(self, url):

        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return image

    def searchAlbum(self, album_url):
        """
        Searching the album on Spotify
            :param album_id: the album ID, URI or URL
            :return:
        """
        results = self.spotify.album(album_url)

        album_name = results["name"]
        album_artist = results["artists"][0]["name"]
        cover_url = results["images"][0]["url"]

        return album_name, album_artist, cover_url

    def saveAlbumCover(self, url):
        (album_name, album_artist, cover_url) = self.searchAlbum(url)

        album_cover = self.url2Image(cover_url)

        cv2.imwrite(f"covers/{album_name} - {album_artist}.png", album_cover)

def main():
    link = input("enter the album link: ")
    CoverExtractor().saveAlbumCover(link)

if __name__ == "__main__":
    main()
