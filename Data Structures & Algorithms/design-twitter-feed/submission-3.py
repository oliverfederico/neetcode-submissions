from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # Decrement so more recent tweets are "smaller" for the min-heap

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []
        
        # Include the user's own tweets + the people they follow
        followees = self.followMap[userId].copy()
        followees.add(userId)

        # 1. Initialize the heap with the most recent tweet from each followee
        for followeeId in followees:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Push: [time_count, tweet_id, followee_id, next_index_to_check]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # 2. Pop the most recent tweet and push the next most recent tweet from that user
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index >= 0:
                next_count, next_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [next_count, next_tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)