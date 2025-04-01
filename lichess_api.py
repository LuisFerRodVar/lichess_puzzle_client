import requests


def get_puzzle():
    url = "https://lichess.org/api/puzzle/next"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pgn = data["game"]["pgn"]
        solution = data["puzzle"]["solution"]
        return (pgn, solution)
    return None
