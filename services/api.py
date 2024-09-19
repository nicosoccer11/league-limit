import requests
from datetime import datetime, timedelta

class RiotAPIService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_puuid(self, summoner_name: str, tagline: str) -> str:
        ''' 
        Returns the PUUID of the given summoner name and tagline
        '''
        url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tagline}?api_key={self.api_key}'
        response = requests.get(url)
        return response.json()['puuid']

    def get_most_recent_match_by_puuid(self, puuid: str) -> str:
        ''' 
        Returns the players most recent match based on their PUUID
        '''
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={self.api_key}'
        response = requests.get(url)
        return response.json()[0]

    def get_match_results_and_date(self, match_id: str, puuid: str) -> bool:
        ''' 
        Returns the match results (win(T)/loss(F)) of the given matchId for the given PUUID
        '''
        url = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.api_key}'
        response = requests.get(url)
        particpants = response.json()['info']['participants']
        gameEndUnix = response.json()['info']['gameEndTimestamp']
        for i in range(len(particpants)):
            if particpants[i]['puuid'] == puuid:
                return particpants[i]['win'], gameEndUnix

    @staticmethod   
    def get_seconds_until_6am() -> int:
        '''
        Returns the number of seconds remaining until 6am
        '''
        now = datetime.now()
        # Calculate the target time, which is 6 AM of the next day
        target_time  = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1, hours=6)

        seconds_until_6am = (target_time - now).total_seconds()

        return int(seconds_until_6am)
    
    @staticmethod
    def get_date() -> datetime.date:
        '''
        Gets the current date
        '''
        now = datetime.now()

        return str(now.date())

    @staticmethod
    def unix_to_date(unix_time: int) -> str:
        ''' 
        Converts a Unix timestamp in milliseconds to a human-readable date.
        '''
        # Convert milliseconds to seconds
        unix_time_seconds = unix_time / 1000
        
        return datetime.fromtimestamp(unix_time_seconds).strftime('%Y-%m-%d %H:%M:%S')

