# we need to map userIds to followerId, 
# userId to postId
# 
class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = defaultdict(set)    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i = len(self.tweets)-1
        while len(feed) < 10 and i >= 0:
            if self.tweets[i][0] in self.following[userId] or self.tweets[i][0] == userId:
                feed.append(self.tweets[i][1])
            i-=1
        return feed 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
           self.following[followerId].remove(followeeId)
