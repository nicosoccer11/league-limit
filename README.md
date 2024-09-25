# League Client Blocker

This is a for fun personal script I wrote that automatically manages access to the League of Legends client based on recent match results.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the Repository:**

- SSH
    ```sh    
    git clone git@github.com:nicosoccer11/league-limit.git
    cd league-limit
    ```
    
- HTTPS
    ```sh
    git clone https://github.com/nicosoccer11/league-limit.git
    cd league-limit
    ```

2. **(Optional) Create a Virtual Environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Create a .env file:**

    Create a .env file in the root of your project directory with the following content:

    ```ini
    API_KEY='your-api-key'
    ```
## Running the Script

### Running main.py

The main script, `main.py`, pulls up the GUI. From here you can insert your summoner name, id, and path to your client. Then you can block/unblock the League client based on your most recent match results. 
```sh
python main.py
```