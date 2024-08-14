import requests
import os
import subprocess
import time
from datetime import datetime, timedelta
from config import API_KEY

def get_puuid(summoner_name: str, tagline: str) -> str:
    ''' 
    Returns the PUUID of the given summoner name and tagline
    '''
    url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tagline}?api_key={API_KEY}'
    response = requests.get(url)
    return response.json()['puuid']

def get_most_recent_match_by_puuid(puuid: str) -> str:
    ''' 
    Returns the players most recent match based on their PUUID
    '''
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={API_KEY}'
    response = requests.get(url)
    return response.json()[0]

def get_match_results_and_date(match_id: str, puuid: str) -> bool:
    ''' 
    Returns the match results (win(T)/loss(F)) of the given matchId for the given PUUID
    '''
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}'
    response = requests.get(url)
    particpants = response.json()['info']['participants']
    gameEndUnix = response.json()['info']['gameEndTimestamp']
    for i in range(len(particpants)):
        if particpants[i]['puuid'] == puuid:
            return particpants[i]['win'], gameEndUnix
        
def get_seconds_until_6am() -> int:
    '''
    Returns the number of seconds remaining until 6am
    '''
    now = datetime.now()
    # Calculate the target time, which is 6 AM of the next day
    target_time  = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1, hours=6)

    seconds_until_6am = (target_time - now).total_seconds()

    return int(seconds_until_6am)

def get_date() -> datetime.date:
    '''
    Gets the current date
    '''
    now = datetime.now()

    return str(now.date())

def unix_to_date(unix_time: int) -> str:
    ''' 
    Converts a Unix timestamp in milliseconds to a human-readable date.
    '''
    # Convert milliseconds to seconds
    unix_time_seconds = unix_time / 1000
    
    return datetime.fromtimestamp(unix_time_seconds).strftime('%Y-%m-%d %H:%M:%S')


def close_league_client():
    '''
    Closes the League of Legends client
    '''
    # This is Windows
    if os.name == 'nt':
        print("Running on Windows")
        subprocess.call(["taskkill", "/F", "/IM", "LeagueClient.exe"])
        subprocess.call(["taskkill", "/F", "/IM", "LeagueClientUx.exe"])
    # This is a Unix-like system (Linux, macOS)
    elif os.name == 'posix':
        print("Running on a Unix-like system")
        subprocess.call(["pkill", "LeagueClient"])
        subprocess.call(["pkill", "LeagueClientUx"])
    else:
        print("Unsupported operating system")

def prevent_league_access(seconds_until_6am):
    # Sleep until 6 AM
    time.sleep(seconds_until_6am)