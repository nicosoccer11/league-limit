import requests
from datetime import datetime, timedelta

API_KEY = 'RGAPI-3d6c250f-d0cd-450c-8b3d-587ba820cb6b'
SUMMONER_NAME = 'nicosoccer11'
TAGLINE = '123'

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

def get_match_results(match_id: str, puuid: str) -> str:
    ''' 
    Returns the match results (win/loss) of the given matchId for the given PUUID
    '''
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}'
    response = requests.get(url)
    particpants = response.json()['info']['participants']
    for i in range(len(particpants)):
        if particpants[i]['puuid'] == puuid:
            return particpants[i]['win']

def get_seconds_until_midnight() -> int:
    '''
    Returns the number of seconds remaining until midnight
    '''
    now = datetime.now()
    midnight = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1)

    seconds_until_midnight = (midnight - now).total_seconds()

    return int(seconds_until_midnight)

    

def main():
    puuid = get_puuid(SUMMONER_NAME, TAGLINE)
    match_id = get_most_recent_match_by_puuid(puuid)
    match_result = get_match_results(match_id, puuid)
    print(match_result)
    print(get_seconds_until_midnight())

main()