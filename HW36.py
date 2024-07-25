class VideoContent:
    total_videos = 0

    def __init__(self, title, licensor, duration):
        self.title = title
        self.licensor = licensor
        self.duration = duration
        VideoContent.total_videos += 1

    def get_duration_minutes(self):
        return self.duration / 60

    def display_info(self):
        print(
            f"Title: {self.title}, Licensor: {self.licensor}, Duration: {self.duration} seconds ({self.get_duration_minutes()} minutes)")

    @classmethod
    def display_total_videos(cls):
        print(f"Total videos: {cls.total_videos}")

    @staticmethod
    def is_premium(duration):
        return duration > 1200


class PremiumVideoContent(VideoContent):
    def __init__(self, title, licensor, duration, price):
        super().__init__(title, licensor, duration)
        self.price = price

    def display_info(self):
        super().display_info()
        print(f"Price: {self.price} EURO")


class Publisher:

    total_publishers = 0

    def __init__(self, name, website):
        self.name = name
        self.website = website
        self.videos = []
        Publisher.total_publishers += 1

    def add_video(self, video):
        self.videos.append(video)

    def display_info(self):
        print(f"Publisher: {self.name}, Website: {self.website}")
        print("Videos:")
        for video in self.videos:
            video.display_info()

    @classmethod
    def display_total_publishers(cls):
        print(f"Total publishers: {cls.total_publishers}")


class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.subscriptions = []

    def subscribe(self, subscription):
        self.subscriptions.append(subscription)

    def display_info(self):
        print(f"User: {self.username}, Email: {self.email}")
        print("Subscriptions:")
        for subscription in self.subscriptions:
            subscription.display_info()


class Subscription:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Subscription: {self.name}, Price: {self.price} USD")


class Platform:

    def __init__(self):
        self.publishers = []
        self.users = []

    def add_publisher(self, publisher):
        self.publishers.append(publisher)

    def add_user(self, user):
        self.users.append(user)

    def display_info(self):
        print("Platform Information:")
        print("Publishers:")
        for publisher in self.publishers:
            publisher.display_info()
        print("Users:")
        for user in self.users:
            user.display_info()


# Create instances and demonstrate their work

# VideoContent and PremiumVideoContent instances
video1 = VideoContent("News Highlights", "TV Channel", 900)
video2 = PremiumVideoContent("Weekly Review", "News Agency", 1500, 19.99)

# Publisher instances
publisher1 = Publisher("News Publisher", "www.newspublisher.com")
publisher2 = Publisher("Entertainment Publisher", "www.entertainmentpublisher.com")

# Adding videos to publishers
publisher1.add_video(video1)
publisher1.add_video(video2)

# User and Subscription instances
user1 = User("john_doe", "john@example.com")
subscription1 = Subscription("Basic Plan", 9.99)
subscription2 = Subscription("Premium Plan", 19.99)

# Adding subscriptions to user
user1.subscribe(subscription1)
user1.subscribe(subscription2)

# Platform instance
platform = Platform()

# Adding publishers and users to platform
platform.add_publisher(publisher1)
platform.add_publisher(publisher2)
platform.add_user(user1)

# Displaying information
platform.display_info()