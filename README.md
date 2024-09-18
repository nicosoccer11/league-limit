# League Client Blocker

This is a for fun personal script I wrote that automatically manages access to the League of Legends client based on recent match results.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the Repository:**

- SSH    
    git clone git@github.com:nicosoccer11/league-limit.git
    cd league-limit
- HTTPS
    git clone https://github.com/nicosoccer11/league-limit.git
    cd league-limit

2. **(Optional) Create a Virtual Environment:**

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Required Packages:**

    pip install -r requirements.txt

4. **Create a .env file:**

    Create a .env file in the root of your project directory with the following content:

    API_KEY='your-api-key'
    SUMMONER_NAME='your-summoner-name'
    TAGLINE='your-tagline'
    PATH=r'C:\Riot Games\Riot Client\RiotClientServices.exe'

## Running the Scripts

### Blocking the League Client

The main script, `main.py`, blocks the League client based on your most recent match results.

To run the script and block access:

```sh
python main.py
```

### Unblocking the League Client

```sh
python unblock.py
```