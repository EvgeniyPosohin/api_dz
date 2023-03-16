import requests


class Hero:

    def __init__(self,  name, stat=0):
        self.name = name
        self.stat = stat

    def get_stat(self):
        for dict_hero in all_hero:
            if dict_hero['name'] == self.name:
                self.stat = dict_hero['powerstats']
                print(f'{self.name} - {self.stat}')


# теперь можно сравнивать по любому задаваемому аттрибуту
def compare(l_h, attr):
    good = []
    for hero in l_h:
        if [hero.stat[attr], hero.name] in good:
            continue
        else:
            good.append([hero.stat[attr], hero.name])
    top = sorted(good, key=lambda x: x[0], reverse=True)
    print('самый сильный по', attr, ':', top[0][1], end=' ')
    for i in top[1:]:
        if top[0][0] > i[0]:
            return
        else:
            print(f', {i[1]}')


r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
all_hero = r.json()


hero_H = Hero('Hulk')
hero_CA = Hero('Captain America')
hero_Th = Hero('Thanos')

list_hero = [hero_H, hero_CA, hero_Th]

hero_H.get_stat()
hero_Th.get_stat()
hero_CA.get_stat()
compare(list_hero, 'intelligence')
