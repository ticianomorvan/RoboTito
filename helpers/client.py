class Client:
    def __init__(self, githubURL: str):
        self.githubURL = githubURL

    def get_github(self):
        return self.githubURL
