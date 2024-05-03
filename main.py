import os
from typing import Dict, Optional
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

MCRT_ID = "4m7q9onIm2bqhwHy9utqmw"

def get_artist_info():
    client_credentials_manager = SpotifyClientCredentials(client_id= os.environ.get("CLIENT_ID"), client_secret=os.environ.get("CLIENT_SECRET"))
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)  
    artist_info = sp.artist(MCRT_ID)
    return artist_info


print(get_artist_info())






