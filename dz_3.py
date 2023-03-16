import requests


class Stackoverflow:

    def get_params(self):
        params = {'fromdate': '1678752000',
                  'todate': '1678924800',
                  'order': 'desc',
                  'sort': 'creation',
                  'tagged': 'python',
                  'site': 'stackoverflow'}
        return params

    def get_questions(self):
        url = "https://api.stackexchange.com//2.3/questions?"
        response = requests.get(url, params=self.get_params())
        question = response.json()
        return question

    def set_question(self):
        for quest in self.get_questions()['items']:
            print(quest['title'])


stackoverflow = Stackoverflow()
stackoverflow.set_question()
