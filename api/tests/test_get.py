"""import requests

# Testing if the endpoint is correct
url_pets = 'http://localhost:8000/pet'


class TestPets:
    url_pets = 'http://localhost:8000/pet'

    def test_get_pets(self):
        result = requests.get(url=url_pets)

        assert result.status_code == 200
        assert result.json()[0]['category'] == 'dog'



"""

