from requests import get
from lesson_24.swapi import config

class StarshipService:
    def __init__(self):
        self.__starship_url = f"{config['host1']}starships/"

    def get_all_starships(self, page=1):
        return get(f'{self.__starship_url}?page={page}')

    def get_single_starships(self, id=41):
        return get(f'{self.__starship_url}?page={page}')