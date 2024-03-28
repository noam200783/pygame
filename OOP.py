import random


class UserTiktok:
    def __init__(self, user_name, topics):
        self.user_name = user_name
        self.topics = topics

    def display_information_to_the_user(self):
        print("Name:", self.user_name)
        interests = self.topics.keys()
        print("Interests:", interests)

    def watch_the_video(self, search):
        if search in self.topics:
            self.topics[search] += 1
        else:
            self.topics[search] = 1

    def suggest_video(self):
        next_video = random.choices(list(self.topics.keys()))
        print("Next suggested video  :", next_video)


noam = UserTiktok("noam", {"tv": 1})
noam.display_information_to_the_user()
noam.watch_the_video("cat")
noam.display_information_to_the_user()
noam.watch_the_video("israel")
noam.display_information_to_the_user()
noam.watch_the_video("israel")
noam.display_information_to_the_user()
noam.suggest_video()


class InfluencerTiktok(UserTiktok):
    def __init__(self, user_name, topics, followers):
        super().__init__(user_name, topics)
        self.followers = followers

    def display_information(self):
        print("Name:", self.user_name)
        interests = self.topics.keys()
        print("Interests:", interests)
        print(f"followers:{self.followers}")

    def add_followers(self):
        self.followers += 1

    def get_paid(self):
        if self.followers < 1000:
            print(f"your paid:{self.followers * 1}")
        elif 1000 < self.followers < 10000:
            print(f"your paid:{self.followers * 2}")
        else:
            print(f"your paid:{self.followers * 3}")


ori = InfluencerTiktok("ori", {"tv": 1}, 5000)
ori.display_information()
ori.watch_the_video("dog")
ori.display_information()
ori.watch_the_video("israel")
ori.display_information()
ori.watch_the_video("israel")
ori.display_information()
ori.suggest_video()
ori.add_followers()
ori.add_followers()
ori.add_followers()
ori.add_followers()
ori.add_followers()
ori.display_information()
ori.get_paid()
