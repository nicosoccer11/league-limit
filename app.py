import requests
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

def get_match_results(match_id: str, puuid: str) -> bool:
    ''' 
    Returns the match results (win(T)/loss(F)) of the given matchId for the given PUUID
    '''
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}'
    response = requests.get(url)
    particpants = response.json()['info']['participants']
    for i in range(len(particpants)):
        if particpants[i]['puuid'] == puuid:
            return particpants[i]['win']

def get_seconds_until_6am() -> int:
    '''
    Returns the number of seconds remaining until 6am
    '''
    now = datetime.now()
    # Calculate the target time, which is 6 AM of the next day
    target_time  = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1, hours=6)

    seconds_until_6am = (target_time - now).total_seconds()

    return int(seconds_until_6am)
