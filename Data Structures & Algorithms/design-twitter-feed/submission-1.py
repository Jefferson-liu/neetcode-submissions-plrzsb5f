from collections import deque,defaultdict
import heapq
class Twitter:

    def __init__(self):

        self.userTweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if len(self.userTweets[userId]) > 10:
            self.userTweets[userId].popleft()
        self.userTweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for user in self.following[userId]:
            for tweet in self.userTweets[user]:
                heapq.heappush_max(maxHeap, tweet)
        for tweet in self.userTweets[userId]:
            heapq.heappush_max(maxHeap, tweet)
        
        feed = []
        count = 0
        while maxHeap and count < 10:
            feed.append(heapq.heappop_max(maxHeap)[1])
            count += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
