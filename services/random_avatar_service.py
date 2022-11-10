import requests


class RandomAvatarService:
    @staticmethod
    def get():
        r = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
        return r.json()[0]
