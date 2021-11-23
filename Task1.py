from pprint import pprint
import requests

your_token = "2619421814940190"


def get_data_hero(search_hero, token):
    hero_dict = dict()
    for name_hero in search_hero:
        url = f' https://superheroapi.com/api/'

        full_url = url + token + "/search/" + name_hero
        r = requests.get(full_url)
        # print(r.url)
        # print(r.status_code)
        hero_json = r.json()
        hero_lst = []
        d = {}
        try:
            for current_hero in hero_json['results']:
                if current_hero['name'] == name_hero:
                    d['id'] = current_hero['id']
                    d['name'] = current_hero['name']
                    d['intelligence'] = current_hero['powerstats']['intelligence']
                    # d['race'] = current_hero['appearance']['race']
                    # d['strength'] = current_hero['powerstats']['strength']
                    # d['speed'] = current_hero['powerstats']['speed']
                    # d['durability'] = current_hero['powerstats']['durability']
                    # d['power'] = current_hero['powerstats']['power']
                    # d['combat'] = current_hero['powerstats']['combat']

                    hero_lst.append(d)
                    hero_dict[name_hero] = hero_lst

        except KeyError:
            print(f' Персонажа  {name_hero} нет')

    return hero_dict


if __name__ == '__main__':
    name = ['Hulk', 'Captain America', 'Thanos', ]  # 'Galactus', 'Star-Lord' 'Captain Marvel'
    hero_result = get_data_hero(search_hero=name, token=your_token + '/')
    max = 0
    for v in hero_result.values():
        if max > int(v[0]['intelligence']):
            continue
        else:
            max = int(v[0]['intelligence'])

    for k, v in hero_result.items():
        if max == int(v[0]['intelligence']):
            print(k, max)