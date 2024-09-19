from services import RiotAPIService, LeagueBlockerService
from config import SUMMONER_NAME, TAGLINE, PATH, API_KEY

def initialize_services():
    api_service = RiotAPIService(api_key=API_KEY)
    blocker_service = LeagueBlockerService(path_to_client=PATH)
    return api_service, blocker_service

def check_and_block(api_service: RiotAPIService, blocker_service: LeagueBlockerService):
    try:
        # Get summoner PUUID
        puuid = api_service.get_puuid(SUMMONER_NAME, TAGLINE)

        # Get most recent match by PUUID
        match_id = api_service.get_most_recent_match_by_puuid(puuid)

        # Get match results (win(T)/loss(F)) and match end date
        match_result, game_end_unix = api_service.get_match_results_and_date(match_id, puuid)
        unix_to_date = api_service.unix_to_date(game_end_unix)

        # Check if the match result is a loss and if it occurred today
        if not match_result and unix_to_date[:10] == api_service.get_date():
            blocker_service.prevent_league_access()
        else:
            print("Have not lost today\n")

    except Exception as e:
        print(f"An error occurred: {e}\n")
    
def unblock_client(blocker_service: LeagueBlockerService):
    try:
        blocker_service.block_league_client_windows(block=False)
        print("Client unblocked successfully\n")
    except Exception as e:
        print(f"An error occurred while unblocking: {e}\n")

# def main():
#     api_service, blocker_service = initialize_services()
#     check_and_block(api_service, blocker_service) 

#     #Unblock the league client
#     #blocker_service.block_league_client_windows(path_to_client = r"C:\Riot Games\Riot Client\RiotClientServices.exe", block = False)

#     #TODO: password protection / challenge system for unblocking (makes it harder to unblock, self control mech)

#     #TODO: rule based blocking (lose 1 or 2 or 3 ...etc)

#     #TODO: riot api key troubles


# if __name__ == '__main__':
#     main()
