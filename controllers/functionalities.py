from services import RiotAPIService, LeagueBlockerService
from config import API_KEY
import json

def save_user_data(username, tagline, path):
    user_data = {
        "username": username,
        "tagline": tagline,
        "path_to_cient": path
    }
    with open('user_data.json', 'w') as f:
        json.dump(user_data, f)

def load_user_data():
    try:
        with open('user_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None  # Return None if no user data is found

def initialize_services():
    user_data = load_user_data()
    if not user_data:
        print("No user data found. Please provide summoner name, tagline, and path.")
        return None, None

    # Load path_to_client from the user data
    path_to_client = user_data.get("path_to_client")
    if not path_to_client:
        print("Path to client not found in user data.")
        return None, None

    api_service = RiotAPIService(api_key=API_KEY)
    blocker_service = LeagueBlockerService(path_to_client=path_to_client)
    return api_service, blocker_service

def check_and_block(api_service: RiotAPIService, blocker_service: LeagueBlockerService):

    user_data = load_user_data()
    if not user_data:
        print("User data not available. Cannot proceed with blocking.")
        return

    # Get summoner name and tagline from the user data
    summoner_name = user_data.get("username")
    tagline = user_data.get("tagline")

    try:
        # Get summoner PUUID
        puuid = api_service.get_puuid(summoner_name, tagline)

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

