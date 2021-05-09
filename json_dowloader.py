from requests import api
import json

limite = (4, 12)
# def get_cep(cep):
#     print(cep is not str)
#     print(len(cep)>8)
#     if cep is not str and len(cep)!=8:
#         raise FileNotFoundError
#     resposta = api.get(f"http://viacep.com.br/ws/{cep}/json/", timeout = limite)
#     if resposta.status_code == 404:
#         raise FileNotFoundError

#     return resposta.json()
site_pokeapi = "http://pokeapi.co"
def pokedex(numero):
    if 1 > numero or numero> 5000:
        raise FileNotFoundError
    resposta = api.get(f"{site_pokeapi}/api/v2/pokemon/{numero}/", timeout = limite)
    if resposta.status_code == 404:
        raise FileNotFoundError

    with open("./json/pokemon.json",'w') as file:
        json.dump(resposta.json(), file)


def load_json(json_file):
    with open(json_file) as file:
        data = json.load(file)
        file.close()
    return data

