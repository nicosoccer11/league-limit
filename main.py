import os
import subprocess
import time
import app
from config import SUMMONER_NAME, TAGLINE

def close_league_client():
    if os.name == 'nt':
        # This is Windows
        print("Running on Windows")
        subprocess.call(["taskkill", "/F", "/IM", "LeagueClient.exe"])
        subprocess.call(["taskkill", "/F", "/IM", "LeagueClientUx.exe"])
    elif os.name == 'posix':
        # This is a Unix-like system (Linux, macOS)
        print("Running on a Unix-like system")
        subprocess.call(["pkill", "LeagueClient"])
        subprocess.call(["pkill", "LeagueClientUx"])
    else:
        print("Unsupported operating system")

def prevent_league_access(seconds_until_6am):
    # Sleep until 6 AM
    time.sleep(seconds_until_6am)

def main():

    # Get summoner puuid
    puuid = app.get_puuid(SUMMONER_NAME, TAGLINE)

    # Get most recent match by puuid
    match_id = app.get_most_recent_match_by_puuid(puuid)

    # Get match results (win(T)/loss(F))
    match_result = app.get_match_results(match_id, puuid)

    # if match_result is False, close the league client
    if match_result == False:
        close_league_client
    else:
        pass

if __name__ == '__main__':
    main()