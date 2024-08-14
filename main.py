import app
from config import SUMMONER_NAME, TAGLINE

def main():

    # Get summoner puuid
    puuid = app.get_puuid(SUMMONER_NAME, TAGLINE)

    # Get most recent match by puuid
    match_id = app.get_most_recent_match_by_puuid(puuid)

    # Get match results (win(T)/loss(F))
    match_result, gameEndUnix = app.get_match_results_and_date(match_id, puuid)
    
    # Get the date of the match
    unix_to_date = app.unix_to_date(gameEndUnix)

    # if match_result is False, and date of match is == to current day close the league client
    if match_result == False and unix_to_date[0:10] == app.get_date():
        app.close_league_client()
    else:
        pass

if __name__ == '__main__':
    main()