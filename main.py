from views import MyApp

def main():
    # Initialize and run the GUI
    app = MyApp()
    app.mainloop()

    #Unblock the league client
    #blocker_service.block_league_client_windows(path_to_client = r"C:\Riot Games\Riot Client\RiotClientServices.exe", block = False)

    #TODO: password protection / challenge system for unblocking (makes it harder to unblock, self control mech)

    #TODO: rule based blocking (lose 1 or 2 or 3 ...etc)

    #TODO: riot api key troubles


if __name__ == '__main__':
    main()