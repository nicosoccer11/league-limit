import app

def main():
    #Unblock the league client
    app.block_league_client_windows(path_to_client = r"C:\Riot Games\Riot Client\RiotClientServices.exe", block = False)

    #TODO: Add additional logic to make it hard to unblock the client

if __name__ == '__main__':
    main()