import requests
import os
import subprocess
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

#Do i need this!?!?      
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

def is_league_running(league_client_name = "LeagueClient.exe") -> bool:
    '''
    Checks if the League of Legends client is running
    '''
    if os.name == 'nt':  # Windows
        # Check for the League client process on Windows
        tasks = subprocess.check_output(["tasklist"], universal_newlines=True)
        return league_client_name in tasks
    else:  # Unix-based
        # Check for the League client process on Unix-based systems
        processes = subprocess.check_output(["ps", "aux"], universal_newlines=True)
        return league_client_name in processes
    
def block_league_client_windows(path_to_client: str, block: bool):
    '''
    Block or unblock the League of Legends client by changing file permissions on Windows
    '''
    if block:
        # Remove execution permissions
        subprocess.call(["icacls", path_to_client, "/deny", "everyone:(RX)"])
    else:
        # Restore execution permissions
        subprocess.call(["icacls", path_to_client, "/grant", "everyone:(RX)"])
        
def prevent_league_access(path_to_client: str):
    '''
    Prevents access to the League of Legends client until 6 AM
    '''

    # Check if the system is running Windows or Unix-based
    is_windows = os.name == 'nt'
    league_client_name = "LeagueClient.exe" if is_windows else "LeagueClient"

    if is_league_running(league_client_name):
        # Close the League client immediately
        close_league_client()

    # Block the League client
    block_league_client_windows(path_to_client, block = True)
    print(f"League client blocked. Will unblock at 6 AM.")
