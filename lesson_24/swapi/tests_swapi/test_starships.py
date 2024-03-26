


def test_get_starships_without_patametr(starship_service):
    starshios = starship_service.get_all_starships()
    assert starshios.json()["next"] == "https://swapi.dev/api/starships/?page=2"


@pytest.mark.parametrize(['current_page,previous, next'], [(1, None ,"https://swapi.dev/api/starships/?page=2"),
                                                           (2, "https://swapi.dev/api/starships/?page=1", "https://swapi.dev/api/starships/?page=3"),
                                                           (3, "https://swapi.dev/api/starships/?page=2", "https://swapi.dev/api/starships/?page=4"),
                                                           (4, "https://swapi.dev/api/starships/?page=3", None)])
def test_get_starships_with_patametr(starship_service,current_page,previous, next):
    starshios = starship_service.get_all_starships()
    assert starshios.json()["previous"] == previous
    assert starshios.json()["next"] == next

def test_get_single_starship(starship_service)
    starship_service =
