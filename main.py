import requests
import datetime
from pprint import pprint

class StackOverFlow():

    def get_all_answers(self):
        params = {
            'order': 'desc',
            'sort': 'activity',
            'site': 'stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.3/answers', params=params).json()
        return response

    def get_all_comments(self):
        params = {
            'order': 'desc',
            'sort': 'creation',
            'site': 'stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.3/comments', params=params).json()
        return response

    def get_all_badges(self):
        params = {
            'order': 'desc',
            'sort': 'rank',
            'site': 'stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.3/badges', params=params).json()
        return response

    def get_all_collectives(self):
        params = {
            'order': 'desc',
            'sort': 'name',
            'site': 'stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.3/collectives', params=params).json()
        return response

    def get_all_articles(self):
        params = {
            'order': 'desc',
            'sort': 'activity',
            'site': 'stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.3/articles', params=params).json()
        return response

    def get_questions_fromday(self, todate, fromdate, tag: str):
        url = 'https://api.stackexchange.com/2.3/questions'
        params = {
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'activity',
            'fromdate': f'{fromdate}',
            'todate': f'{todate}',
            'tagged': tag
        }
        response = requests.get(url, params=params)
        resp = response.json()
        questions = {}
        for items in resp['items']:
            unix_date = items['last_activity_date']
            date = datetime.datetime.utcfromtimestamp(unix_date).strftime('%Y-%m-%d')
            questions.setdefault(items['question_id'], {date: items['link']})

        return questions

    def get_questions_lastday_tag(self, tag: str):
        today = datetime.date.today()
        date = today - datetime.timedelta(1)
        url = 'https://api.stackexchange.com/2.3/questions'
        params = {
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'activity',
            'fromdate': f'{date}',
            'todate': f'{today}',
            'tagged': tag
        }
        response = requests.get(url, params=params)
        resp = response.json()
        questions = {}
        for items in resp['items']:
            unix_date = items['last_activity_date']
            date = datetime.datetime.utcfromtimestamp(unix_date).strftime('%Y-%m-%d')
            questions.setdefault(items['question_id'], {date: items['link']})

        return questions

    def get_questions_lastday(self):
        today = datetime.date.today()
        date = today - datetime.timedelta(1)
        url = 'https://api.stackexchange.com/2.3/questions'
        params = {
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'activity',
            'fromdate': f'{date}',
            'todate': f'{today}'
        }
        response = requests.get(url, params=params)
        resp = response.json()
        questions = {}
        for items in resp['items']:
            unix_date = items['last_activity_date']
            date = datetime.datetime.utcfromtimestamp(unix_date).strftime('%Y-%m-%d')
            questions.setdefault(items['question_id'], {date: items['link']})

        return questions

    def get_answers_ids(self, id: int):
        url = 'https://api.stackexchange.com/2.3/answers/'
        params = {
            'ids': id,
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'activity',
        }
        response = requests.get(url, params=params).json()
        return response

    def get_info_site(self):
        params = {
            'site': 'Stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.3/info', params=params).json()
        return response

    def get_all_posts(self):
        params = {
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'activity'
        }
        response = requests.get('https://api.stackexchange.com/2.3/posts', params=params).json()
        return response

    def get_posts_ids(self, id):
        params = {
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'activity',
            'ids': id
        }
        response = requests.get('https://api.stackexchange.com/2.3/posts', params=params).json()
        return response

    def get_collectives_slugs(self, slugs):
        params = {
            'site': 'Stackoverflow',
            'order': 'desc',
            'sort': 'name',
            'slugs': slugs
        }
        response = requests.get('https://api.stackexchange.com/2.3/collectives', params=params).json()
        return response