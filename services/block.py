import os
import subprocess

class LeagueBlockerService:
    def __init__(self, path_to_client: str):
        self.path_to_client = path_to_client

    def close_league_client(self):
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

    def is_league_running(self, league_client_name = "LeagueClient.exe") -> bool:
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
        
    def block_league_client_windows(self, block: bool):
        '''
        Block or unblock the League of Legends client by changing file permissions on Windows
        '''
        if block:
            # Remove execution permissions
            subprocess.call(["icacls", self.path_to_client, "/deny", "everyone:(RX)"])
            
        else:
            # Restore execution permissions
            print(f"Path: {self.path_to_client}")
            subprocess.call(["icacls", self.path_to_client, "/grant", "everyone:(RX)"])
            
    def prevent_league_access(self):
        '''
        Prevents access to the League of Legends client until 6 AM
        '''

        # Check if the system is running Windows or Unix-based
        is_windows = os.name == 'nt'
        league_client_name = "LeagueClient.exe" if is_windows else "LeagueClient"

        if self.is_league_running(league_client_name):
            # Close the League client immediately
            self.close_league_client()

        # Block the League client
        self.block_league_client_windows(block = True)
